from accounts.models import CustomUser
import datetime
import random
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from trending.models import Trending
from subcat.models import SubCat
from cat.models import Cat
from comments.models import Comment
from subcat.models import SubCat
from django.shortcuts import redirect, render
from .models import News
from main.models import Main


# Create your views here.

def news_list(request):
    news = News.objects.all()
    print(request.user)
    context = {
        'news': news
    }
    return render(request, 'adminpanel/news/index.html', context)


def news_detail(request,word):
    
    site = Main.objects.get(pk=1)
    news = News.objects.all().order_by('-pk')
    cat = Cat.objects.all()
    subcat = SubCat.objects.all()
    lastnews = News.objects.all().order_by('-pk')[:3]

    shownews = News.objects.filter(name=word)
    popnews = News.objects.all().order_by('-show')
    popnews2 = News.objects.all().order_by('-show')[:3]
    trending = Trending.objects.all().order_by('-pk')[:5]

    tagname = News.objects.get(name=word).tag
    tag = tagname.split(',')

    try :

        mynews = News.objects.get(name=word)
        mynews.show = mynews.show + 1
        mynews.save()

    except:

        print("Can't Add Show")

    code = News.objects.get(name=word).pk
    comment = Comment.objects.filter(news_id=code, status=1).order_by('-pk')[:3]
    cmcount = len(comment)

    link = "/urls/" + str(News.objects.get(name=word).rand)

    return render(request, 'front/news_detail.html', {'site':site, 'news':news, 'cat':cat, 'subcat':subcat, 'lastnews':lastnews, 'shownews':shownews, 'popnews':popnews, 'popnews2':popnews2, 'tag':tag, 'trending':trending, 'code':code, 'comment':comment, 'cmcount':cmcount, 'link':link})
def news_detail_short(request, pk):
    site  =  Main.objects.get(pk=1)
    news = News.objects.all().order_by('-pk')
    cat = Cat.objects.all()
    subcat = SubCat.objects.all()
    lastnews = News.objects.all().order_by('-pk')[:3]

    shownews = News.objects.filter(rand=pk)
    popnews = News.objects.all().order_by('-show')
    popnews2 = News.objects.all().order_by('-show')[:3]
    trending = Trending.objects.all().order_by('-pk')[:5]

    tagname = News.objects.get(rand=pk).tag
    tag = tagname.split(',')

    try:
        mynews = News.objects.get(rand=pk)
        mynews.show = mynews.show + 1
        mynews.save()
    except:
        print('Can`t add Show')

    link = "/urls/" + str(News.objects.get(name=word).rand)
    context = {'site':site, 'news':news, 'cat':cat, 'subcat':subcat, 'lastnews':lastnews, 'shownews':shownews, 'popnews':popnews, 'popnews2':popnews2, 'tag':tag, 'trending':trending, 'link':link}
    return render(request,'front/news_detail.html', context)

def news_add(request):

    # login check start
    if not request.user.is_authenticated :
        return redirect('mylogin')
    # login check end

    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day
    
    if len(str(day)) == 1 :
        day = "0" + str(day)
    if len(str(month)) == 1 :
        month = "0" + str(month)

   
    today = str(year) + "/" + str(month) + "/" + str(day)
    time = str(now.hour) + ":" + str(now.minute)

    date = str(year) + str(month) + str(day)
    randint = str(random.randint(1000,9999))
    rand = date + randint
    rand = int(rand)

    while len(News.objects.filter(rand=rand)) != 0 :
        randint = str(random.randint(1000,9999))
        rand = date + randint
        rand = int(rand)

    cat = SubCat.objects.all()
    
    if request.method == 'POST':

        newstitle = request.POST.get('newstitle')
        newscat = request.POST.get('newscat')
        newstxtshort = request.POST.get('newstxtshort')
        newstxt = request.POST.get('newstxt')
        newsid = request.POST.get('newscat')
        tag = request.POST.get('tag')


        if newstitle == "" or newstxtshort == "" or newstxt == "" or newscat == "" :
            messages.error(request,"All Fields Requirded")
            # return render(request, 'back/error.html' , {'error':error})

        
        try : 

            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            url = fs.url(filename)

            if str(myfile.content_type).startswith("image"):

                if myfile.size < 5000000 :

                    newsname = SubCat.objects.get(pk=newsid).name
                    ocatid = SubCat.objects.get(pk=newsid).catid

                    b = News(name=newstitle, short_txt=newstxtshort, body_txt=newstxt, date=today, picname=filename, picurl=url, writer=request.user, catname=newsname, catid=newsid, show=0, time=time, ocatid=ocatid, tag=tag, rand=rand)
                    b.save()

                    count = len(News.objects.filter(ocatid=ocatid))

                    b = Cat.objects.get(pk=ocatid)
                    b.count = count
                    b.save()

                    return redirect('news_list')

                else:

                    fs = FileSystemStorage()
                    fs.delete(filename)

                    messages.error(request,"Your File Is Bigger Than 5 MB")
                    # return render(request, 'back/error.html' , {'error':error})

            else:

                fs = FileSystemStorage()
                fs.delete(filename)

                messages.error(request,"Your File Not Supported")
                # return render(request, 'back/error.html' , {'error':error})

        except Exception as e:

            # error = "Please Input Your Image"
            messages.error(request, 'Error {}'.format(str(e)))
            # return render(request, 'back/error.html' , {'error':error})

    return render(request, 'adminpanel/news/create.html', {'cat':cat})




