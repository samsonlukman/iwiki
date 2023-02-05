from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry>", views.user_entry, name="search"),   
    path("query/", views.query, name="query"),
    path("new_page/", views.new_page, name="new_page"),
    path("edit_page", views.edit_page, name="edit_page"),
    path("save_edit", views.save_edit, name="save_edit"),
    path("random_page", views.random_page, name="random_page",)
    
]

"""the string entry allows the user input keywords that acts as paths,
    the path is linked to the user_entry function in views while search allows to
    manipulate the path"""


