from rest_framework import serializers
from .models import ClassSchedule, ClassAttendance, Query, QueryComment


class ClassScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassSchedule
        fields = '__all__'


class ClassAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassAttendance
        fields = '__all__'


class QuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Query
        fields = '__all__'


class QueryCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = QueryComment
        fields = '__all__'
