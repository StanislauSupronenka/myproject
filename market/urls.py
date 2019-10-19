from django.urls import path

from market import views


urlpatterns = [
    path("rates", views.rates),
    path("create", views.create_deal),
    path("deals/", views.deal_list, name="view"),
    path('stats', views.get_stats, name='charts'),

    ]