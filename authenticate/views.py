from django.contrib.auth.models import Group
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from accounts.models import CustomUser
from django.shortcuts import redirect, render
from django.views.generic.base import View
from .utils import EmailBackend, account_activation_token

# from django.contrib.auth.models import User

from django.urls import reverse
from django.contrib import auth
from django.contrib import messages
from django.core.mail import EmailMessage
import threading


class EmailTreading(threading.Thread):
    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send(fail_silently=False)


class RegisterView(View):
    def get(self, request):
        return render(request, "auth/register.html")

    def post(self, request):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST["email"]
        password = request.POST["password"]
        gender = request.POST.get('gender')

        if len(password) < 6:
            messages.error(request, "Password too short")
            return render(request, "auth/register.html")
        # first_name = ""
        # CustomUser.objects.create_user(first_name=first_name)
        user = CustomUser.objects.create_user(email=email, password=password)
        my_student_group = Group.objects.get_or_create(name="user")
        my_student_group[0].user_set.add(user)
        user.first_name = first_name
        user.last_name = last_name
        user.is_active = False
        
        if gender == "M":
            user.gender = gender
            user.profile_pic = "picture/luffy.jpg"
        elif gender == "F":
            user.gender = gender
            user.profile_pic = "picture/lupa.jpg"
        else:
            messages.error(request, "Eh pilih gender lu tolol")
            


        
        user.save()
        email_subject = "Active your account"
        current_site = get_current_site(request)

        email_body = {
            "user": user,
            "domain": current_site.domain,
            "uid": urlsafe_base64_encode(force_bytes(user.pk)),
            "token": account_activation_token.make_token(user),
        }
        link = reverse(
            "activate",
            kwargs={"uidb64": email_body["uid"], "token": email_body["token"]},
        )
        email_subject = "Active your account"
        active_url = "http://" + current_site.domain + link
        email = EmailMessage(
            email_subject,
            f"Hi {user.first_name} {user.last_name}"
            + ", Please the link below to activate your account \n"
            + active_url,
            "noreply@potato.com",
            [email],
        )
        EmailTreading(email).start()

        messages.success(request, "Account Successfully Created")

        return redirect("login")


# user = User.objects.create_user(email=email, password=password)
# user.set_password(password)
# user.save()
class VerificationView(View):
    def get(self, request, uidb64, token):
        try:
            id = force_text(urlsafe_base64_decode(uidb64))
            user = CustomUser.objects.get(pk=id)

            if not account_activation_token.check_token(user, token):
                return redirect("login" + "?message" + "User already Activated")

            if user.is_active:
                return redirect("login")

            user.is_active = True
            user.save()

            messages.success(request, "Account activate success")

            return redirect("login")
        except Exception as ex:
            print("Error " + str(ex))

        return redirect("register")

## lanjut lagi dibagian admin

class LoginView(View):
    def get(self, request):
        return render(request, "auth/login.html")

    def post(self, request):
        email = request.POST["email"]
        password = request.POST["password"]
 
        user = EmailBackend.authenticate(request, username=request.POST.get('email'), password=request.POST.get('password'))
        if user != None:
            auth.login(request,user)
            return redirect('news_list')


class LogoutView(View):
    def get(self, request):
        auth.logout(request)
        messages.success(request, "you have been logged out")
        return redirect("home")
