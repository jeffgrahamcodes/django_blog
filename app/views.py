from typing import Any

from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from app.models import Article
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = "app/index.html"
    context_object_name = "articles"

    def get_queryset(self) -> QuerySet[Any]:
        return Article.objects.filter(creator=self.request.user).order_by("-created_at")


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    fields = ["title", "status", "content", "twitter_post"]
    template_name = "app/article_create_form.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = ["title", "status", "content", "twitter_post"]
    template_name = "app/article_update_form.html"
    success_url = reverse_lazy("home")
    context_object_name = "article"

    def test_func(self) -> bool | None:
        return self.request.user == self.get_object().creator


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = "app/article_delete_form.html"
    success_url = reverse_lazy("home")
    context_object_name = "article"

    def test_func(self) -> bool | None:
        return self.request.user == self.get_object().creator
