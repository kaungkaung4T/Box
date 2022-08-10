from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="index"),
    path("registration", views.registration, name="registration"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("profile",views.profile_home, name="profile"),

    path("chat", views.chat, name="chat"),
    path("chat/<str:chatid>/", views.chat2, name="chat2"),
    path("save", views.save, name="save"),
    path("store", views.store, name="store"),
    path("sms/<str:chatid>/",views.sms, name="sms"),

    path("blog", views.blog, name="blog"),
    path("updateblog/<str:pk>", views.update_blog, name="updateblog"),
    path("deleteblog/<str:pk>", views.delete_blog, name="deleteblog"),
    path("profile2/<str:p>/", views.profile2, name="profile2"),
    path("like", views.like, name="like"),
    path("read/<str:pk>", views.read_more, name="read"),

    path("search",views.search, name="search"),
    path("file", views.file, name="file"),
    path("fileUpdate/<str:pk>", views.update_file, name="ufile"),
    path("fileDelete/<str:pk>", views.delete_file, name="dfile"),

    path("setting", views.setting, name="setting"),
    path("users", views.users, name="users"),

    path("api", views.api),


    path("rest", views.resting.as_view(), name="rest"),
    path("rest/<str:pk>/", views.resting.as_view(), name="update"),
    path("rest/<str:pk>/update", views.update_rest, name="up"),
    path("rest/<str:pk>/delete", views.delete_rest, name="del"),
    path("rest2", views.file_test.as_view(), name="rest2"),
    path("rest2/<str:pk>", views.file_test.as_view(), name="update"),

    path("rest_second/<str:pk>", views.file_test2.as_view(), name="update"),
    path("rest2/<str:pk>/update", views.update_rest2, name="up2"),
    path("rest2/<str:pk>/delete", views.delete_rest2, name="del2"),
    path("api-auth/", include("rest_framework.urls")),

    path("image", views.image, name="image"),
]

