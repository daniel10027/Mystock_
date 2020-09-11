from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from bootstrap_modal_forms.forms import BSModalModelForm, BSModalForm
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin

from .models import Book, Article, Categorie, ArrivageExistant, Sortie


class BookFilterForm(BSModalForm):
    type = forms.ChoiceField(choices=Book.BOOK_TYPES)

    class Meta:
        fields = ['type', 'clear']




class BookModelForm(BSModalModelForm):
    publication_date = forms.DateField(
        error_messages={'invalid': 'Enter a valid date in YYYY-MM-DD format.'}
    )

    class Meta:
        model = Book
        exclude = ['timestamp']

class ArticleModelForm(BSModalModelForm):


    class Meta:
        model = Article
        exclude = ['active','created','date_update']

class ArrivageModelForm(BSModalModelForm):


    class Meta:
        model = ArrivageExistant
        exclude = ['active','created','date_update']

class SortieModelForm(BSModalModelForm):


    class Meta:
        model = Sortie
        exclude = ['active','created','date_update']


class CustomUserCreationForm(PopRequestMixin, CreateUpdateAjaxMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
