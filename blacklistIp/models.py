from django.db import models

# Create your models here.


class BlackList(models.Model):
    ip = models.CharField(max_length=15)
    date = models.CharField(max_length=12, default="-")
    # date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ip
