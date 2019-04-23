from django.contrib.auth.models import User
from rest_framework import serializers

from innovationApp.models import Student, Coach, Project


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email','is_staff')

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.StringRelatedField(many=False, read_only=True)
    project_owner = serializers.StringRelatedField(many=False, read_only=True, allow_null=True)
    class Meta:
        model = Student
        fields = ('user','project_owner')

class CoachSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.StringRelatedField(many=False, read_only=True)
    class Meta:
        model = Coach
        fields = ('user')

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    createur = serializers.StringRelatedField(many=False, read_only=True)
    superviseur = serializers.StringRelatedField(many=False, read_only=True)
    membres = StudentSerializer(many=True, read_only=True, allow_null=True)
    class Meta:
        model = Project
        fields = ('createur','superviseur','membres')
