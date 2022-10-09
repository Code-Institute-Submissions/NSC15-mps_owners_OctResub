from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from . import views


urlpatterns = [
    path('', views.PostView.as_view(), name='index'),
    path("<slug:slug>", login_required(views.Postinfo.as_view()), name='post_info'),
    path('comment/edit/<int:pk>', staff_member_required(views.UpdateComment.as_view()), name='edit_comment'),
    path('comment/delete/<int:pk>', staff_member_required(views.DeleteComment.as_view()), name='delete_comment'),
]
