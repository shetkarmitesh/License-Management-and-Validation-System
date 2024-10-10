import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import base64
import io
import json
from collections import Counter
from venv import logger
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from CentralServerapp.models import License
import logging
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth
import csv
# Create your views here.
@login_required(login_url='/administrator/login')
def index(request):
    licenses = License.objects.all().order_by("createdAt")
    
    status_counts = Counter(license.status for license in licenses)
    labels = ['Approved', 'Pending', 'Failed']
    sizes = [
        status_counts.get('approved', 0),
        status_counts.get('pending', 0),
        status_counts.get('failed', 0)
    ]
    colors = ['#4CAF50', '#FF9800', '#F44336'] 
    # Create a pie chart
    plt.figure(figsize=(8, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90,colors=colors)
    plt.axis('equal')  # Equal aspect ratio ensures the pie chart is a circle.

    # Save the plot to a BytesIO object
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png',transparent=True)
    buffer.seek(0)
    img_str = base64.b64encode(buffer.read()).decode('utf-8')
    plt.close()  # Close the plot to free memory

    return render(request,'admin/index.html',{'LicenseDetails':licenses[:3], 'img_str': img_str})
def profile(request):
    profileDetails = User.objects.get(id=request.user.id)
    return render(request,'admin/profile.html',{'profileDetails':profileDetails})

def notifications(request):
    return render(request,'admin/index.html')

def requests(request):
    LicenseDetails = License.objects.all().order_by("createdAt")

    return render(request,'admin/requests.html',{'LicenseDetails':LicenseDetails})


def updatestatus(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            status = data.get('status')
            licenseKey = data.get('licenseKey')
            logger.info(f'Received status: {status}')  # Log the received status

            # Update status logic here
            if License.objects.filter(licenseKey=licenseKey).exists():
                lic = License.objects.get(licenseKey=licenseKey)
                lic.status = status
                lic.save()
            return JsonResponse({'message': 'Status updated successfully', 'status': status}, status=200)
        except Exception as e:
            logger.error(f'Error: {str(e)}')  # Log the error
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request'}, status=400)

def login(request):
    if request.method=="POST":
        # fetching the data from form
        username = request.POST['email-address']
        password = request.POST['password']
        
        user = auth.authenticate(username=username ,password=password,is_staff=True)
        if (user is not None ): 
            
            auth.login(request,user)
            return redirect('index')
        else:
        
            redirect('login')

    return render (request,'admin/index.html')
def logout(request):
    auth.logout(request)
    return render(request,'admin/login.html')


def signup(request):
    if request.method=="POST":
        # fetching the data from form
        first_name = request.POST['first-name']
        last_name = request.POST['last-name']
        email = request.POST['email-address']
        password1 = request.POST['password']
        password2= request.POST['passwordC']
        Staff = request.POST['role']
        if Staff.lower() == "staff":  # Convert to lower case for comparison
            Staff = True
        # adding the data to database
        if password1==password2:
            if User.objects.filter(email=email).exists():
                return redirect('signup')
           
            user = User.objects.create_user(username=email,password=password1,email=email,first_name=first_name,last_name=last_name,is_staff = Staff)
            user.save()
       
            return redirect('signup')
        else: 
            return redirect('signup')
         
    return render(request,'admin/signup.html')

def report(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="license_report.csv"'

    writer = csv.writer(response)
    writer.writerow(['License Key', 'Created Date','Expiration Date','Device Number','Status'])  # Header row

    # Fetch all licenses
    licenses = License.objects.all().values_list('licenseKey', 'createdAt', 'expirationDate','deviceNo','status') 
    for license in licenses:
        writer.writerow(license)

    return response