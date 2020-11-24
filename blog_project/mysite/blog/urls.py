from django.urls import path
from mysite.blog import views

urlpatterns = {
    path('about/', views.AboutView.as_view(), name='about')
}