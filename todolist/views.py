from django.shortcuts import render,HttpResponse,redirect
from .models import User,Task
from django.template import RequestContext

def login(request):
	if request.method == 'POST':
		RefId = request.POST['RefId']
		if User.objects.filter(RefId=RefId).exists():
			request.session['RefId'] = RefId
			return redirect('login/home')
		else:
			return HttpResponse('nouserfound')
	else:
		return render(request,'todolist/login.html')
def home(request):

	if request.session.has_key('RefId'):
		RefId = request.session['RefId']
		user = User.objects.get(RefId=RefId)
		task = Task.objects.filter(Owner=user.UserId).all()
		
		packet = {
		'user':user,
		'task':task,
		
		}
		return render(request,'todolist/home.html',packet)
	else:
		return redirect('login')

def save(request):
	RefId = request.session['RefId']
	user = User.objects.get(RefId=RefId)
	title=request.GET['title']
	text=request.GET['text']
	task = Task(Owner=user,TaskName=title,Discription=text)
	task.save()
	return redirect('home')


def logout(request):
   try:
      del request.session['RefId']
      request.session.flush()
      from django.contrib.auth.models import AnonymousUser
      request.user = AnonymousUser()
   except:
      pass
   return redirect('login')