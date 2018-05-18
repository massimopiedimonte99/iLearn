from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Count
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Author, Book
 
'''

Basic Views

'''
def index_view(request):
    try:
        return render(request, 'books/index.html', { 
            'books': Book.objects.all(),
            'user': request.user
        })
    except:
        return render(request, 'books/index.html', {
            'books': Book.objects.all(),
        })

class DetailView(generic.DetailView):
    model = Book
    template_name="books/detail.html"


'''

Crud Operations.

'''
class AddBook(LoginRequiredMixin, CreateView):
    model = Book
    fields = ['author' , 'title', 'isbn', 'cover_image']
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddBook, self).form_valid(form)

class EditBook(LoginRequiredMixin, UpdateView):
    model = Book
    fields = ['author' , 'title', 'isbn', 'cover_image']
    login_url = '/login/'
    template_name='books/edit_form.html'
    redirect_field_name = 'redirect_to'

class DeleteBook(LoginRequiredMixin, DeleteView):
    model = Book
    fields = ['author' , 'title', 'isbn']
    success_url = reverse_lazy('books:index')
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    ''' 
    
        This function is used to convert get requests to post requests and let me omit
        a delete confirmation page. 

    '''
    def get(self, request, *args, **kwargs):
        book_publisher = Book.objects.filter(pk=self.kwargs['pk'])[0].user
        # If the publisher is not the authenticated user, don't delete the book!
        if(request.user != book_publisher):
            return render(request, 'books/index.html', {
                'books': Book.objects.all(),
                'b': book_publisher
            })    
        return self.post(request, *args, **kwargs)

class AddAuthor(LoginRequiredMixin, CreateView):
    model = Author
    fields = ['name' , 'surname']
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = "books/author_form.html"