from django.urls import path, include
from rest_framework import routers
from .views import TaskViewSet, CategoryViewSet, CreateUserView, ListUserView, LoginUserView, ProfileViewSet
from django.contrib.auth import views

router = routers.DefaultRouter()
router.register('category', CategoryViewSet)
router.register('tasks', TaskViewSet)
router.register('profile', ProfileViewSet)

urlpatterns = [
    path('create/', CreateUserView.as_view(), name='create'),
    path('users/', ListUserView.as_view(), name='users'),
    path('loginuser/', LoginUserView.as_view(), name='loginuser'),

    path('accounts/password_reset/', views.PasswordResetView.as_view(),
         name='password_reset'),
    path('accounts/password_reset/done/', views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('accounts/reset/done/', views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
    path('', include(router.urls)),
]