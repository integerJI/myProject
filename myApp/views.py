# myApp/views.py

from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Post, Comment
from myMember.models import Profile

try:
    from django.utils import simplejson as json
except ImportError:
    import json
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_POST

def index(request):
    posts = Post.objects.order_by('-id')
    app_url = request.path

    conn_user = request.user
    conn_profile = Profile.objects.get(user=conn_user)

    if not conn_profile.profile_image:
        pic_url = ""
    else:
        pic_url = conn_profile.profile_image.url
            
    context = {
        'id' : conn_user.username,
        'nick' : conn_profile.nick,
        'profile_pic' : pic_url,
        'intro' : conn_profile.intro,
        'posts' : posts,
        'app_url' : app_url,
    }
    return render(request, 'index.html', context=context)

def post(request):
    if request.method == 'POST':
        post = Post()
        post.main_text = request.POST['main_text']
        post.create_img = request.FILES['create_img']
        post.create_user = User.objects.get(username = request.user.get_username())
        post.save()
        return redirect(reverse('index'))
    return render(request, 'post.html')

def detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'detail.html', {'post': post})
    
def update(request, post_id):
    post = Post.objects.get(id = post_id)
    if request.method == 'POST':
        post.main_text = request.POST['main_text']
        post.create_user = User.objects.get(username = request.user.get_username())
        post.save()
        return redirect(reverse('index'))
    return render(request, 'update.html')

def delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect(reverse('index'))

@login_required
def c_post(request, post_id):
    if request.method =='POST':
        comment = get_object_or_404(Post, id=post_id)
        comment_text = request.POST.get('comment_text')
        comment_user = User.objects.get(username = request.user.get_username())
        Comment.objects.create(comment=comment, comment_text=comment_text, comment_user=comment_user)

        if request.POST.get('app_url') == '/myApp/index/':
            return redirect(reverse('index'), post_id)
        else :
            return redirect('detail', post_id)

@login_required
def c_delete(request, post_id, comment_id):
    post = get_object_or_404(Post, id=post_id)
    comment = get_object_or_404(Comment, id=comment_id)

    if request.method =='POST':
            
        comment.delete()
        
        if request.POST.get('app_url') == '/myApp/index/':
            return redirect(reverse('index'), post_id)
        else :
            return redirect('detail', post_id)

@login_required
def c_post(request, post_id):
    if request.method =='POST':
        comment = get_object_or_404(Post, id=post_id)
        comment_text = request.POST.get('comment_text')
        comment_user = User.objects.get(username = request.user.get_username())
        Comment.objects.create(comment=comment, comment_text=comment_text, comment_user=comment_user)

        if request.POST.get('app_url') == '/myApp/index/':
            return redirect(reverse('index'), post_id)
        else :
            return redirect('detail', post_id)

@login_required
def c_delete(request, post_id, comment_id):
    post = get_object_or_404(Post, id=post_id)
    comment = get_object_or_404(Comment, id=comment_id)

    if request.method =='POST':
            
        comment.delete()
        
        if request.POST.get('app_url') == '/myApp/index/':
            return redirect(reverse('index'), post_id)
        else :
            return redirect('detail', post_id)

@login_required
@require_POST
def like(request):
    if request.method == 'POST':
        user = request.user 
        create_user = request.POST.get('pk', None)
        post = get_object_or_404(Post, id=create_user)

        if post.post_likes.filter(id = user.id).exists():
            post.post_likes.remove(user) 
            message = '좋아요 취소'
        else:
            post.post_likes.add(user)
            message = '좋아요!'

    context = {'likes_count' : post.total_likes, 'message' : message}
    return HttpResponse(json.dumps(context), content_type='application/json')
