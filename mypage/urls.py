from django.urls import include, path
from . import views

urlpatterns = [
    path("edit_page/<int:pk>", views.edit_page, name="edit_page")
]