from django import forms
from .models import Question, Answer

class AnswerForm(forms.Form):
    answer = forms.ModelChoiceField(queryset=Answer.objects.none(), widget=forms.RadioSelect) #Отображаем в виде радиокнопок

    def __init__(self, question, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['answer'].queryset = question.answers.all() # Выбираем варианты ответа для конкретного вопроса