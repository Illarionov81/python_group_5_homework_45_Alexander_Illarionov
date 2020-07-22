from django.shortcuts import render
from webapp.models import To_Do_list



def task_list(request):
    data = To_Do_list.objects.all()
    return render(request, 'index_to_do.html', context={
        'task_list': data
    })

def task_view(request):
    task_id = request.GET.get('pk')
    task = To_Do_list.objects.get(pk=task_id)
    context = {'task': task}
    return render(request, "task.html", context)