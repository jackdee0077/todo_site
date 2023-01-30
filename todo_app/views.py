from django.shortcuts import render,redirect

# Create your views here.

from django.views import View

from todo_app.models import Task, Comment,Tag
from todo_app.forms import TaskForm, CommentForm,TagForm

class HomeView(View): 
    '''
        Home view function as the site homepage, 
        listing out all task objects in data base and linking out each ones detail view
        '''
    def get(self, request):
        '''
        the content requires to render the homepage
        '''

        task_form = TaskForm()
        task = Task.objects.all()
        html_data = {
            'task_list' : task,
            'form' : task_form,

        }
        return render(
            request=request,
            template_name='index.html',
            context= html_data
            
        )
    def post(self, request):
        '''
        this method saves new TAsks to the data base before redirecting'''
        task_form = TaskForm(request.POST)
        task_form.save()

        return redirect('home')

class TaskDetailView(View):
    '''
    TaskDetailView provides the ability to update and delete indidual 
    Task object from the database 
    '''
    def get(self, request, task_id):
        ''' 
        The content required to render a task object's detail pagepy
        '''
        task = Task.objects.get(id=task_id)
        task_form = TaskForm(instance=task)

        tag_form=TagForm
        tags=task.tags.all()
        comments = Comment.objects.filter(task=task)
        comment_form = CommentForm(task=task)

        html_data = {
            'task_object' : task,
            'form' : task_form,
            'comment_list': comments,
            'comment_form': comment_form,
            'tag_form': tag_form,
            'tags': tags,
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
        elif 'add' in request.POST:
            comment_form = CommentForm (request.POST, task=task)
            comment_form.save()
            return redirect('task_detail', task_id=task_id)
        return redirect ('home')





        