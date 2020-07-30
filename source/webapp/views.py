from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import To_Do_list, STATUS_CHOICES
from webapp.forms import TaskForm
from django.http import HttpResponseNotAllowed


def task_list(request):
    data = To_Do_list.objects.all()
    return render(request, 'index_to_do.html', context={
        'task_list': data
    })


def task_view(request, pk):
    task = get_object_or_404(To_Do_list, pk=pk)
    context = {'task': task}
    return render(request, "task.html", context)


def task_delete_view(request, pk):
    task = get_object_or_404(To_Do_list, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', context={'task': task})
    elif request.method == 'POST':
        task.delete()
        return redirect("task_list")


def task_create_view(request, *args, **kwargs):
    if request.method == "GET":
        return render(request, 'task_create.html', context={
            'form': TaskForm()
        })
    elif request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            summary = form.cleaned_data['summary']
            description = form.cleaned_data['description']
            status = form.cleaned_data['status']
            completion_time = form.cleaned_data['completion_time']
            if completion_time:
                task = To_Do_list.objects.create(summary=summary, description=description,
                                                 completion_time=completion_time,
                                                 status=status)
            else:
                task = To_Do_list.objects.create(summary=summary, description=description,
                                                 status=status)
            return redirect('task_view', pk=task.pk)
        else:
            return render(request, 'task_create.html', context={'form': form})
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])


def task_update_view(request, pk):
    task = get_object_or_404(To_Do_list, pk=pk)
    if request.method == "GET":
        return render(request, 'task_update.html', context={'status_choices': STATUS_CHOICES, 'task': task})
    elif request.method == 'POST':
        errors = {}
        task.summary = request.POST.get('summary')
        if not task.summary:
            errors['summary'] = 'Это поле обязательне для сохранения!'
        task.description = request.POST.get('description')
        task.status = request.POST.get('status')
        if not task.status:
            errors['status'] = 'Это поле обязательне для сохранения!'
        completion_time = request.POST.get('completion_time')
        if completion_time:
            task.completion_time = request.POST.get('completion_time')
        if errors:
            return render(request, 'task_update.html', context={'status_choices': STATUS_CHOICES,
                                                                'task': task,
                                                                'errors': errors})
        task.save()
        return redirect('task_view', pk=task.pk)
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])
