from typing import Any
from django.db import models
from uuid import uuid4
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('email field required')

        email = self.normalize_email(email)
        user = self.model(email=email, username=username)
        user.set_password(password)

        user.save()
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
       user = self.create_user(email=email, username=username, password=password)
       user.is_staff = True
       user.is_admin = True
       user.is_superuser = True
       user.save()
       return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255)
    bio = models.CharField(max_length=150, null=True, blank=True)
    mention = models.CharField(max_length=50)
    profile_pic = models.ImageField(null=True, blank=True)
    followers_count = models.IntegerField(default=0)
    following_count = models.IntegerField(default=0)
    post_count = models.IntegerField(default=0)
    bookmark_count = models.IntegerField(default=0)
    email_verifed = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    def __str__(self) -> str:
        return f'email:{self.email} username:{self.username}'

class Lists(models.Model):
    user_list = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_list')
    list_name = models.CharField(max_length=255)
    descritpion = models.CharField(max_length=255, blank=True)
    craeted_at = models.DateTimeField(auto_now=True)

class Post(models.Model):
    user_post = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_post')
    post_content = models.CharField(max_length=240)
    post_img = models.ImageField(null=True, blank=True)
    is_comment = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    list = models.ManyToManyField(Lists, blank=True)
    comment_count = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    bookmark = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f'user: {self.user_post.username}, content: {self.post_content}'

class Like(models.Model):
    user_like = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_like')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_like')

class Bookmark(models.Model):
    user_bookmark = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_bookmark')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_bookmark')

class Follow(models.Model):
    to_follow = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_following")
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_followers")

class Comment(Post, models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comment')

class Verification(models.Model):
    token = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='verify_user')