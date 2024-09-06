from django.shortcuts import render,redirect,get_object_or_404
from .forms import StudentRegistration
from .models import UserProfile
import logging
logger = logging.getLogger(__name__)
# Create your views here.
def add_show(request):
    if request.method =='POST': #to post data
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            fm = StudentRegistration()
    else:        
      fm = StudentRegistration() #to get data get method
    stud=UserProfile.objects.all()
    return render(request,'studentinfo/addandshow.html',{'form':fm,'stu':stud})

def update_data(request,id):
    student= get_object_or_404(UserProfile,pk=id)
    logger.debug(f"id is {id},student object:{student.name},{student.email}")
    
    
    
    if request.method=='POST':
        
        form = StudentRegistration(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('/studentinfo')
    else:
        
        form = StudentRegistration(instance=student)
        logger.debug(f"Form initialized with: {form.instance.name}, {form.instance.email}")
    return render(request,'studentinfo/update.html',{'form':form})

def delete_data(request,id):
    if request.method=='POST':
         del1 = UserProfile.objects.get(pk=id)
         del1.delete()
    return redirect('/studentinfo')
       