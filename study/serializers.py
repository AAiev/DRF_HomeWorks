from rest_framework import serializers

from study.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer(read_only=True, many=True)
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
        fields = ('title', 'description', 'image_preview', 'quantity_lessons', 'lesson',)
