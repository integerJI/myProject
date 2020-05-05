# myApp/models.py

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import re

class Post(models.Model):
    main_text = models.CharField(max_length=200)
    create_user = models.ForeignKey(User, on_delete = models.CASCADE)
    create_date = models.DateTimeField('date published', default=timezone.now)
    update_date = models.DateTimeField('date published', null = True, default=timezone.now)
    create_img = models.ImageField(blank=True, upload_to="post/%Y/%m/%d", null=True)
    post_likes = models.ManyToManyField(User, related_name='post_likes')
    tag_set = models.ManyToManyField('Tag', blank=True)
    tag_set_2 = models.ManyToManyField('Tag_2', blank=True)

    def __str__(self):
        return self.main_text

    @property
    def total_likes(self):
        return self.post_likes.count()

    def tag_save(self):
        tags = re.findall(r'#(\w+)\b', self.main_text)

        if not tags:
            return

        for t in tags:
            tag, tag_created = Tag.objects.get_or_create(tag_name=t)
            self.tag_set.add(tag)

    def tag_save_2(self):
        tags_2 = re.findall(r'#(\w+)\b', self.main_text)

        if not tags_2:
            return

        for t_2 in tags_2:
            tag_2, tag_created_2 = Tag_2.objects.get_or_create(tag_name_2=t_2)
            self.tag_set_2.add(tag_2)

class Comment(models.Model):
    comment = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, related_name='comments')
    comment_text = models.CharField(max_length=200)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    comment_date = models.DateTimeField('date published', default=timezone.now)
    comment_update_date = models.DateTimeField('date published', null = True, default=timezone.now)
    
    class Meta:
        ordering = ['-id']
            
    def __str__(self):
        return '%s - %s' % (self.comment_user, self.comment_text) 

class Tag(models.Model):
    tag_name = models.CharField(max_length=140, unique=True)

    def __str__(self):
        return self.tag_name

class Tag_2(models.Model):
    tag_name_2 = models.CharField(max_length=140, unique=True)

    def __str__(self):
        return self.tag_name_2
