from django.db import models
from .views import database

# Create your models here.
class Tag(models.Model):
    uid = models.CharField(max_length=70, unique=True)

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        database.child("Tags").child(self.uid).remove()
    
    def __str__(self):
        return f"{self.id} - {self.uid}"

class Product(models.Model):
    block_type = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.block_type} - {self.id} - ${self.price}"