from django.db import models


class War(models.Model):
    year = models.TextField(blank = True)
    month = models.TextField(blank = True)
    description = models.TextField(blank = True)
    image = models.ImageField(upload_to='media', blank = True)
    def __str__(self):
        return self.description


class Test(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True) # Описание теста
    # Другие поля, например, автор, дата создания

    def __str__(self):
        return self.title


class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='questions') # Связь с моделью теста
    text = models.CharField(max_length=500)

    def __str__(self):
        return self.text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text
