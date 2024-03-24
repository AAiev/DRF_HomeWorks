from django.contrib import admin

from users.models import User, Payment


@admin.register(User)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'first_name', 'last_name', 'user_groups', 'email', 'is_active', 'is_staff')
    list_filter = ('is_active', 'is_staff', 'user_groups',)
    search_fields = ('first_name', 'last_name',)


@admin.register(Payment)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'date_pay', 'amount_payment', 'method_payment', 'course', 'lesson', 'user')
    list_filter = ('method_payment', 'user',)
    search_fields = ('method_payment', 'user', 'amount_payment', 'date_pay',)
