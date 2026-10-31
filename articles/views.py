from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.views import View
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404
from taggit.models import Tag
from .models import Article
from .forms import CommentForm
from .services.open_library import search_books

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = "article_new.html"
    fields = (
        "title",
        "body",
        "tags",
        "featured_book_query"
    )
    
    def form_valid(self, form):
        """
        Set the author of an article to the currently logged-in user.
        """
        form.instance.author = self.request.user
        return super().form_valid(form)

class CommentGet(DetailView):
    model = Article
    template_name = "article_detail.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        
        article = self.object
        
        # only search open library if featured book query provided
        if article.featured_book_query:
            context["featured_books"] = search_books(
                article.featured_book_query
            )
        else:
            context["featured_books"] = []
        
        return context
    
class CommentPost(SingleObjectMixin, FormView):
    model = Article
    form_class = CommentForm
    template_name = "article_detail.html"
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        comment = form.save(commit = False)
        comment.article = self.object
        comment.author = self.request.user
        comment.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        article = self.object
        return reverse("article_detail", kwargs = {"pk": article.pk})

class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = "article_list.html"
    
class TaggedArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = "tagged_articles.html"
    context_object_name = "articles"
    
    def get_queryset(self):
        self.tag = get_object_or_404(
            Tag,
            slug = self.kwargs["tag_slug"]
        )
        return Article.objects.filter(
            tags__in = [self.tag]
        )
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tag"] = self.tag
        return context

class ArticleDetailView(LoginRequiredMixin, DetailView):
    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view()
        return view(request, *args, **kwargs)
    
class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = (
        "title",
        "body",
        "tags",
        "featured_book_query"
    )
    template_name = "article_edit.html"
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
    
class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = "article_delete.html"
    success_url = reverse_lazy("article_list")
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user