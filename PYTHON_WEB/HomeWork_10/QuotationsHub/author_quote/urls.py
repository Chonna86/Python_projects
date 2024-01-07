from django.urls import path
from .views import AuthorListCreateView, QuoteListCreateView, QuoteDetailView, quotes_by_tag ,top_tags

urlpatterns = [
    path('authors/', AuthorListCreateView.as_view(), name='author-list-create'),
    path('quotes/', QuoteListCreateView.as_view(), name='quote-list-create'),
    path('quotes/<int:pk>/', QuoteDetailView.as_view(), name='quote-detail'),
    path('quotes/tag/<str:tag_name>/', quotes_by_tag, name='quotes_by_tag'),
    path('top_tags/', top_tags, name='top_tags'),
]