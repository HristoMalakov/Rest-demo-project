from django.db import models


class Question(models.Model):
    author = models.CharField(max_length=50, default="Anonymous")
    question = models.TextField()

    def __str__(self):
        return f"{self.author} : {self.question}"



class Answer(models.Model):
    author = models.CharField(max_length=50, default="Anonymous")
    content = models.TextField()
    likes = models.PositiveIntegerField()
    dislikes = models.PositiveIntegerField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author} : {self.content[:10]}..."


