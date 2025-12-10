from django.contrib import admin

from .models import Contact

# Register your models here.
admin.site.register(Contact)
from django.contrib import admin
from .models import MediaFile

@admin.register(MediaFile)
class MediaFileAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'uploaded_at')   # columns in admin list view
    search_fields = ('title', 'owner__username')       # search bar
    list_filter = ('uploaded_at',)                     # filter sidebar
from django.contrib import admin
from .models import Course, Enrollment

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'duration', 'price')
    search_fields = ('title',)

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'enrolled_at')
    list_filter = ('course', 'enrolled_at')
