from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class IMUser(models.Model):
    class UserType(models.TextChoices):
        EIT = 'EIT', 'EIT'
        TEACHING_FELLOW = 'TEACHING_FELLOW', 'Teaching Fellow'
        ADMIN_STAFF = 'ADMIN_STAFF', 'Admin Staff'
        ADMIN = 'ADMIN', 'Admin'

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    user_type = models.CharField(max_length=20, choices=UserType.choices, default=UserType.EIT)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.first_name


class Cohort(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    year = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class CohortMember(models.Model):
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE, related_name='members')
    member = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='cohort_memberships')
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cohort
