from django.views.generic import ListView, FormView, CreateView, DetailView
from .models import Post, Comment, Topic

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

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']

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
        topic = self.kwargs.get("author", None)
        results = []
        if topic:
            reuslts = Post.objects.filter(author__username=topic)
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
        print(topic)
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
