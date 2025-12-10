from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from .models import Contact
from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponseForbidden
from .models import MediaFile
from .forms import MediaForm



# Create your views here.
def home(request):
    return render(request, "home.html")
def index(request):
    return render(request, "index.html")
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
    return render(request, 'login.html',    {'form':form})
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



@login_required
def media_list(request):
    files = MediaFile.objects.filter(owner=request.user).order_by('-uploaded_at')
    return render(request, 'media_list.html', {'files': files})

@login_required
def media_add(request):
    if request.method == 'POST':
        form = MediaForm(request.POST, request.FILES)
        if form.is_valid():
            media = form.save(commit=False)
            media.owner = request.user
            media.save()
            return redirect('media_list')
    else:
        form = MediaForm()
    return render(request, 'media_form.html', {'form': form, 'action': 'Add'})

@login_required
def media_edit(request, pk):
    media = get_object_or_404(MediaFile, pk=pk)
    if media.owner != request.user:
        return HttpResponseForbidden("You cannot edit this file.")
    if request.method == 'POST':
        form = MediaForm(request.POST, request.FILES, instance=media)
        if form.is_valid():
            form.save()
            return redirect('media_list')
    else:
        form = MediaForm(instance=media)
    return render(request, 'media_form.html', {'form': form, 'action': 'Edit'})

@login_required
def media_delete(request, pk):
    media = get_object_or_404(MediaFile, pk=pk)
    if media.owner != request.user:
        return HttpResponseForbidden("You cannot delete this file.")
    if request.method == 'POST':
        media.delete()
        return redirect('media_list')
    return render(request, 'media_confirm_delete.html', {'media': media})



from django.contrib.auth.decorators import login_required
from .models import Course, Enrollment

@login_required
def profile(request):
    courses = Course.objects.all()
    enrolled_courses = Enrollment.objects.filter(user=request.user)
    return render(request, 'profile.html', {
        'user': request.user,
        'courses': courses,
        'enrolled_courses': enrolled_courses
    })


@login_required
def enroll_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    Enrollment.objects.get_or_create(user=request.user, course=course)
    return redirect('profile')
