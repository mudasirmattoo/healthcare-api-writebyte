from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patients')
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    address = models.TextField()
    
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Doctor(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    speciality = models.CharField(max_length=200)
    
    
    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name} - Speciality: {self.speciality}"
    

class PatientDoctorMapping(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    assigned_time = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('patient', 'doctor')
        
    def __str__(self):
        return f"{self.patient} ----> {self.doctor}"
    