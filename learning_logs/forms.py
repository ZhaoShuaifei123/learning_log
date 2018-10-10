from django import forms
from .models import Topic ,Entry

class TopicForm(forms.ModelForm):
	"""forms表单：会根据Modle中我们自己定义的数据表自己创建表单,并且会添加默认的小部件，然后在html页面调用form就可以显示表单，而不用
	我们自己去写表单如<input>等"""
	class Meta:
		model=Topic
		fields=['text']
		labels={'text':""}

class EntryForm(forms.ModelForm):
	class Meta:
		model=Entry
		fields={'text'}
		labels={'text':""}
		widgets={'text':forms.Textarea(attrs={'cols':80})}


