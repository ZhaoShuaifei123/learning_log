from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.

def logout_view(request):
	"""注销用户"""
	logout(request)
	return redirect(reverse('index'))

def register(request):
	"""注册新用户"""
	if request.method!="POST":
		#显示空的注册表单
		form=UserCreationForm()
	else:
		# 处理填写好的表单
		form=UserCreationForm(data=request.POST)
		if form.is_valid():
			new_user=form.save()#在数据库中保存的是用户名和密码的散列值，save方法会返回新创建的用户对象
			# 让用户自动登录，再重定向到主页
			authenticated_user=authenticate(username=new_user.username,password=request.POST['password1'])
			login(request,authenticated_user)
			return redirect(reverse('index'))
	context={'form':form}
	return render(request,'users/register.html',context)











