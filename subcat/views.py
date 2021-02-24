from django.contrib import messages
from django.shortcuts import redirect, render
from .models import SubCat
from cat.models import Cat

# Create your views here.
#
def subcatList(request):
    sub = SubCat.objects.all()
    cat = Cat.objects.all()
    context = {"sub": sub, "cat": cat}
    return render(request, "adminpanel/subcat/index.html", context)


def subAdd(request):
    # cat = Cat.objects.all()
    # context = {"cat": cat}
    if request.method == "POST":
        name = request.POST.get("name")
        catid = request.POST.get("cat")

        if name == "":
            messages.error(request, "All Fields Requirded")
            return redirect("subcat_list")

        if len(SubCat.objects.filter(name=name)) != 0:
            messages.error(request, "This Name Used Before")
            return render(request, "")

        catname = Cat.objects.get(pk=catid).name
        SubCat.objects.create(name=name, catname=catname, catid=catid)
        return redirect("subcat_list")
    return render(request, "adminpanel/subcat/index.html")


def subDelete(request, pk):
    sub = SubCat.objects.get(id=pk)
    sub.delete()

    return redirect("subcat_list")
