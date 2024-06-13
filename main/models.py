from django.db import models
import uuid

# Create your models here.

class Contacto(models.Model):
    customer_name = models.CharField(max_length=64)
    customer_email = models.EmailField(max_length=64)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.customer_name} - {self.customer_email}'
