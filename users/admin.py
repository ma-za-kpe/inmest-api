from django.contrib import admin
from .models import IMUser
from .models import Cohort
from .models import CohortMember
admin.site.register(IMUser)
admin.site.register(Cohort)
admin.site.register(CohortMember)

