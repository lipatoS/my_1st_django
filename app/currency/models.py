from django.db import models


class Registrator(models.Model):
    login = models.CharField(max_length=16)
    passwords = models.CharField(max_length=20)
    mails = models.CharField(max_length=20)


