from rest_framework import serializers
from .models import IMUser, Cohort, CohortMember
from django.contrib.auth.models import User


class UserTypeSerializer(serializers.Serializer):
    value = serializers.CharField(max_length=20)
    display = serializers.CharField(max_length=20)


class IMUserSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = IMUser
        fields = '__all__'


class CohortSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Cohort
        fields = '__all__'


class CohortMemberSerializer(serializers.ModelSerializer):
    cohort = serializers.PrimaryKeyRelatedField(queryset=Cohort.objects.all())
    member = serializers.PrimaryKeyRelatedField(queryset=IMUser.objects.all())

    class Meta:
        model = CohortMember
        fields = '__all__'
