from rest_framework import serializers

from materials.models import Course, Lesson
from materials.validators import validator_url


class LessonSerializer(serializers.ModelSerializer):
    url_video = serializers.URLField(validators=[validator_url])

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer(read_only=True, many=True)
    quantity_lessons = serializers.SerializerMethodField()
    subscribe = serializers.SerializerMethodField()

    def get_quantity_lessons(self, obj):
        """вывод количества уроков"""
        quantity_lessons = obj.lesson.all().count()
        return quantity_lessons

    def get_subscribe(self, obj):
        # вывод наличия подписки
        subscribe = obj.subscribe.is_active
        return subscribe

    class Meta:
        model = Course
        fields = ('id', 'title', 'description', 'image_preview', 'quantity_lessons', 'lesson',)
