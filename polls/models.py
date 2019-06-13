from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
class Question(models.Model): #类为django.db.models.Model的子类
    question_text = models.CharField(max_length=200) #指定数据类型指定最大长度，数据库结构需要、数据验证
    pub_date = models.DateTimeField('date publishded')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)#定义外键关系 每个Choice关联一个Question
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0) #可选参数 defaul为0

    def __str__(self):
        return self.choice_text
