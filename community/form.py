from django import forms
from community.models import User


class QuestionForm(forms.ModelForm):
    class Meta:
        model = User  # 사용할 모델
        fields = ['name', 'age', 'gender', 'date', 'time']  # QuestionForm에서 사용할 Question 모델의 속성