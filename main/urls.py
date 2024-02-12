from django.urls import path
from .views import (
    ClassScheduleList, ClassScheduleDetail,
    ClassAttendanceList, ClassAttendanceDetail,
    QueryList, QueryDetail,
    QueryCommentList, QueryCommentDetail
)

urlpatterns = [
    path('class-schedules/', ClassScheduleList.as_view(), name='class-schedule-list'),
    path('class-schedules/<int:pk>/', ClassScheduleDetail.as_view(), name='class-schedule-detail'),
    path('class-attendance/', ClassAttendanceList.as_view(), name='class-attendance-list'),
    path('class-attendance/<int:pk>/', ClassAttendanceDetail.as_view(), name='class-attendance-detail'),
    path('queries/', QueryList.as_view(), name='query-list'),
    path('queries/<int:pk>/', QueryDetail.as_view(), name='query-detail'),
    path('query-comments/', QueryCommentList.as_view(), name='query-comment-list'),
    path('query-comments/<int:pk>/', QueryCommentDetail.as_view(), name='query-comment-detail'),
]
