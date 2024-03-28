from django.contrib import admin

from materials.models import Course, Lesson


@admin.register(Course)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'description',)
    search_fields = ('title',)


@admin.register(Lesson)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'description', 'course',)
    list_filter = ('course',)
    search_fields = ('title', 'course',)