def news_update(request, pk):
    news = News.objects.get(pk=pk)
    cat = SubCat.objects.all()

    if request.method == "POST":
        newstitle = request.POST.get('newstitle')
        newscat = request.POST.get('newscat')
        newstxtshort = request.POST.get('newstxtshort')
        newstxt = request.POST.get('newstxt')
        newsid = request.POST.get('newscat')
        tag = request.POST.get('tag')

        if newstitle == "" or newstxtshort == "" or newstxt == "" or newscat == "":
            messages.error(request,'All Fields Requirded')

            return redirect('news_edit')

        try:
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            url = fs.url(filename)

            if str(myfile.content_type).startswith('image'):
                if myfile.size < 5000000:
                    newsname = SubCat.objects.get(pk=newsid).name
                    b = News.objects.get(pk=pk)
                    fss = FileSystemStorage()
                    fss.delete(b.picname)
                    
                    b.name = newstitle
                    b.short_txt = newstxtshort
                    b.body_txt = newstxt
                    b.picname = filename
                    b.picurl = url
                    b.catname = newsname
                    b.catid = newsid
                    b.tag = tag
                    b.act = 0

                    b.save()
                    return redirect('news_list')
                else:
                    fs = FileSystemStorage()
                    fs.delete(filename)
                    messages.error(request,'Your File Is Bigger Than 5mb')
                    return redirect('news_list')
            else:
                fs = FileSystemStorage()
                fs.delete(filename)
                messages.error(request,'Your File Not Supported')
                return redirect('news_list')
        except Exception as e:
            newsname = SubCat.objects.get(pk=newsid).name
            b = News.objects.get(pk=pk)

            b.name = newstitle
            b.short_txt = newstxtshort
            b.body_txt = newstxt
            b.catname = newsname
            b.catid = newsid
            b.tag = tag

            b.save()
            
            return redirect('news_list')

    context = {
        'pk': pk,
        'news': news,
        'cat': cat
    }
    return render(request,'adminpanel/news/update.html', context)



def news_delete(request, pk):
    try:
        b = News.objects.get(pk=pk)
        fs = FileSystemStorage()
        fs.delete(b.picname)

        ocatid = News.objects.get(pk=pk).ocatid
        b.delete()
        count = len(News.objects.filter(ocatid=ocatid))

        m = Cat.objects.get(pk=ocatid)
        m.count = count
        m.save()

    except Exception as e:
        messages.error(request, str(e))
        return render(request, "")

    return redirect("news_list")

def news_publish(request, pk):
    news = News.objects.get(pk=pk)
    news.act = 1
    news.save()
    return redirect('news_list')

def news_all_show(request, word):
    catid = Cat.objects.get(name=word).pk
    allnews = News.objects.filter(ocatid=catid)
    site = Main.objects.get(pk=1)
    news = News.objects.filter(act=1).order_by('-pk')
    cat = Cat.objects.all()
    subcat = SubCat.objects.all()
    lastnews = News.objects.filter(act=1).order_by('-pk')[:3]
    popnews = News.objects.filter(act=1).order_by('-show')
    popnews2 = News.objects.filter(act=1).order_by('-show')[:3]
    trending = Trending.objects.all().order_by('-pk')[:5]
    lastnews2 = News.objects.filter(act=1).order_by('-pk')[:4]
    context = {'site':site, 'news':news, 'cat':cat, 'subcat':subcat, 'lastnews':lastnews, 'popnews':popnews, 'popnews2':popnews2, 'trending':trending, 'lastnews2':lastnews2, 'allnews':allnews}
    return render(request, 'front/all_news.html', context)


def Testing(request, username):
    context = {
        'name': "renaldy",
        "username": username,
        'pendidikan': 'Kuliah' 
    }
    return render(request, 'front/tes.html', context)