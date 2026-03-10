from django.urls import path

from . import views

app_name = "users"
urlpatterns = [
    path("redirect/", view=views.UserRedirectView.as_view(), name="redirect"),
    path(
        "update-profile/", view=views.UserUpdateView.as_view(), name="user_update_view"
    ),
    path(
        "<str:username>/", view=views.UserDetailView.as_view(), name="user_detail_view"
    ),
]
