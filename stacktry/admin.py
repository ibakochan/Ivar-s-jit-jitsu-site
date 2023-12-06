from django.contrib import admin
from stacktry.models import Click, Lesson, ParticipationCount

admin.site.register([Click, Lesson, ParticipationCount])
