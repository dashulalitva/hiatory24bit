from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import War, Question, Answer, Test
from .forms import AnswerForm


def index(request):
    war1941 = War.objects.all()[:10]
    war1942 = War.objects.all()[10:14]
    war1943 = War.objects.all()[14:20]
    war1944 = War.objects.all()[20:32]
    war1945 = War.objects.all()[32:45]
    return render(request, 'main/index.html', {'war1941': war1941, 'war1942': war1942, 'war1943': war1943, 'war1944': war1944, 'war1945': war1945,})


def test_view(request):
    test = get_object_or_404(Question, pk=1)
    questions = Question.objects.all()
    if request.method == 'POST':
        score = 0
        for question in questions:
            try:
                selected_answer_id = request.POST.get(f'question_{question.id}')  # Получаем ID выбранного ответа
                if selected_answer_id:  # Проверяем, что ответ выбран
                    answer = Answer.objects.get(pk=selected_answer_id)
                    if answer.is_correct:
                        score += 1
                # Если ответ не выбран, ничего не делаем (считаем, что ответ неправильный)
            except ObjectDoesNotExist:
                # Обработка случая, когда ответ с таким ID не найден (маловероятно, но лучше обработать)
                pass  # Или log.error(), если нужна запись в лог

        context = {'test': test, 'score': score, 'total_questions': len(questions)}
        return render(request, 'main/results.html', context)
    else:
        forms = {}
        for question in questions:
            forms[question.id] = AnswerForm(question=question)
        context = {'test': test, 'questions': questions, 'forms': forms}
        return render(request, 'main/test.html', context)
# Create your views here.
def map_interactive(request):
    return render(request, 'main/map.html')