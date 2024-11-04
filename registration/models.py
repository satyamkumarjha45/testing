from django.db import models

class Registration(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    slap = models.CharField(max_length=10)  # Assuming this is a field you need
    
    def __str__(self):
        return self.name

