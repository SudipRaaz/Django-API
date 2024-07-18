from django.urls import path
from rest_framework.decorators import api_view
from . import views

urlpatterns = [
    path('blogposts/', views.BlogPostListCreate.as_view(), name="blogpost-view-create"),
    path('blogposts/<int:pk>/', views.BlogPostRetrieveUpdateDestroy.as_view(), name="update-blogpost"),
    path('blogposts/<str:title>/', views.BlogPostRetrieveTitle.as_view(), name="searchusing- titles"),
    path('blogposts/<str:title>/', views.BlogPostRetrieve.as_view(), name="search-titles"),
    path('login/', views.Login, name="login"),
    path("signup/", views.Signup, name="singup"),
    # path("testtoken/", views.Test_token, name="test-tokens"),
    path("getusers/", views.userlistfetcher.as_view(), name="get-users"),
    path("getusers/<int:pk>/", views.ReadUpdateDeleteUser.as_view(), name="rud-users"),

]