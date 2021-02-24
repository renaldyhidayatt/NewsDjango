from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Comment
from news.models import News
from cat.models import Cat
from subcat.models import SubCat
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage
from trending.models import Trending
# from django.contrib.auth.models
from accounts.models import CustomUser
import random
import string
import datetime

# Create your views here.
def news_cm_add(request, pk):
    if request.method == 'POST':
        now = datetime.datetime.now()
        year = now.year
        month = now.month
        day = now.day

        if len(str(day)) == 1:
            day = "0" + str(day)
        if len(str(month)) == 1:
            month = "0" + str(month)

        today = str(year) + "/" + str(month) + "/" + str(day)
        time = str(now.hour) + ":" + str(now.minute)

        cm = request.POST.get('msg')

        if request.user.is_authenticated:
            if request.user.user_type == "A":
                user = CustomUser.objects.get(pk=request.user.id)
                b = Comment.objects.create(name=user.first_name, email=user.email, cm=cm, news_id=pk, date=today, time=time)
        else:
            name = request.POST.get('name')
            email = request.POST.get('email')

            b = Comment.objects.create(name=name, email=email, cm=cm, news_id=pk,date=today, time=time)

    newsname = News.objects.get(pk=pk).name

    return redirect('news_detail', word=newsname)


def comments_list(request):
    if request.user.user_type == "A":
        comment = Comment.objects.all()
        return render(request, 'adminpanel/comments/index.html', { 'comment': comment})
    elif request.user.user_type == "M":
        comment = Comment.objects.all()
        return render(request, 'adminpanel/comments/index.html', { 'comment': comment})
    else:

        return redirect(reverse('home'))

def comments_del(request,pk):
    comment = Comment.objects.filter(pk=pk)
    comment.delete()
    return redirect('comments_list')

def comments_confirme(request,pk):
    comment = Comment.objects.get(pk=pk)
    comment.status = 1
    comment.save()
    return redirect('comments_list')