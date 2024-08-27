from django.urls import path
from Admin import views
app_name = "Admin"

urlpatterns = [
    path("homepage/",views.homepage,name="homepage"),
    path("adminreg/",views.adminreg,name="adminreg"),
    path("deleteadmin/<int:id>",views.deleteadmin,name="deleteadmin"),

    path("department/",views.department,name="department"),
    path("deletedepartment/<int:id>",views.deletedepartment,name="deletedepartment"),
    path("editdepartment/<int:id>",views.editdepartment,name="editdepartment"),

    path("designation/",views.designation,name="designation"),
    path("deletedesignation/<int:id>",views.deletedesignation,name="deletedesignation"),
    path("editdesignation/<int:id>",views.editdesignation,name="editdesignation"),

    path("state/",views.state,name="state"),
    path("deletestate/<int:id>",views.deletestate,name="deletestate"),
    path("editstate/<int:id>",views.editstate,name="editstate"),

    path("worktype/",views.worktype,name="worktype"),
    path("deleteworktype/<int:id>",views.deleteworktype,name="deleteworktype"),
    path("editworktype/<int:id>",views.editworktype,name="editworktype"),

    path("district/",views.district,name="district"),
    path("deletedistrict/<int:id>",views.deletedistrict,name="deletedistrict"),
    path("editdistrict/<int:id>",views.editdistrict,name="editdistrict"),

    path("place/",views.place,name="place"),
    path("deleteplace/<int:id>",views.deleteplace,name="deleteplace"),
    path("ajaxdistrict/",views.ajaxdistrict,name="ajaxdistrict"),

    path("newofficer/",views.newofficer,name="newofficer"),
    path("verifyofficer/<int:id>/<int:status>",views.verifyofficer,name="verifyofficer"),
    path("approvedofficer/",views.approvedofficer,name="approvedofficer"),
    path("rejectedofficer/",views.rejectedofficer,name="rejectedofficer"),

    path('chatpage/<int:id>',views.chatpage,name="chatpage"),
    path('ajaxchat/',views.ajaxchat,name="ajaxchat"),
    path('ajaxchatview/',views.ajaxchatview,name="ajaxchatview"),
    path('clearchat/',views.clearchat,name="clearchat"),

    path('assignwork/<int:id>',views.assignwork,name="assignwork"),
    path('deleteassignwork/<int:id>',views.deleteassignwork,name="deleteassignwork"),
]