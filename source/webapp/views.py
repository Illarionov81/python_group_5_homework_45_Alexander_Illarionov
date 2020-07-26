from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import To_Do_list, STATUS_CHOICES
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
    task.delete()
    return redirect("task_list")


def task_add_view(request):
    if request.method == "GET":
        return render(request, 'task_create.html', context={
            'status_choices': STATUS_CHOICES
        })
    elif request.method == 'POST':
        summary = request.POST.get('summary')
        description = request.POST.get('description')
        status = request.POST.get('status')
        completion_time = request.POST.get('completion_time', None)
        if completion_time:
            task = To_Do_list.objects.create(summary=summary, description=description,
                                             completion_time=completion_time,
                                             status=status)
        else:
            task = To_Do_list.objects.create(summary=summary, description=description,
                                             status=status)
        return redirect('task_view', pk=task.pk)
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])
