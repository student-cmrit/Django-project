from django.contrib import admin
from django.urls import path,include

from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(
        template_name='loginpage.html',
        redirect_authenticated_user=True,
        next_page='home'  # Replace '/home/' with your desired redirect URL
    ), name='login'),
    
    path('',views.homepage,name='home'),
    
     path('logout/', auth_views.LogoutView.as_view(), name='logout'),
     
     path('register/', views.register, name='register'),  # Registration URL
      path('create_employee/', views.create_employee, name='create_employee'),
    path('employee_list/', views.employee_list, name='employee_list'),
    path('edit_employee/',views.edit_employee,name='edit_employee'),
     path('employee/edit/<int:id>/', views.edit_employee, name='edit_employee'),
    path('employee/delete/<int:id>/', views.delete_employee, name='delete_employee'),
]



from django.conf.urls.static import static
from django.conf import settings
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)