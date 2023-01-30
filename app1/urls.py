from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("about/", views.about, name='about'),
    path("contact/", views.contact, name='contact'),
    path("dashboard/", views.dashboard, name='dashboard'),
    path("signup/", views.signup, name='signup'),
    path("login/", views.login, name='login'),
    path("logout/", views.logout, name='logout'),
    path("addpost/", views.add_post, name='addpost'),
    path("updatepost/<int:id>/", views.update_post, name='updatepost'),
    path("deletepost/<int:id>/", views.delete_post, name='deletepost'),
]
