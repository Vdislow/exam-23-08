from django.contrib import admin
from .models import *


@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
    list_display = ('name', 'main_work', 'phone_number',)
    search_fields = ('name',)

    @admin.display(description='level')
    def get_level(self, obj):
        if obj.experience.year >= 3:
            return 'middle'
        if obj.experience.year < 3:
            return 'strong junior'


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_filter = ('language', 'mentor', )
    list_display = ('name', 'date_started', 'students', 'mentor', 'language')
    search_fields = ('student__name', 'mentor__name')

