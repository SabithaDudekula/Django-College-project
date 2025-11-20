from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Department, Hod, Student


@login_required
def home_page(request):
    return render(request, "mainapp/home.html")



from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages


def register_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Check if username taken
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("register")

        # Create new user
        User.objects.create_user(username=username, password=password)
        messages.success(request, "Account created successfully. Please login.")
        return redirect("login")

    return render(request, "mainapp/register.html")

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password")
            return redirect("login")

    return render(request, "mainapp/login.html")

def logout_user(request):
    logout(request)
    return redirect("login")


# ---------------- DEPARTMENT CRUD ---------------- #

@login_required
def department_list(request):
    departments = Department.objects.all()
    return render(request, "mainapp/departments_list.html", {"departments": departments})


@login_required
def department_add(request):
    if request.method == "POST":
        name = request.POST.get("name")
        code = request.POST.get("code")
        Department.objects.create(name=name, code=code)
        return redirect("department_list")

    return render(request, "mainapp/departments_add.html")


@login_required
def department_edit(request, id):
    department = Department.objects.get(id=id)

    if request.method == "POST":
        department.name = request.POST.get("name")
        department.code = request.POST.get("code")
        department.save()
        return redirect("department_list")

    return render(request, "mainapp/departments_edit.html", {"department": department})


@login_required
def department_delete(request, id):
    dept = Department.objects.get(id=id)
    dept.delete()
    return redirect("department_list")

# ---------------- HOD CRUD ---------------- #


@login_required
def hod_list(request):
    hods = Hod.objects.select_related('department').all()
    return render(request, "mainapp/hod_list.html", {"hods": hods})


@login_required
def hod_add(request):
    departments = Department.objects.all()

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        department_id = request.POST.get("department")

        Hod.objects.create(
            name=name,
            email=email,
            department_id=department_id
        )
        return redirect("hod_list")

    return render(request, "mainapp/hod_add.html", {"departments": departments})


@login_required
def hod_edit(request, id):
    hod = Hod.objects.get(id=id)
    departments = Department.objects.all()

    if request.method == "POST":
        hod.name = request.POST.get("name")
        hod.email = request.POST.get("email")
        hod.department_id = request.POST.get("department")
        hod.save()
        return redirect("hod_list")

    return render(request, "mainapp/hod_edit.html", {"hod": hod, "departments": departments})


@login_required
def hod_delete(request, id):
    hod = Hod.objects.get(id=id)
    hod.delete()
    return redirect("hod_list")


# ---------------- STUDENT CRUD ---------------- #



@login_required
def student_list(request):
    students = Student.objects.select_related('department').all()
    return render(request, "mainapp/student_list.html", {"students": students})

@login_required
def student_add(request):
    departments = Department.objects.all()

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        department_id = request.POST.get("department")

        Student.objects.create(
            name=name,
            email=email,
            department_id=department_id
        )
        return redirect("student_list")

    return render(request, "mainapp/student_add.html", {"departments": departments})

@login_required
def student_edit(request, id):
    student = Student.objects.get(id=id)
    departments = Department.objects.all()

    if request.method == "POST":
        student.name = request.POST.get("name")
        student.email = request.POST.get("email")
        student.department_id = request.POST.get("department")
        student.save()
        return redirect("student_list")

    return render(request, "mainapp/student_edit.html", {"student": student, "departments": departments})

@login_required
def student_delete(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect("student_list")
