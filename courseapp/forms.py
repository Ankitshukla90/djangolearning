from django import forms

from .models import Lesson, Badge, Quiz, LessonContent

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['title', 'content', 'points', 'level', 'image']

class BadgeForm(forms.ModelForm):
    class Meta:
        model = Badge
        fields = ['name', 'description', 'points', 'image']

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['name', 'lesson', 'question', 'option1', 'option2', 'option3', 'option4', 'correct_answer', 'image']

class LessonContentForm(forms.ModelForm):
    class Meta:
        model = LessonContent
        fields = ['lesson', 'content_type', 'order', 'content', 'image']