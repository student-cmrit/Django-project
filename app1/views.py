

# Create your views here.


from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required

@login_required
def homepage(request):
    return render(request, 'homepage.html')



from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created! You can now log in.')
            return redirect('login')  # Redirect to login page
    else:
        form = UserCreationForm()
    return render(request, 'registerpage.html', {'form': form})

from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee

def create_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)  # Handling form data and file upload
        if form.is_valid():
            form.save()  # Save the employee to the database
            return redirect('employee_list')  # Redirect to the employee list page after saving
    else:
        form = EmployeeForm()

    return render(request, 'create_employee.html', {'form': form})


# views.py

def employee_list(request):
    employees = Employee.objects.all()  # Fetch all employees from the database
    return render(request, 'employee_list.html', {'employees': employees})


def edit_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee details updated successfully.')
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    
    return render(request, 'edit_employee.html', {'form': form, 'employee': employee})

def delete_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        employee.delete()
        messages.success(request, 'Employee deleted successfully.')
        return redirect('employee_list')
    return render(request, 'delete_employee_confirm.html', {'employee': employee})

def update_employee(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    if request.method == 'POST':
        # Update employee logic
        messages.success(request, "Employee updated successfully!")
        return redirect('employee_list')
