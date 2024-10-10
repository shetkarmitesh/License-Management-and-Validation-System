from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class License(models.Model):
    STATUS_CHOICES = [
        ('approved', 'Approved'),
        ('pending', 'Pending'),
        ('failed', 'Failed'),
    ]
    licenseKey = models.CharField(max_length=255)
    isActive = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    createdAt = models.DateField(auto_now_add=True)
    updatedAt = models.DateField(auto_now=True)
    expirationDate = models.DateField()
    deviceNo = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')  


    def name (self):
        return self.user.first_name+" "+self.user.last_name
    def email(self):
        return self.user.email
# class Administrative (models.Model):
