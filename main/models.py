from django.db import models
from users.models import Cohort
from django.contrib.auth.models import User


class ClassSchedule(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date_and_time = models.DateTimeField()
    end_date_and_time = models.DateTimeField()
    is_repeated = models.BooleanField(default=False)
    repeat_frequency = models.CharField(max_length=50, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE)
    venue = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ClassAttendance(models.Model):
    class_schedule = models.ForeignKey(ClassSchedule, on_delete=models.CASCADE)
    attendee = models.ForeignKey(User, on_delete=models.CASCADE)
    is_present = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='attendance_created_by')


class Query(models.Model):
    resolution_choices = [
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('DECLINED', 'Declined'),
        ('RESOLVED', 'Resolved')
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='submitted_queries')
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_queries', blank=True, null=True)
    resolution_status = models.CharField(max_length=20, choices=resolution_choices, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='query_created_by')


class QueryComment(models.Model):
    query = models.ForeignKey(Query, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='query_comments')
