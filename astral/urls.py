"""astral URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from posts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'), #posts url
    path('posts/', include('posts.urls')), #posts url
    path('pages/', include('pages.urls')), #pages url
    path('blog/', include('blog.urls')), #blog url
    path('contact/', include('contact.urls')), #contact url
    path('membership/', include('memberships.urls')), #member url

    #AUTH
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    #ACCOUNT
    path('accounts/', include('accounts.urls')),

    #REST FRAMEWORKS
    path('api/posts/', include('posts.api.urls')),
    path('api/pages/', include('pages.api.urls')),
    path('api/accounts/', include('accounts.api.urls')),
    path('api/blog/', include('blog.api.urls')),
    path('api/contact/', include('contact.api.urls'))


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

