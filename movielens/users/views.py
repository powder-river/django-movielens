from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def user_login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(request, user)
            return redirect('movie_list')
        else:
            return render(request,
                        'users/login.html',
                        {'failed': True,
                        'username': username})

    return render(request,
        'users/login.html')


def logout_view(request):
    logout(request)

    return redirect('user_login')
