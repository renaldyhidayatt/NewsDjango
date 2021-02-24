from django.shortcuts import render, redirect
from newsletter.models import Newsletter
# Create your views here.
def news_letter(request):
    if request.method == 'POST':
        txt = request.POST.get('txt')
        res = txt.find('@')

        if int(rest) != -1:
            b = Newsletter.objects.create(txt=txt, status=1)
            b.save()
        else:
            try:
                int(txt)
                b = Newsletter.objects.create(txt=txt, status=2)
                b.save()
            except Exception as e:
                print('Error ', str(e))
                return redirect('home')


def news_emails(request):
    emails = Newsletter.objects.filter(status=1)
    context = {
        'email': emails
    }
    return render(request,'adminpanel/newsletters/email.html', context)

def news_phone(request):
    emails = Newsletter.objects.filter(status=1)
    context = {
        'email': emails
    }
    return render(request,'adminpanel/newsletters/email.html', context)

def news_txt_del(request, pk, num):
    b = Newsletter.objects.get(pk=pk)
    b.delete()

    if int(num) == 2:
        return redirect('dashboard')
        
    return redirect('news_emails')