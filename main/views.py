from rest_framework import generics
from .models import ClassSchedule, ClassAttendance, Query, QueryComment
from .serializers import ClassScheduleSerializer, ClassAttendanceSerializer, QuerySerializer, QueryCommentSerializer


class ClassScheduleList(generics.ListCreateAPIView):
    queryset = ClassSchedule.objects.all()
    serializer_class = ClassScheduleSerializer


class ClassScheduleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClassSchedule.objects.all()
    serializer_class = ClassScheduleSerializer


class ClassAttendanceList(generics.ListCreateAPIView):
    queryset = ClassAttendance.objects.all()
    serializer_class = ClassAttendanceSerializer


class ClassAttendanceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClassAttendance.objects.all()
    serializer_class = ClassAttendanceSerializer


class QueryList(generics.ListCreateAPIView):
    queryset = Query.objects.all()
    serializer_class = QuerySerializer


class QueryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Query.objects.all()
    serializer_class = QuerySerializer


class QueryCommentList(generics.ListCreateAPIView):
    queryset = QueryComment.objects.all()
    serializer_class = QueryCommentSerializer


class QueryCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = QueryComment.objects.all()
    serializer_class = QueryCommentSerializer
