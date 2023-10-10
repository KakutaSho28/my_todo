# ここにURLの設定を書いていく。
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
]