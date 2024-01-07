from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from django.db import models  
from .models import Author, Quote, Tag
from .serializers import AuthorSerializer, QuoteSerializer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]

class QuoteListCreateView(generics.ListCreateAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [IsAuthenticated]

class QuoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [IsAuthenticated]

def quotes_by_tag(request, tag_name):
    tag = Tag.objects.get(name=tag_name)
    quotes = Quote.objects.filter(tags=tag)
    return render(request, 'quotes_by_tag.html', {'tag': tag, 'quotes': quotes})

def quotes_list(request):
    all_quotes = Quote.objects.all()
    quotes_per_page = 10
    paginator = Paginator(all_quotes, quotes_per_page)
    page = request.GET.get('page')

    try:
        quotes = paginator.page(page)
    
    except PageNotAnInteger:
        quotes = paginator.page(1)
    
    except EmptyPage:
        quotes = paginator.page(paginator.num_pages)

    return render(request, 'author_quote/quotes_list.html', {'quotes': quotes})

def top_tags(request):
    top_tags = Tag.objects.annotate(num_quotes=models.Count('quote')).order_by('-num_quotes')[:10]
    return render(request, 'top_tags.html', {'top_tags': top_tags})