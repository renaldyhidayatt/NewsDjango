from django.shortcuts import render, redirect
from contactform.models import ContactForm
from django.contrib import messages
import datetime

# Create your views here.
def contact_add(request):
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day
    
    if len(str(day)) == 1:
        day = "0" + str(day)
    if len(str(month)) == 1:
        month = "0" + str(month)

    today = str(year) + '/' + str(month) + "/" + str(day)
    time = str(now.hour) + ":" + str(now.minute)

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        txt= request.POST.get('msg')

        if name == "" or email == "" or txt == "":
            messages.error(request,'All FIelds Required')
            return redirect('home')
        b = ContactForm.objects.create(name=name, email=email, txt=txt,date=today,time=time)
        b.save()
        messages.success(request,'You Message Receved')

    return redirect('home')
            


def contact_show(request):
    msg = ContactForm.objects.all()
    context = {
        'msg': msg
    }
    return render(request, 'adminpanel/contactform/index.html', context)

def contact_del(request, pk):
    b = ContactForm.objects.filter(pk=pk)
    b.delete()
    return redirect('contact_show')