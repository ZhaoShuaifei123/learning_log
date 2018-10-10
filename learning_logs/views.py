from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Topic,Entry
from .forms import TopicForm,EntryForm
from django.http import HttpResponseRedirect, Http404


# Create your views here.

def index(request):
	"""学习笔记的主页"""
	return render(request, "lenarning_logs/index.html")#第一个参数是原始请求对象

def test(request):
	"""学习笔记的主页"""
	return render(request, "lenarning_logs/test.html")#第一个参数是原始请求对象

@login_required()
def topics(request):
	"""显示当前用户的所有主题"""
	topics=Topic.objects.filter(owner=request.user).order_by("date_added")
	context={"topics_date":topics}
	return render(request,"lenarning_logs/topics.html",context)

@login_required()
def topic(request,topic_id):
	"""显示当前用户进入某个主题后显示的对应条目"""
	topic=Topic.objects.get(id=topic_id)#获得某一条具体数据用get，获得很多条数据用过滤filter
	#确认请求主题的是当前用户
	if topic.owner!=request.user:
		raise Http404  #抛出异常，404:服务器上没有请求的资源
	entries=topic.entry_set.order_by("-date_added")
	context={"topic_date":topic,"entries_date":entries}
	return render(request,"lenarning_logs/topic.html",context)

@login_required()
def new_topic(request):
	"""添加新主题"""
	if request.method!="POST":
		"未提交数据，返回空表单"
		form=TopicForm()#创建了一个空表单
	else:
		form=TopicForm(request.POST) #拿到提交的表单信息,并将数据放入创建成的表单中
		if form.is_valid():
			new_topic=form.save(commit=False)#将表单数据保存到数据库
			new_topic.owner=request.user
			new_topic.save()
			return HttpResponseRedirect('topics')

	context = {'form': form}
	return render(request,"lenarning_logs/new_topic.html",context)

@login_required()
def new_entry(request,topic_id):
	"""为某个主题添加内容"""
	topic=Topic.objects.get(id=topic_id)
	if request.method!="POST":
		form=EntryForm()
	else:
		form=EntryForm(request.POST)
		if form.is_valid():
			new_entry=form.save(commit=False)#创建数据库中entry对象，但是不保存到数据库
			new_entry.topic=topic
			new_entry.save()
			return redirect(reverse('topic',args=[topic.id]))#快捷键：alt+enter

	context={'topic':topic,'form':form}

	return render(request,'lenarning_logs/new_entry.html',context)

@login_required()
def edit_entry(request,entry_id):
	"""编辑具体内容"""
	entry=Entry.objects.get(id=entry_id)
	topic=entry.topic
	# 确认请求编辑具体内容的是当前用户
	if topic.owner!=request.user:
		raise Http404

	if request.method!="POST":
		#初次请求，使用当前条目填充表单,如果不传递参数instance=entry，则创建的form表单是一个空表单不会带上数据
		form=EntryForm(instance=entry)
	else:
		# POST提交数据，对数据进行处理
		form = EntryForm(instance=entry, data=request.POST)
		if form.is_valid():
			form.save()
			return redirect(reverse('topic', args=[topic.id]))

	context={'entry':entry,'topic':topic,'form':form}
	return render(request,'lenarning_logs/edit_entry.html',context)
















