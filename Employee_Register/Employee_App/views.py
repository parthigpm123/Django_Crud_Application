from django.shortcuts import render

# Create your views here.

def employee_list(request):
      return render(request,'Employee_App/employee_list.html') 
      
def employee_form(request):
      return render(request,'Employee_App/employee_form.html')
      
      
def employee_delete(request): 
      return     