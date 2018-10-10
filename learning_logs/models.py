from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Topic(models.Model):
	"""用户学习主题"""
	owner = models.ForeignKey(User,on_delete=models.CASCADE) # 删除关联数据,与之关联也删除
	text=models.CharField(max_length=200)
	date_added=models.DateTimeField(auto_now_add=True) #不是字符串类型

	def __str__(self):
		"""返回模型的字符串表示"""
		return self.text  #必须返回字符串

class Entry(models.Model):
	"""学到的有关某个主题的具体知识"""
	topic=models.ForeignKey(Topic,on_delete=models.CASCADE) # 删除关联数据,与之关联也删除
	text=models.TextField()
	date_added=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		"""返回模型的字符串表示"""
		if len(self.text)>20 :
			return self.text[:20]+"..."
		else:
			return self.text


