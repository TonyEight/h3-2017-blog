from django.shortcuts import render
from django.views import generic

from .models import Category, Entry


class HomeView(generic.ListView):
	template_name = 'blog/index.html'
	context_object_name = 'categories'
	model = Category


class CategoryIndexView(generic.DetailView):
	template_name = 'blog/category-index.html'
	context_object_name = 'category'
	model = Category


class EntryDetailView(generic.DetailView):
	template_name = 'blog/entry-detail.html'
	context_object_name = 'entry'
	model = Entry