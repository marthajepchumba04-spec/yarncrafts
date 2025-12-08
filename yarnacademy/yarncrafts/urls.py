from .import views
from django.urls import path

urlpatterns=[
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('courses/',views.courses,name='courses'),
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='login'),
    path('profile/',views.profile,name='profile'),
    path('student/',views.students,name='student'),
    path('<int:id>/',views.students_details,name='students_details'),
    path('create/',views.student_create,name='student_create'),
    path('<int:id>/edit/',views.student_update,name='student_update'),
    path('<int:id>/delete/',views.student_delete,name='student_delete'),
]