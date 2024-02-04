from django.urls import path
from . import views


urlpatterns=[
        path('register',views.RegisterView.as_view()),
        path('login',views.LoginView.as_view()),
        path('upload/', views.VideoModelViewSet.as_view({'get': 'list','post':'create'}), name='upload_video'),
        path('videos/', views.VideoListAPIView.as_view(), name='video-list'),



]