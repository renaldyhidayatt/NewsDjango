from django.shortcuts import render, get_object_or_404, redirect
from .models import Main
from news.models import News
from cat.models import Cat
from subcat.models import SubCat
# from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage
from trending.models import Trending
from django.contrib.auth.models import User, Group, Permission
# from manager.models import Manager
from django.contrib import messages
import random
import string
from ipware import get_client_ip
from ip2geotools.databases.noncommercial import DbIpCity
from blacklistIp.models import BlackList



# Create your views here.

def home(request):
    site = Main.objects.get(pk=1)
    news = News.objects.filter(act=1).order_by('-pk')
    cat = Cat.objects.all()
    subcat = SubCat.objects.all()
    lastnews = News.objects.filter(act=1).order_by('-pk')[:3]
    popnews = News.objects.filter(act=1).order_by('-show')
    popnews2 = News.objects.filter(act=1).order_by('-show')[:3]
    trending = Trending.objects.all().order_by('-pk')[:5]
    lastnews2 = News.objects.filter(act=1).order_by('-pk')[:4]
    context = {
        'site': site,
        'news': news,
        'cat': cat,
        'subcat': subcat,
        'lastnews': lastnews,
        'lastnews2': lastnews2,
        'trending': trending,
        'popnews': popnews,
        'popnews2': popnews2

    }
    return render(request, 'front/index.html', context)

def about(request):
    site = Main.objects.get(pk=1)
    news = News.objects.all().order_by('-pk')
    cat = Cat.objects.all()
    subcat = SubCat.objects.all()
    lastnews = News.objects.all().order_by('-pk')[:3]
    popnews2 = News.objects.all().order_by('-show')[:3]
    trending = Trending.objects.all().order_by('-pk')[:5]
    context = {
        'site': site,
        'news': news,
        'cat': cat,
        'subcat': subcat,
        'popnews2': popnews2,
        'trending': trending
    }
    return render(request,'front/about.html', context)




def site_setting(request):
    if request.method == "POST":
        name = request.POST.get("name")
        tell = request.POST.get("tell")
        fb = request.POST.get("fb")
        tw = request.POST.get("tw")
        yt = request.POST.get("yt")
        link = request.POST.get("link")
        txt = request.POST.get("txt")

        if fb == "":
            fb = "#"
        if tw == "":
            tw = "#"
        if yt == "":
            yt = "#"
        if link == "":
            link = "#"

        if name == "" or tell == "" or txt == "":
            messages.error(request, "All Fields Required")
            return redirect("home")

        try:
            myfile = request.FILES["myfile"]
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            url = fs.url(filename)
            picurl = url
            picname = filename
        except:
            picurl = "-"
            picname = "-"

        try:

            myfile2 = request.FILES["myfile2"]
            fs2 = FileSystemStorage()
            filename2 = fs2.save(myfile2.name, myfile2)
            url2 = fs2.url(filename2)

            picurl2 = url2
            picname2 = filename2

        except:

            picurl2 = "-"
            picname2 = "-"

        b = Main.objects.get(pk=1)
        b.name = name
        b.tell = tell
        b.fb = fb
        b.tw = tw
        b.yt = yt
        b.link = link
        b.about = txt

        if picurl != "-":
            b.picurl = picurl
        if picname != "-":
            b.picname = picname
        if picurl2 != "-":
            b.picurl2 = picurl2
        if picname2 != "-":
            b.picname2 = picname2

        b.save()
    site = Main.objects.get(pk=1)
    print(site)

    context = {"site": site}
    return render(request, "adminpanel/settings/index.html", context)


def about_setting(request):
    if request.method == "POST":
        txt = request.POST.get("txt")
        if txt == "":
            messages.error(request, "All Field Requirded")
            return render(request, "adminpanel/about/index.html")

        b = Main.objects.get(pk=1)
        b.abouttxt = txt
        b.save()
    about = Main.objects.get(pk=1).abouttxt

    context = {"about": about}
    return render(request, "adminpanel/about/index.html", context)

def contact(request):
    site = Main.objects.get(pk=1)
    news = News.objects.all().order_by('-pk')
    cat = Cat.objects.all()
    subcat = SubCat.objects.all()
    lastnews = News.objects.all().order_by('-pk')[:3]
    popnews2 = News.objects.all().order_by('-show')[:3]
    trending = Trending.objects.all().order_by('-pk')[:5]
    context = {
        'site': site,
        'news': news,
        'cat': cat,
        "subcat": subcat,
        'lastnews': lastnews,
        'popnews2': popnews2,
        'trending': trending
    }
    return render(request, 'front/contact.html', context)


# def HomePage(request):
#     return render(request, "front/index.html")


# def AdminCkEditor(request):
#     return render(request, "adminpanel/ckeditor.html")


# def adminPage(request):
#     return render(request, "adminpanel/index.html")


# def adminTablePage(request):
#     users = CustomUser.objects.all()

#     paginator = Paginator(users, 5)
#     page_number = request.GET.get("page")
#     page_obj = Paginator.get_page(paginator, page_number)

#     context = {"users": users, "page_obj": page_obj}

#     return render(request, "adminpanel/tables.html", context)


# def adminProfilePage(request):
#     return render(request, "adminpanel/profile.html")


# def registerPage(request):
#     return render(request, "front/index.html")
