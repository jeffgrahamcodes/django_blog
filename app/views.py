from django.shortcuts import render
from django.urls import reverse_lazy
from app.models import Article
from django.views.generic import CreateView, ListView, UpdateView, DeleteView


class ArticleListView(ListView):
    model = Article
    template_name = "app/index.html"
    context_object_name = "articles"


class ArticleCreateView(CreateView):
    model = Article
    fields = ["title", "status", "content", "twitter_post"]
    template_name = "app/article_create_form.html"
    success_url = reverse_lazy("home")


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ["title", "status", "content", "twitter_post"]
    template_name = "app/article_update_form.html"
    success_url = reverse_lazy("home")
    context_object_name = "article"


class ArticleDeleteView(DeleteView):
    model = Article
    template_name = "app/article_delete_form.html"
    success_url = reverse_lazy("home")
    context_object_name = "article"
