"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from product.views import IndexView, RegExpView, OrmView, QuestionsView, SqlView, DiscountView, GitView


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^reg-exp/', RegExpView.as_view(), name='reg_exp'),
    url(r'^orm/', OrmView.as_view(), name='orm'),
    url(r'^questions/', QuestionsView.as_view(), name='questions'),
    url(r'^sql/', SqlView.as_view(), name='sql'),
    url(r'^discount/', DiscountView.as_view(), name='discount'),
    url(r'^git/', GitView.as_view(), name='git'),
]
