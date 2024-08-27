from django.urls import path
from Officer import views
app_name = "Officer"

urlpatterns = [
    path("homepage/",views.homepage,name="homepage"),

    path("profile/",views.profile,name="profile"),
    path("editprofile/",views.editprofile,name="editprofile"),
    path("changepassword/",views.changepassword,name="changepassword"),

    path("viewadmin/",views.viewadmin,name="viewadmin"),
    path('chatpage/<int:id>',views.chatpage,name="chatpage"),
    path('ajaxchat/',views.ajaxchat,name="ajaxchat"),
    path('ajaxchatview/',views.ajaxchatview,name="ajaxchatview"),
    path('clearchat/',views.clearchat,name="clearchat"),

    path('viewworks/',views.viewworks,name="viewworks"),
    path('updatework/<int:id>/<int:status>',views.updatework,name="updatework"),
]