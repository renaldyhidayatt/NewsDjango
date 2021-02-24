from trending.models import Trending
from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.


def trending_list(request):
    trending = Trending.objects.all()

    context = {"tren": trending}

    return render(request, "adminpanel/trending/index.html", context)


def trending_add(request):
    if request.method == "POST":
        txt = request.POST.get("txt")

        if txt == "":
            messages.error(request, "All Fields Requirded")
            return render(request, "")

        messages.success(request, "Successfully Create Trending")
        Trending.objects.create(txt=txt)
        return redirect("trending_list")

    return render(request, "adminpanel/trending/index.html")


def trending_delete(request, pk):
    tren = Trending.objects.get(id=pk)
    tren.delete()
    return redirect("trending_list")
