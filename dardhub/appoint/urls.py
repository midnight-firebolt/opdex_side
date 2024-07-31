from django.urls import path , include
from viewMeds import views
from . import views
urlpatterns = [
    path("",views.HomePage,name = "patient"),
    path("reg/",views.RegPage , name = "newreg"),
    path("meds/", include("viewMeds.urls")),
]