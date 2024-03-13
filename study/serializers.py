from rest_framework import serializers

from study.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):

    quantity_lessons = serializers.SerializerMethodField()

    def get_quantity_lessons(self, obj):
        '''вывод количества уроков'''
        quantity_lessons = obj.lesson.all()
        if not quantity_lessons:
            return None
        else:
            return len(quantity_lessons)



    class Meta:
        model = Course
        fields = '__all__'