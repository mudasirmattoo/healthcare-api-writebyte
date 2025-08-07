from django.urls import path
from .views import RegisterView, PatientDetails, CreateDoctorList,CreateMappingList,CreatePatientList, DoctorDetails,MappingDetailView, PatientDoctorsListView

urlpatterns = [
    path('auth/register/',RegisterView.as_view(), name='register'),
    path('patients/',CreatePatientList.as_view(), name="create-patients"),
    path('patients/<int:pk>/',PatientDetails.as_view(), name="patient-details"),
    
    path('doctors/',CreateDoctorList.as_view(), name="create-doctors"),
    path('doctors/<int:pk>/',DoctorDetails.as_view(), name="doctor-details"),
    
    path('mappings/',CreateMappingList.as_view(),name='create-mapping'),
    path('mappings/<int:pk>/',MappingDetailView.as_view(),name='mapping-details'),
    
    #all docs for a patient
    path('patients/<int:patient_id>/doctors/', PatientDoctorsListView.as_view(), name='patient-doctors-list'),
]
