from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect,render,get_object_or_404
from .forms import RegisterForm, StudentForm
from .models import Contact
from .models import Student


# Create your views here.
def home(request):
    return render(request, "home.html")
def about(request):
    return render(request,"about.html")
def courses(request):
    return render(request, "courses.html")
def register(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=RegisterForm()


    return render(request, "register.html", {"form":form})
def user_login(request):
    if request.method=="POST":
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('profile')
        else:
         form=AuthenticationForm()
    return render(request, "login.html", {"form":form})
def contact(request):
    if request.method=="POST":
        full_name=request.POST.get("full_name")
        email=request.POST.get("email")
        message=request.POST.get("message")

        Contact.objects.create(full_name=full_name,email=email,message=message)



    return render(request, "contact.html")
@login_required
def profile(request):
    return render(request, "profile.html")
def logout_user(request):
    logout(request)
    return redirect('home')



def students(request):
    student= Student.objects.all()
    return render(request, "students.html", {"students":students})
def students_details(request,id):
    student= get_object_or_404(Student,id=id)
    return render(request, "students_details.html", {"student":student})

def student_create(request):
    if request.method == "POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students_details',id)
        else:
         form=StudentForm()
         return render(request, "student_form.html", {"form":form})
def student_update(request,id):
    student = get_object_or_404(Student,id=id)



    if request.method == "POST":
        form=StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('students',id)
        else:
            form=StudentForm(instance=student)
            return render(request, "students/student_form.html", {"form":form})


def student_delete(request,id):
    student = get_object_or_404(Student,id=id)
    if request.method == "POST":
        student.delete()
        return redirect('students')
    return render(request, "students/student_delete.html", {"student":student})