from django.urls import path, include

from . import views



urlpatterns = [
    path('', views.employee_form,name='employee_insert'), # for inserting a new employee record
    path('<int:id>/', views.employee_form,name='employee_update'),# for updating an existing employee record
    path('delete/<int:id>/', views.employee_delete,name='employee_delete'),
    path('list/', views.employee_list,name='employee_list')# for showing the list of employees
]
