from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    # name of the field is question_text
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    # ForeignKey is used to link the question to the choise
    # on_delete=models.CASCADE means that if the question is deleted,
    # all the choises will be deleted as well
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choise_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choise_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)