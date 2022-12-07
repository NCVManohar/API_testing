from django.urls import path
from apis import views

urlpatterns = [
    path('api/tutorials/', views.tutorial_list),
    path('api/tutorials/<int:pk>/', views.tutorial_detail),
]