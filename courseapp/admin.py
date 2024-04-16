from django.contrib import admin
from .models import Lesson, Badge, Quiz, LessonContent

# Register your models here.
admin.site.register(Lesson)
admin.site.register(Badge)
admin.site.register(Quiz)
admin.site.register(LessonContent)
