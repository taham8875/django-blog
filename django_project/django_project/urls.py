"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

from django.contrib import messages
from django.conf import settings
from django.conf.urls.static import static


class MyLoginView(auth_views.LoginView):

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated and 'next' in request.GET:
            messages.warning(
                request, 'You must log in first.')
        return super().get(request, *args, **kwargs)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("blog/", include('blog.urls')),
    path("login/", MyLoginView.as_view(template_name='users/login.jinja2'),
         name='user-login'),
    path("logout/", auth_views.LogoutView.as_view(template_name='users/logout.jinja2'),
         name='user-logout'),
    path("password-reset/", auth_views.PasswordResetView.as_view(template_name='users/password_reset.jinja2'),
         name='password_reset'),
    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.jinja2'),
         name='password_reset_done'),
    path("password-reset-confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.jinja2'),
         name='password_reset_confirm'),
    path("password-reset-complete/", auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.jinja2'),
         name='password_reset_complete'),
    path("", include('blog.urls')),
    path("", include('users.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
