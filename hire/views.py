from django.shortcuts import render,redirect

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from hire.models import AppliedUserData
# Create your views here.
def open_Hire_me(request):
    return render(request,'hireme.html')


@login_required
def hire_me(request):
    if request.method == "POST":
        data_Firstname = request.POST['Firstname']
        data_Lastname = request.POST['Lastname']
        data_job_role = request.POST['job_role']
        data_phonenumber = request.POST['phonenumber']
        data_address = request.POST['address']
        front_image = request.FILES['my_image']
        my_user = request.user

        print(data_Firstname, data_Lastname, data_job_role, data_phonenumber, data_address, front_image, my_user)

        AppliedUserData.objects.create(Firstname=data_Firstname, Lastname=data_Lastname, job_role=data_job_role, phonenumber=data_phonenumber, address=data_address, my_image=front_image, user=my_user)

        messages.info(request, f"{data_Firstname} detail has been recorded")

    return render(request, "hireme.html")
#men products
def open_my_details(request):
  my_user= request.user
  mydetail_list =AppliedUserData.objects.filter(user= my_user)
  data = {
        'mydetails_list_show': mydetail_list
    }
  print(data)
  return render(request, "detail.html", data)

def open_Hire_me(request):
    return render(request,'hireme.html')






@login_required
def delete_data_method(request,id):
    
    obj = AppliedUserData.objects.get(id=id) 
    obj.delete()
    messages.info(request,f"Data has been deleted...")
    Data_list = AppliedUserData.objects.all()
    data = {
        'product_list_show':Data_list
    }
    
    return render(request,"detail.html",data)
@login_required
def update_data_method(request, id):
    try:
        obj = AppliedUserData.objects.get(id=id)
        
        if request.method == "POST":
            obj.Firstname = request.POST['Firstname']
            obj.Lastname = request.POST['Lastname']
            obj.job_role = request.POST['job_role']
            obj.phonenumber = request.POST['phonenumber']
            obj.address = request.POST['address']
            
            
            if 'my_image' in request.FILES:
                obj.my_image = request.FILES['my_image']
            
            obj.save()
            messages.info(request, f"Your data has been updated.")
            
        
        data = {
            'my_detail': obj
        }
        return render(request, 'update_form.html', data)  
    except AppliedUserData.DoesNotExist:
        messages.error(request, f"The requested data does not exist.")
        return redirect('update_form.html') 


