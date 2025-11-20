from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),

    # Department CRUD
    path('departments/', views.department_list, name='department_list'),
    path('departments/add/', views.department_add, name='department_add'),
    path('departments/edit/<int:id>/', views.department_edit, name='department_edit'),
    path('departments/delete/<int:id>/', views.department_delete, name='department_delete'),

    # HOD CRUD
    path('hods/', views.hod_list, name='hod_list'),
    path('hods/add/', views.hod_add, name='hod_add'),
    path('hods/edit/<int:id>/', views.hod_edit, name='hod_edit'),
    path('hods/delete/<int:id>/', views.hod_delete, name='hod_delete'),

    # Student CRUD
    path('students/', views.student_list, name='student_list'),
    path('students/add/', views.student_add, name='student_add'),
    path('students/edit/<int:id>/', views.student_edit, name='student_edit'),
    path('students/delete/<int:id>/', views.student_delete, name='student_delete'),

    # Authentication URLs
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),

]
