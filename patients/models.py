from datetime import date
from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
import os

from doctors.models import Doctor

# Create your models here.

class Patient(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    birthday = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=True, blank=True)

    class Meta:
        db_table = 'patient'
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):  # create auto slug
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('patients:patient_detail', kwargs={'slug': self.slug})

    def get_age(self):
        if self.birthday:
            today = date.today()
            age = today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))
            return age

def get_upload_to(instance, filename):
    return os.path.join(
        "user_%d" % instance.patient.id, filename)
def get_upload_path(instance, filename):
    print(instance, filename)
    # return os.path.join(
    #   "user_%d" % instance.patient.id, "car_%s" % instance.slug, filename)

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    date = models.DateField()
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField(null=True, blank=True)
    documents = models.FileField(upload_to= get_upload_to, blank=True)
    status = models.CharField(max_length=20, choices=(('pending', 'Pending'), ('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')), default='pending')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')


    class Meta:
        db_table = 'appointment'
        verbose_name = 'Appointment'
        verbose_name_plural = 'Appointments'



        # return '%p/documents' % (instance.patient)

    def __str__(self):
        return self.patient.name + ' - ' + self.date.strftime('%m/%d/%Y') + ' - ' + self.time.strftime('%I:%M %p')
    
    def get_absolute_url(self):
        return reverse('appointment-detail', kwargs={'pk': self.pk})

    
class Treatment(models.Model):
        name = models.CharField(max_length=100)
        description = models.TextField(null=True, blank=True)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
        slug = models.SlugField(null=True, blank=True)
        patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='treatments')

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