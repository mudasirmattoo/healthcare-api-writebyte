from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Doctor, Patient, PatientDoctorMapping

class RegisterSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    class Meta:
        model = User
        fields = ('username','email','password','first_name','last_name')
        extra_kwargs = {'password': {'write_only':True}}
        
    def create(self, validated_data):
        return User.objects.create_user(username=validated_data['username'],
                                   email=validated_data['email'],password=validated_data['password'], 
                                   first_name=validated_data['first_name'],last_name = validated_data['last_name'])
        
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('id', 'first_name', 'last_name', 'date_of_birth', 'address')
        read_only_fields = ('id',)
        
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ('id', 'first_name', 'last_name', 'speciality')
        read_only_fields = ('id',)

class PatientDoctorMappingSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only=True)
    doctor = DoctorSerializer(read_only=True)
    p_id = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all(),source='patient',write_only=True)
    d_id = serializers.PrimaryKeyRelatedField(queryset=Doctor.objects.all(),source='doctor',write_only=True)
    class Meta:
        model = PatientDoctorMapping
        fields = ('id', 'patient', 'doctor', 'p_id', 'd_id', 'assigned_at')
        read_only_fields = ('id','assigned_at')

    