from django.shortcuts import render, redirect
from django.views import View

# Create your views here.
class SignIn(View):
  def get(self, request):
    is_login = request.session.get('is_login', False)
    email = request.session.get('email', '')
    params = {'is_login':is_login, 'email': email}
    return render(request, 'sign/signin.html', params)

  def post(self, request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    request.session['email'] = email
    request.session['is_login'] = True
    return redirect('/')


class SignOut(View):
  def post(self, request):
    del request.session['is_login']
    del request.session['email']
    return redirect('/')
