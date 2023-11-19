from django.urls import path
from . import views
app_name='personal'
urlpatterns = [

     path("Branches_Type", views.Branches, name="Branches_Type"),
     path("Ap_accepted", views.Application_accepted, name="Ap_accepted"),
     path("Aplication_Form", views.Aplication_Form, name="Aplication_Form"),
     path("home_page", views.home_page, name="home_page"),
     path("signup", views.register, name="signup"),
     path("signin", views.sign_in, name="signin"),
     path("logout", views.logout_view, name="logout"),
     path("", views.index, name="index"),

     path('add_person', views.person, name = "person"),
     path('cities', views.cities, name = "cities")
]
