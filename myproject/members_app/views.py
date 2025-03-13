from django.shortcuts import render, redirect

def input_view(request):
    if request.method == "POST":
        request.session['user_input'] = request.POST.get('user_input', '')
        return redirect('output_view')
    return render(request, 'members_app/input.html')

def output_view(request):
    user_input = request.session.get('user_input', 'Немає даних')
    return render(request, 'members_app/output.html', {'user_input': user_input})

def session_view(request):
    count = request.session.get('count', 0)
    request.session['count'] = count + 1
    return render(request, 'members_app/session.html', {'count': count})
