from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from CentralServerapp.models import License
import uuid
from django.contrib.auth.decorators import login_required
from CentralServerapp.views import createLicense,validateLicense
from datetime import datetime,timedelta
import sweetify
# Create your views here.
def signup(request):
    if request.method=="POST":
        # fetching the data from form
        first_name = request.POST['first-name']
        last_name = request.POST['last-name']
        email = request.POST['email-address']
        password1 = request.POST['password']
        password2= request.POST['passwordC']
        createDate = request.POST['createDate']
        deviceNo = request.POST['deviceNo']

        # adding the data to database
        if password1==password2:
            if User.objects.filter(email=email).exists():
                return redirect('signup')
           
            user = User.objects.create_user(username=email,password=password1,email=email,first_name=first_name,last_name=last_name)
            user.save()
            createLicense(user,createDate,deviceNo)
            sweetify.success(request, 'Account Will create Shortly', timer=2000)

            return redirect('signup')
        else: 
            return redirect('signup')
         
    return render(request,'signup.html')

def login(request):
    if request.method=="POST":
        # fetching the data from form
        username = request.POST['email-address']
        password = request.POST['password']
        deviceNo = request.POST['deviceNo']
        
        user = auth.authenticate(username=username ,password=password)
        # licenseDetails = License.objects.get(user_id = request.id)
        if (user is not None and validateLicense(user,deviceNo)): 
            
            auth.login(request,user)
            return redirect('display')
        else:
            # messages.info(request,"invalid credentails")
            print("errrrrrrrrrrrrrrorrrrrrrrrrr")
            redirect('login')
    return render (request,'login.html')
@login_required
def display(request):
    # userDetails = User.objects.get(id = request.user.id)
    licenseDetails = License.objects.get(user_id= request.user.id )
    print(licenseDetails.id,licenseDetails.email)
    return render(request,'details.html',{'licenseDetails':licenseDetails})
    
def logout(request):
    auth.logout(request)
    return render(request,'signup.html')
