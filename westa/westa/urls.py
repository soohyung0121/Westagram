from django.urls import path, include

urlpatterns = [
    path('user', include('user.urls')),
    path('comment', include('comment.urls')),
]
