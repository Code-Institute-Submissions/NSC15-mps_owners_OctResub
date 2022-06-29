from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostView.as_view(), name='index'),
    path("<slug:slug>", views.Postinfo.as_view(), name='post_info'),
    path('comment/edit/<int:pk>', views.UpdateComment.as_view(), name='edit_comment')
]
