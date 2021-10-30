from django.shortcuts import render
from users.models import User, Store
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from homepage.models import *


# Create your views here.

def addfood_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))

    return render(request, "storepage/addfood.html",{
        "foods": Food.objects.all()

    })

def statistic_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))

    return render(request, "storepage/statistic.html")


def comment_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))

    return render(request, "storepage/comment.html")


'''
def storelist_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))

    return render(request, "storepage/storeitem.html",{
    "foods": Food.objects.all()

    })
'''
'''
def addfood(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))

'''


def storeitem(request, store_user):
    store = store_user
    return render(request, "storepage/storeitem.html",{
        "store": store,
        "foods": Food.objects.filter(registered_store=store)
    })
'''
def addfood(request):
    if request.method == "POST":
        Food.objects.create(
        F_name = request.POST['foodname'],
        price = request.POST['price'],
        category = request.POST['type'],
        description = request.POST['description'])
    return reverse("storepage:addfoodview")
'''