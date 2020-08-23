from django.urls import include, path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('signup/',views.signup, name="signup"),
    path('profile/<int:pk>',views.profile, name="profile"),
    path('profile_update/<int:pk>',views.profile_update, name="profile_update"),
    path('login/',LoginView.as_view(), name="login"),
    path('logout/',LogoutView.as_view(), name="logout"),
]
