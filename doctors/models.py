from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

# Create your models here.

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=True, blank=True)

    class Meta:
        db_table = 'doctor'
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):  # create auto slug
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('doctors:doctor_detail', kwargs={'slug': self.slug})

    class Treatment(models.Model):
        name = models.CharField(max_length=100)
        description = models.TextField(null=True, blank=True)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
        slug = models.SlugField(null=True, blank=True)

        class Meta:
            db_table = 'treatment'
            verbose_name = 'Treatment'
            verbose_name_plural = 'Treatments'
        
        def __str__(self):
            return self.name

        def save(self, *args, **kwargs):  # create auto slug
            if not self.slug:
                self.slug = slugify(self.name)
            return super().save(*args, **kwargs)