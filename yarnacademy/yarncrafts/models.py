from django.db import models

# Create your models here.
class Contact(models.Model):
    # Create your models here.
    full_name = models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField()
    created_at= models.TimeField(auto_now=True)

    def __str__(self):
        return f"The name is{self.full_name}:{self.email}:{self.message}"
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    enrollment_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"