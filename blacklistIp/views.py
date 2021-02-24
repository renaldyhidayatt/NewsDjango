from datetime import datetime
from blacklistIp.models import BlackList
from django.shortcuts import redirect, render

# Create your views here.


def back_list(request):
    b = BlackList.objects.all()
    context = {"black": b}
    return render(request, "adminpanel/blacklist/index.html", context)


def ip_add(request):

    if request.method == "POST":

        now = datetime.now()
        year = now.year
        month = now.month
        day = now.day

        if len(str(day)) == 1:
            day = "0" + str(day)
        if len(str(month)) == 1:
            month = "0" + str(month)

        today = str(year) + "/" + str(month) + "/" + str(day)
        time = str(now.hour) + ":" + str(now.minute)

        ip = request.POST.get("ip")

        if ip != "":

            # BlackList.objects.create(ip=ip, date=today)
            b = BlackList(ip=ip, date=today)
            b.save()

    return redirect("blacklist")


def ip_del(request, pk):

    b = BlackList.objects.filter(pk=pk)
    b.delete()

    return redirect("blacklist")


## add ip addres
# def ipAdd(request):
