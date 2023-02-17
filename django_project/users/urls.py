from django.urls import path
from users import views as user_views

urlpatterns = [
    path("register/", user_views.register, name='user-register'),
    path("profile/", user_views.profile, name='user-profile'),
]
