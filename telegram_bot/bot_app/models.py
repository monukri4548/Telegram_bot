from django.db import models

class User(models.Model):
    telegram_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    subscribed = models.BooleanField(default=False)

class BotSettings(models.Model):
    name = models.CharField(max_length=50)
    token = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)