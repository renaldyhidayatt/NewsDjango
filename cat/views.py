import csv
from django.contrib import messages
from django.http.response import HttpResponse
from cat.models import Cat
from django.shortcuts import redirect, render
from django.views.generic.base import View

# Create your views here.


def cat_list(request):
    cat = Cat.objects.all()
    context = {"cat": cat}

    return render(request, "adminpanel/cat/index.html", context)


def CatAdd(request):
    if request.method == "POST":
        name = request.POST.get("name")

        if name == "":
            messages.error(request, "All Fields Requirded")
            return redirect("cat_list")

        if len(Cat.objects.filter(name=name)) != 0:
            messages.warning(request, "This Name Used Before")
            return render(request, "")

        messages.success(request, "Successfully Cat")
        Cat.objects.create(name=name)

        return redirect("cat_list")

    return render(request, "adminpanel/cat/index.html")


def export_cat_csv(request):
    response = HttpResponse(content="text/csv")
    response["Content-Disposition"] = 'attachment; filename="cat.csv"'
    writer = csv.writer(response)
    writer.writerow(["Title", "Counter"])
    for i in Cat.objects.all():
        writer.writerow([i.name, i.count])

    return response


def import_cat_csv(request):

    if request.method == "POST":
        csv_file = request.FILES["csv_file"]
        if not csv_file.endswith(".csv"):
            error = "Please Input Csv File"
            return render(request, "back/error.html", {"error": error})
        if csv_file.multiple_chunks():
            error = "File Too Large"
            return render(request, "back/error.html", {"error": error})
        file_data = csv_file.read().decode("utf-8")
        lines = file_data.split("\n")
        for line in lines:
            fields = line.split(",")

            try:
                if (
                    len(Cat.objects.filter(name=fields[0])) == 0
                    and fields[0] != "Title"
                    and fields[0] != ""
                ):
                    b = Cat(name=fields[0])
                    b.save()

            except:
                print("finish")

    return redirect("cat_list")


def cat_del(request, pk):
    cat = Cat.objects.get(id=pk)
    cat.delete()

    return redirect("cat_list")


# def CatEdit(request):


# class CatAdd(View):
#     def get(self, request):
#         pass

#     def post(self, request):
#         pass


# class CatEdit(View):
#     def get(self, request):
#         pass

#     def post(self, request):
#         pass
