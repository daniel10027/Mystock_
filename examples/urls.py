from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [

   
    path('', views.Index.as_view(), name='index'),

    path('filter/', views.BookFilterView.as_view(), name='filter_book'),

    path('create/', views.BookCreateView.as_view(), name='create_book'),

    path('last-create/', views.ArrivageCreateView.as_view(), name='arrivage_create_book'),

    path('sortie/', views.SortieCreateView.as_view(), name='sortie'),

    path('update/<int:pk>', views.BookUpdateView.as_view(), name='update_book'),

    path('read/<int:pk>', views.BookReadView.as_view(), name='read_book'),

    path('delete/<int:pk>', views.BookDeleteView.as_view(), name='delete_book'),

    path('books/', views.books, name='books'),

    path('signup/', views.SignUpView.as_view(), name='signup'),

    path('login/', views.CustomLoginView.as_view(), name='login'),
]
