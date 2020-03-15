import uuid
from django.views.generic import ListView, FormView, CreateView, DetailView
from django.http import HttpResponseForbidden
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Comment, Topic
from .forms import CommentForm

class CommentFormView(CreateView):
    model = Comment
    #form_class = CommentForm
    template_name = "posts/comment_form.html"
    fields = ['content']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["node_uid"] = self.kwargs.get("pk", None)
        #print(context["node_uid"])
        return context

    def form_valid(self, form):
        new_comment = form.save(commit=False)
        if self.kwargs.get("pk") != "parent":
            parent_comment = Comment.objects.get(uid=self.kwargs.get("pk"))
            new_comment.parent = parent_comment
            new_comment.post = parent_comment.post
        else:
            new_comment.post = Post.objects.first()
        form.instance.author = self.request.user
        return super().form_valid(form)


class CommentListView(ListView):
    model = Comment
    template_name = "posts/post_recursetree.html"
    context_object_name = "comments"

class TopicMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["topics"] = Topic.objects.all()
        return context

class PostDetailView(DetailView):
    model = Post
    
    def get_object(self, queryset=None):
        item = super().get_object(queryset)
        item.views = item.views + 1
        item.save()
        return item

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context['object'].comments.all())
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'topic']
    template_name = "posts/post_create.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class CreateListView(CreateView):
    model = Comment
    fields = ['content']
    template_name = "posts/home.html"
    ordering = ["-date_posted"]

    def get_context_data(self, **kwargs):
        context = super(CreateListView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context

class PostListView(TopicMixin, ListView):
    model = Post
    template_name = "posts/home.html"
    context_object_name = "posts"
    ordering = ["-date_posted"]
    paginate_by = 5
    
class PostsListByAuthorView(TopicMixin, ListView):
    model = Post
    context_object_name ="posts"
    template_name = "posts/posts_by_author.html"
    paginate_by = 5
    ordering = ["-date_posted"]

    def get_queryset(self):
        author = self.kwargs.get("name", None)
        print(author)
        results = []
        if author:
            results = Post.objects.filter(author__username=author)
        return results

    def get_context_data(self, **kwargs):
        """
        Pass author's username to the context
        """
        context = super().get_context_data(**kwargs)
        context["author"] = self.kwargs.get("name", None)
        return context

class PostsListByTopicView(TopicMixin, ListView):
    model = Post
    context_object_name ="posts"
    template_name = "posts/posts_by_topic.html"
    paginate_by = 5
    ordering = ["-date_posted"]

    def get_queryset(self):
        topic = self.kwargs.get("name", None)
        results = []
        if topic:
            results = Post.objects.filter(topic__name=topic)
        return results

    def get_context_data(self, **kwargs):
        """
        Pass topic's name to the context
        """
        context = super().get_context_data(**kwargs)
        context["topic"] = self.kwargs.get("name", None)
        return context

class CommentCreateView(CreateView):
    model = Comment
    fields = ['content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
