from rest_framework import generics
from .models import IMUser, Cohort, CohortMember
from .serializers import IMUserSerializer, CohortSerializer, CohortMemberSerializer


class IMUserList(generics.ListCreateAPIView):
    queryset = IMUser.objects.all()
    serializer_class = IMUserSerializer


class IMUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = IMUser.objects.all()
    serializer_class = IMUserSerializer


class CohortList(generics.ListCreateAPIView):
    queryset = Cohort.objects.all()
    serializer_class = CohortSerializer


class CohortDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cohort.objects.all()
    serializer_class = CohortSerializer


class CohortMemberList(generics.ListCreateAPIView):
    queryset = CohortMember.objects.all()
    serializer_class = CohortMemberSerializer


class CohortMemberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CohortMember.objects.all()
    serializer_class = CohortMemberSerializer
