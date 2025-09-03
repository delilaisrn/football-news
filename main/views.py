from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406405374',
        'name': 'Delila Isrina Aroyo',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)
