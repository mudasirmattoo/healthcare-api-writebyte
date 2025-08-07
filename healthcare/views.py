from django.shortcuts import render
from rest_framework import generics, permissions, status
from .models import Patient, Doctor, PatientDoctorMapping
from django.contrib.auth.models import User
from rest_framework.response import Response
from .serializers import PatientSerializer, PatientDoctorMappingSerializer, DoctorSerializer, RegisterSerializer
from .permissions import AdminOrReadOnly, OwnerOrReadOnly
from django.shortcuts import get_object_or_404


# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (permissions.AllowAny,)
    
class CreatePatientList(generics.ListCreateAPIView):
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Patient.objects.filter(user=self.request.user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
class CreateDoctorList(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated, AdminOrReadOnly]

        
class PatientDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated, OwnerOrReadOnly]
    
    def get_queryset(self):
        return Patient.objects.filter(user=self.request.user)
    
class DoctorDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated, AdminOrReadOnly]
    
    
class CreateMappingList(generics.ListCreateAPIView):
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return PatientDoctorMapping.objects.filter(patient__user=self.request.user)
    
    def create(self,request,*args,**kwargs):
        patient_queryset = Patient.objects.filter(user=request.user)
        serializer = self.get_serializer(
            data=request.data,
            context={'patient_queryset': patient_queryset}
        )
        serializer.fields['patient_id'].queryset = patient_queryset

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class MappingDetailView(generics.RetrieveDestroyAPIView):
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [permissions.IsAuthenticated, OwnerOrReadOnly]

    def get_queryset(self):
        return PatientDoctorMapping.objects.filter(patient__user=self.request.user)

class PatientDoctorsListView(generics.ListAPIView):
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        patient_id = self.kwargs['patient_id']
        patient = get_object_or_404(Patient, id=patient_id, user=self.request.user)
        doctor_ids = PatientDoctorMapping.objects.filter(patient=patient).values_list('doctor_id', flat=True)
        return Doctor.objects.filter(id__in=doctor_ids)