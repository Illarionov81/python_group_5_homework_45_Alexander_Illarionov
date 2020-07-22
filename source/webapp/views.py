from django.shortcuts import render

def to_do(request):
    if request.method =='GET':
        return render(request, "index_to_do.html")
    elif request.method == 'POST':
        print(request.POST)
        context = {
            'first_namber': request.POST.get('first_namber', 0),
            'second_namber': request.POST.get('second_namber', 0),
            'do': request.POST.get('do', 0),
            'rezalt': 0
        }

        return render(request, 'index_to_do.html', context)