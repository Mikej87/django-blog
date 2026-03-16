from django.urls import path
from . import views

urlpatterns = [
    # Replace these with your actual blog views
    path("", views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path("<int:event_id>/", views.event_detail, name="event_detail"),
]