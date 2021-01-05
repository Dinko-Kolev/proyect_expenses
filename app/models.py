from django.db import models

# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    budget = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.first_name
    
    class Meta:
       
        managed = True
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'


class Expense(models.Model):
    title = models.CharField(max_length=50)
    image_url = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField(default=0.00)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['id']   
        managed = True
        verbose_name = 'Expense'
        verbose_name_plural = 'Expenses'