from .import views
from django.urls import path

urlpatterns=[
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('index/',views.index,name='index'),
    path('courses/',views.courses,name='courses'),
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='login'),
    path('profile/',views.profile,name='profile'),


    path('enroll/<int:course_id>/', views.enroll_course, name='enroll_course'),

    path('logout/',views.logout_user,name='logout'),
    path('media/', views.media_list, name='media_list'),
    path('media/add/', views.media_add, name='media_add'),
    path('media/<int:pk>/edit/', views.media_edit, name='media_edit'),
    path('media/<int:pk>/delete/', views.media_delete, name='media_delete'),
]

