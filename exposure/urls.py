from django.urls import path

from . import views

# app_name = 'exposure'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # About page
    path('about/', views.about, name='about'),

    # References page
    path('references/', views.references, name='references'),

    # Feedback page
    path('feedback/', views.feedback, name='feedback'),
]
