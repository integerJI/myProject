# myMember/views.py

from django.shortcuts import render, redirect # 로그인 / 로그아웃 View 템플릿
from django.contrib.auth.views import LoginView, LogoutView # DB의 USER
from django.contrib.auth.models import User
from django.conf import settings # setting.py에서 오버라이딩

def signup(request):
    if request.method == 'POST':
        # 비밀번호 1과 2를 비교 같으면 실행
        if request.POST['password1'] == request.POST['password2']:
            # User Model에 새로운 유저 생성
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
            # 로그인 페이지로 이동
            return redirect('signin')
    # 아닐경우 회원가입 페이지
    return render(request, 'signup.html')


class Loginviews(LoginView):
    # 로그인을 할때 나올 페이지
    template_name = 'signin.html'
signin = Loginviews.as_view()


class LogoutViews(LogoutView):
    # setting.py에 설정해준 값
    next_page = settings.LOGOUT_REDIRECT_URL
signout = LogoutViews.as_view()