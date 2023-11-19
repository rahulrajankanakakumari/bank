import json
from django.shortcuts import render
from .forms import PersonForm
from django.http import JsonResponse
import json
from .models import City
# Create your views here.

from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import logout



def index(request):
    return render(request, "index.html")

def home_page(request):
    return render(request, "home_page.html")
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("personal:signin")
    else:
        form = UserCreationForm()
    return render(request, "create_account.html", {"form": form})

def sign_in(request):
    if request.method == "POST":
        form =AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # return redirect("profiles:account_status")
            # return redirect("profiles:dashboard")
            return redirect("personal:home_page")
    else:
        form = AuthenticationForm()

        #print('invalid')
    return render(request, "sign_in.html",{"form": form})


def logout_view(request):
    # Logout the user if he hits the logout submit button
    logout(request)
    return redirect("personal:signin")

def Aplication_Form(request):
    if request.method == "POST":
        form =AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # return redirect("profiles:account_status")
            # return redirect("profiles:dashboard")
            return redirect("personal:Ap_accepted")
    else:
        form = AuthenticationForm()

        #print('invalid')
    return render(request, "Aplication_Form.html")
    # return render(request, "Aplication_Form.html")


def Application_accepted(request):
    return render(request, "Ap_accepted.html")

def Branches(request):
    return render(request, "Branches_Type.html")


def person(request):
    form = PersonForm()
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("personal:Ap_accepted")
    return render(request, "person.html", {"form": form})

def cities(request):
    data = json.loads(request.body)
    cities = City.objects.filter(country__id=data['user_id'])
    print(cities)
    return JsonResponse(list(cities.values("id", "name")), safe=False)
