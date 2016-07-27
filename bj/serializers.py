from rest_framework import serializers
from .models import Job_english,Company,Role,Job_hinglish,Job_hindi

class Job_englishSerializer(serializers.ModelSerializer):
	class Meta:
		model = Job_english
		fields='__all__'

class Job_hindiSerializer(serializers.ModelSerializer):
	class Meta:
		model = Job_hindi
		fields='__all__'

class Job_hinglishSerializer(serializers.ModelSerializer):
	class Meta:
		model = Job_hinglish
		fields='__all__'

class CompanySerializer(serializers.ModelSerializer):
	class Meta:
		model=Company
		fields='__all__'

class RoleSerializer(serializers.ModelSerializer):
	class Meta:
		model=Role
		fields='__all__'
