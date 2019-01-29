from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils import timezone
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify


# Create your models here.
class Tenants(models.Model):

    GENDER_CHOICE = {
        ('male', 'Male'), ('female', 'Female') ,('others', 'Others')
    }
    name=models.CharField(max_length=100)
    age=models.IntegerField(blank='true')
    gender = models.CharField(max_length=20, choices=GENDER_CHOICE, default='male')
    slug = models.SlugField(max_length=60)
    mobileno_1=models.CharField(max_length=10)
    mobileno_2=models.CharField(max_length=10)
    mobileno_3=models.CharField(max_length=10)
    address = models.TextField(max_length=200)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    created_on=models.DateTimeField(default=timezone.now)
    location = models.CharField(max_length=100)
    body=models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', args=[self.id, self.slug])


@receiver(pre_save,sender=Tenants)
def pre_save_slug(sender,**kwargs):
    slug = slugify(kwargs['instance'].name)
    kwargs['instance'].slug = slug

