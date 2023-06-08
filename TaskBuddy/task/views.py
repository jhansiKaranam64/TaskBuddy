from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateTaskForm,CreateUserForm, LoginForm,UpdateTaskForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from . models import Task
from django.core.exceptions import ValidationError
from django.db.models import Q
# Create your views here.
def home(request):
    
    return render(request,"index.html")

#- Registering/creating a user
def register(request):
    form= CreateUserForm()
    if request.method =='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('my-login')
        
    context ={'form':form}

    return render(request,'register.html',context=context)

#- Login a user
def my_login(request):
    form= LoginForm
    if request.method =='POST':
        form = LoginForm(request,data=request.POST)
        if form.is_valid():

            username=request.POST.get('username')
            password=request.POST.get('password')

            user = authenticate(request,username=username,password=password)

            if user is not None:
                auth.login(request,user)
                return redirect("dashboard")
    context={'form':form}
    return render(request,"my-login.html",context=context)

#-Dashboard page
@login_required(login_url='my-login')
def dashboard(request):
    return render(request,'profile/dashboard.html')

#- Create a task page
@login_required(login_url='my-login')
def createTask(request):
    form = CreateTaskForm()

    if request.method == 'POST':

        form=CreateTaskForm(request.POST)
        if form.is_valid():

            task = form.save(commit=False)
            task.user = request.user

            task.save()

            return redirect('view-tasks')
        
    context={'form':form}
    return render(request,'profile/create-task.html',context=context)

#- Create a task page
@login_required(login_url='my-login')
def viewTask(request):
    
    current_user = request.user.id
    task = Task.objects.all().filter(user=current_user).order_by('completed','due')

    context={'task':task}
    context['count'] = context['task'].filter(completed=False).count()
    
    return render(request,'profile/view-tasks.html',context=context)

#-Search and filtering a task
def task_list(request):
    query = request.GET.get('query', '')
    filter_status = request.GET.get('status', '')
    current_user = request.user.id
    task = Task.objects.all().filter(user=current_user).order_by('completed','due')

    if query:
        task = task.filter(Q(title__icontains=query) | Q(content__icontains=query))

    if filter_status:
        if filter_status == 'completed':
            task = task.filter(completed=True)
        elif filter_status == 'pending':
            task = task.filter(completed=False)
    context={'task': task, 'query': query, 'filter_status': filter_status}
    return render(request, 'profile/view-tasks.html', context=context)

#- update task page
@login_required(login_url='my-login')
def updateTask(request,pk):

    task = Task.objects.get(id=pk)
    form = UpdateTaskForm(instance=task)

    if request.method =='POST':

        form =UpdateTaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('view-tasks')
        
    context = {'form':form}
    return render(request,'profile/update-task.html',context=context)

#- Delete task page
def deleteTask(request,pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        
        task.delete()

        return redirect('view-tasks')
    return render(request,'profile/delete-task.html')


#-Logout a user
def user_logout(request):

    auth.logout(request)
    return redirect('home')
        
    

