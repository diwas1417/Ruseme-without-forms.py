from django.contrib import admin
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.home,name='home'),
    path('register/', views.register, name="register"),
    path('login/', views.user_login, name="login"),
    path('cvs/', views.info, name="cvs"),
    path('delete/<int:id>/', views.delete, name="delete"),
    path('profile/<int:id>/', views.profile, name="profile"),
    path('createpdf/<int:id>',views.pdf_report_create,name='createpdf'),
    path('logout/',views.user_logout,name='logout'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
