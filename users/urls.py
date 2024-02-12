from django.urls import path
from .views import (
    IMUserList, IMUserDetail,
    CohortList, CohortDetail,
    CohortMemberList, CohortMemberDetail
)

urlpatterns = [
    path('im-users/', IMUserList.as_view(), name='imuser-list'),
    path('im-users/<int:pk>/', IMUserDetail.as_view(), name='imuser-detail'),
    path('cohorts/', CohortList.as_view(), name='cohort-list'),
    path('cohorts/<int:pk>/', CohortDetail.as_view(), name='cohort-detail'),
    path('cohort-members/', CohortMemberList.as_view(), name='cohortmember-list'),
    path('cohort-members/<int:pk>/', CohortMemberDetail.as_view(), name='cohortmember-detail'),
]
