from django.forms import ModelForm
from todo_app.models import Task, Comment,Tag

class TaskForm(ModelForm):
    class Meta():
        model = Task
        fields = ['description']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body'] 
    def __init__(self, *args, **kwargs):
        task_object = kwargs.pop('task')
        super().__init__(*args, **kwargs)
        self.instance.task = task_object

class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ['name'] 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        


    def save(self,task, *args, **kwargs):
        tag_name = self.data['name']
        self.fields['name'].label=''
        tagmain = Tag.objects.create(name=tag_name)
        task.tags.add(tagmain) 