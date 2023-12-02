from django.urls import path, re_path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('signup', views.signup_view.as_view(), name='signup'),
    path('csrf-token', views.getCSRFToken.as_view(), name='csrf-token'),
    path('login', views.login_view.as_view(), name='login'),
    path('logout', views.logout_view.as_view(), name='logout'),
    path('current-user', views.getCurrentUser.as_view(), name='current-user'),
    path('post-feed', views.get_post_feed.as_view(), name='post-feed'),
    path('post-feed-by-user/<int:pk>', views.get_post_feed_by_user.as_view(), name='post-feed-by-user'),
    path('make-post', views.make_post.as_view(), name='make-post'),
    path('comment/<int:pk>', views.comment.as_view(), name='make-comment'),
    path('add-like/<int:pk>', views.add_like.as_view(), name='add-like'),
    path('edit-or-delete-post/<int:pk>',views.edit_or_delete_post.as_view(), name='edit-or-delete-post'),
    path('show-users', views.show_users.as_view(), name='show-users'),
    path('show-followers/<int:pk>', views.show_followers.as_view(), name='show-followers'),
    path('show-following/<int:pk>', views.show_following.as_view(), name='show-following'),
    path('follow/<int:pk>', views.Follow_view.as_view(), name='follow'),
    path('unfollow/<int:pk>', views.Unfollow.as_view(), name='unfollow')
]

urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]