from django.urls import path
from index import views

urlpatterns = [
    path('',views.home,name='home'),
    path('filecomplaintform/',views.filecomplaintform,name='filecomplaintform'),
    path('signinupform/',views.signinupform,name='signinupform'),
    path('logoutUser/',views.logoutUser,name='logoutUser'),
    path('contactus/',views.contactus,name='contactus'),
    path('responses/',views.responses,name='responses'),
    path("search/",views.search_psdetails,name="search"),
    path("view/",views.view_psdetails,name="view"),
    path("reset/",views.reset_psdetails,name="reset"),
    path("policedetails/",views.policedetails,name="policedetails"),
    path("tactics/",views.tactics,name="tactics"),
    path("forgotPassword/",views.forgotPassword,name="forgotPassword"),
    path("resetPassword/",views.resetPassword,name="resetPassword")
]
