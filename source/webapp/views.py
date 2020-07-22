from django.shortcuts import render
from webapp.models import To_Do_list, STATUS_CHOICES
from django.http import HttpResponseNotAllowed


def task_list(request):
    data = To_Do_list.objects.all()
    return render(request, 'index_to_do.html', context={
        'task_list': data
    })


def tasks_view(request):
    task_id = request.GET.get('pk')
    task = To_Do_list.objects.get(pk=task_id)
    context = {'task': task}
    return render(request, "task.html", context)

def task_delete_view(request):
    task_id = request.GET.get('pk')
    task = To_Do_list.objects.get(pk=task_id)
    task.delete()
    data = To_Do_list.objects.all()
    return render(request, 'index_to_do.html', context={
        'task_list': data
    })


def task_add_view(request):
    if request.method == "GET":
        return render(request, 'task_create.html', context={
            'status_choices': STATUS_CHOICES
        })
    elif request.method == 'POST':
        description = request.POST.get('description')
        completion_time = request.POST.get('completion_time', None)
        status = request.POST.get('status')
        task = To_Do_list.objects.create(description=description,
                                         completion_time=completion_time,
                                         status=status)
        context = {'task': task}
        return render(request, 'task.html', context)
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])
