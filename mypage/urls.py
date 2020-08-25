from django.urls import include, path
from . import views

urlpatterns = [
    path("create_page/<int:pk>", views.create_page , name="create_page"),
    path("edit_page_11/<int:pk>", views.edit_page_11 , name="edit_page_11"),
    path("edit_page_12/<int:pk>", views.edit_page_12 , name="edit_page_12"),
    path("edit_page_13/<int:pk>", views.edit_page_13 , name="edit_page_13"),
    path("edit_page_21/<int:pk>", views.edit_page_21 , name="edit_page_21"),
    path("edit_page_22/<int:pk>", views.edit_page_22 , name="edit_page_22"),
    path("edit_page_23/<int:pk>", views.edit_page_23 , name="edit_page_23"),
    path("edit_page_31/<int:pk>", views.edit_page_31 , name="edit_page_31"),
    path("edit_page_32/<int:pk>", views.edit_page_32 , name="edit_page_32"),
    path("edit_page_33/<int:pk>", views.edit_page_33 , name="edit_page_33"),
]