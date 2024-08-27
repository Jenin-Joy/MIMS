from django.urls import path
from Guest import views
app_name = "Guest"

urlpatterns =[
    path("officer/",views.officer,name="officer"),
    path("ajaxplace/",views.ajaxplace,name="ajaxplace"),
    path("login/",views.login,name="login"),
]