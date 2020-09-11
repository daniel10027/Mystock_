from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic
from django.db.models import Q

from bootstrap_modal_forms.generic import (
    BSModalLoginView,
    BSModalFormView,
    BSModalCreateView,
    BSModalUpdateView,
    BSModalReadView,
    BSModalDeleteView
)

from .forms import (
    BookModelForm,
    ArticleModelForm,
    CustomUserCreationForm,
    CustomAuthenticationForm,
    BookFilterForm,
    SortieModelForm,
    ArrivageModelForm
)
from .models import Book, Article, Categorie, ArrivageExistant, Sortie


class Index(generic.ListView):
    model = Article
    context_object_name = 'books'
    template_name = 'index.html'

    def get_queryset(self):
        
        query = self.request.GET.get('q')
        if query:
             object_list = self.model.objects.filter(

                Q(nom__icontains=query) |
                Q(categorie__nom__icontains=query) |
                Q(quantite__icontains=query)
              
            )
        else:
            object_list = self.model.objects.all()
        return object_list

    def get_context_data(self, **kwargs):

        context = super(Index, self).get_context_data(**kwargs)
        context['last']    = Article.objects.filter(active=True).order_by("-created")[:4]
        context['nb']      = Article.objects.all().count()
        context['cat']     = Categorie.objects.all().count()
        context['arrivage']= ArrivageExistant.objects.filter(active=True)
        context['sortie']  = Sortie.objects.filter(active=True)
        context['s']       = Sortie.objects.all().count()

        return context


class BookFilterView(BSModalFormView):
    template_name = 'examples/filter_book.html'
    form_class = BookFilterForm

    def form_valid(self, form):
        if 'clear' in self.request.POST:
            self.filter = ''
        else:
            self.filter = '?type=' + form.cleaned_data['type']

        response = super().form_valid(form)
        return response

    def get_success_url(self):
        return reverse_lazy('index') + self.filter


class BookCreateView(BSModalCreateView):
    template_name = 'examples/create_book.html'
    form_class = ArticleModelForm
    success_message = 'Félicitation: Article ajouté avec succes.'
    success_url = reverse_lazy('index')

class ArrivageCreateView(BSModalCreateView):
    template_name = 'examples/arrivage_create_book.html'
    form_class = ArrivageModelForm
    success_message = 'Félicitation: Arrivage enregistré avec succes.'
    success_url = reverse_lazy('index')


class SortieCreateView(BSModalCreateView):
    template_name = 'examples/sortie_create_book.html'
    form_class = SortieModelForm
    success_message = 'Félicitation: sortie enregistré avec succes.'
    success_url = reverse_lazy('index')

class BookUpdateView(BSModalUpdateView):
    model = Article
    template_name = 'examples/update_book.html'
    form_class = ArticleModelForm
    success_message = 'Success: Book was updated.'
    success_url = reverse_lazy('index')


class BookReadView(BSModalReadView):
    model = Article
    template_name = 'examples/read_book.html'


class BookDeleteView(BSModalDeleteView):
    model = Book
    template_name = 'examples/delete_book.html'
    success_message = 'Success: Book was deleted.'
    success_url = reverse_lazy('index')


class SignUpView(BSModalCreateView):
    form_class = CustomUserCreationForm
    template_name = 'examples/signup.html'
    success_message = 'Success: Sign up succeeded. You can now Log in.'
    success_url = reverse_lazy('index')


class CustomLoginView(BSModalLoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'examples/login.html'
    success_message = 'Success: You were successfully logged in.'
    success_url = reverse_lazy('index')


def books(request):
    data = dict()
    if request.method == 'GET':
        books = Book.objects.all()
        data['table'] = render_to_string(
            '_books_table.html',
            {'books': books},
            request=request
        )
        return JsonResponse(data)
