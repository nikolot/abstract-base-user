from django.urls import path
from . import views


urlpatterns = [path('signup/', views.SignUp.as_view(), name='signup'),
               path('articles/', views.CustomUserView.as_view()),
               path('articles/<int:pk>', views.CustomUserView.as_view()),
               ]
