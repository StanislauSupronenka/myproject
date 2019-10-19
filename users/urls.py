from django.urls import path

from users import views


urlpatterns = [
    path("", views.login_view),
    path("registration", views.registration),
    path("logout", views.logout_view)
    ]