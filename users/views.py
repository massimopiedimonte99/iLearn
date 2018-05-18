from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from django.views.generic import View
from .forms import UserForm

class UserFormView(View):
    form_class = UserForm
    template_name='users/registration-form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, { 'form': form })

    def post(self, request):
        form = self.form_class(request.POST)

        # If the form is valid, process the data... otherwise return an empty form.
        if form.is_valid():
            # Store the user informations but don't save it in the database yet.
            user = form.save(commit=False)

            # Clean up the data and store them in the database.
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)

            user.save()

            # Authenticate user.
            user = authenticate(username=username, password=password)

            if user is not None and user.is_active:
                login(request, user)
                return redirect('books:index')


        return render(request, self.template_name, { 'form': form })


def logout_user(request):
    logout(request)
    return redirect('books:index')
