from django.urls import include, path
from . import views

urlpatterns = [
    path("create_page/<int:pk>", views.create1 , name="create_page"),
    path("edit_page/<int:pk>", views.create1 , name="edit_page"),
]