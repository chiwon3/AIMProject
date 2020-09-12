from django.urls import include, path
from . import views

urlpatterns = [
    path("create_page/<int:pk>", views.create1 , name="create_page"),
    path("edit_page1/<int:pk>", views.create1 , name="edit_page1"),
    path("edit_page2/<int:pk>", views.create2 , name="edit_page2"),
    path("edit_page3/<int:pk>", views.create3 , name="edit_page3"),
]