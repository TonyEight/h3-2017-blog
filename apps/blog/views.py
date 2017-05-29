from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from .models import Category, Entry
from .forms import EntryForm


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


class EntryCreateView(LoginRequiredMixin, generic.CreateView):
	template_name = 'blog/entry-create.html'
	model = Entry
	form_class = EntryForm
