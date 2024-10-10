from datetime import datetime, timedelta
import uuid
from django.http import HttpResponse
from django.shortcuts import render
from .models import License
# Create your views here.
def createLicense(user,createDate,deviceNo):
    
    licenseKey = uuid.uuid4()
    createdAt = createDate
    expirationDate = datetime.strptime(createDate, "%Y-%m-%d") + timedelta(days=365)
    deviceNo =deviceNo
    License.objects.create(licenseKey=licenseKey,user = user,createdAt=createdAt,expirationDate=expirationDate,isActive=False,deviceNo=deviceNo)


def validateLicense(user,deviceNo):

    
    if License.objects.filter(user =user,deviceNo=deviceNo,isActive=True,status = "approved").exists():
        return True
    else:
        False