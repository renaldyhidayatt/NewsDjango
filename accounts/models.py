import os
from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth.hashers import make_password
from django.dispatch import receiver
from django.db import models

# Create your models here.


class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = CustomUser(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        assert extra_fields["is_staff"]
        assert extra_fields["is_superuser"]
        return self._create_user(email, password, **extra_fields)


def path_to_images(instance, filename):
    return os.path.join("picture", str(instance), filename)


class CustomUser(AbstractUser):
    GENDER = [("M", "Male"), ("F", "Female")]
    ROLE_PERMISSION = [("A", "Admin"), ("M", "Manager"), ("J", "Jurnalis")]
    username = None
    email = models.EmailField(unique=True)
    user_type = models.CharField(default=1, choices=ROLE_PERMISSION, max_length=1)
    gender = models.CharField(max_length=1, choices=GENDER)
    profile_pic = models.ImageField(
        upload_to=path_to_images, null=True, default="picture/luffy.jpg"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email
        # return self.first_name + "" + self.last_name

    @property
    def image_url(self):
        if self.profile_pic:
            return self.profile_pic.url
        return "#"
