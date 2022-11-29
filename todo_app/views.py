from django.shortcuts import render,redirect

# Create your views here.

from django.views import View
from todo_app.models import Task
from todo_app.forms import TaskForm

class HomeView(View): 
    def get(self, request):
        task_form = TaskForm()
        task = Task.objects.all()
        html_data = {
            'task_list' : task,
            'form' : task_form,
        }
        return render(
            request=request,
            template_name='index.html',
            context={
            'task_list' : task,
            'form' : task_form,
        }
        )
    def post(self, request):
        print(request.POST)
        task_form = TaskForm(request.POST)
        task_form.save()

        return redirect('home')
class TaskDetailView(View):
    def get(self, request, task_id):
        task = Task.objects.get(id=task_id)
        task_form = TaskForm(instance=task)
        html_data = {
            'task_object' : task,
            'form' : task_form,
        }
        return render(
            request=request,
            template_name='detail.html',
            context=html_data,
        )
    def post(self, request, task_id):
        task = Task.objects.get(id=task_id)
        if 'update' in request.POST:
            task_form = TaskForm(request.POST, instance=task)
            task_form.save()
        elif 'delete' in request.POST:
            task.delete()
        return redirect ('home')

        # tasks = Task.objects.all()
        # html_data = {
        #     'task_list' : tasks,
        #     'form': task_form,
        # }
        # return render(
        #     request=request,
        #     template_name='index.html',
        #     context=html_data,
        # )