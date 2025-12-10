from django.db import models
from django.contrib.auth import get_user_model



# Create your models here.
class Contact(models.Model):
    # Create your models here.
    full_name = models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField()
    created_at= models.TimeField(auto_now=True)

    def __str__(self):
        return f"The name is{self.full_name}:{self.email}:{self.message}"




User = get_user_model()

class MediaFile(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads/')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='media_files')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    duration = models.CharField(max_length=100, blank=True)  # e.g. "6 weeks"
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return self.title


class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'course')

    def __str__(self):
        return f"{self.user.username} → {self.course.title}"
