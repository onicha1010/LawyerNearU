from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.index),
    path('about',views.about),
    path('from',views.form),
]