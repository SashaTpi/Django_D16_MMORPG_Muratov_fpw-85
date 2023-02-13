from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm, ReplyForm


#Posts:
class PostList(ListView):
    model = Post
    template_name = 'main.html' #'mmorpg.html'
    context_object_name = 'posts'
    paginate_by = 10
    ordering = ['-date']


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'create.html'
    context_object_name = 'post'
    form_class = PostForm
    success_url = '/'


class PostDetails(DetailView):
    model = Post
    template_name = 'post_details.html'
    context_object_name = 'post'


    def post(self, request, pk):
        reply_for_change_status = Reply.objects.get(id=request.POST.get('p_r_n_a_id'))
        reply_for_change_status.accept_status = True
        reply_for_change_status.save(update_fields=['accept_status'])
        return redirect('post_details', pk)


class PostEdit(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'edit.html'
    context_object_name = 'post_details'
    success_url = '/'


class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'delete.html'
    context_object_name = 'post'
    success_url = '/'


#Reply:
class ReplyList(LoginRequiredMixin, ListView):
    model = Reply
    template_name = 'reply_list.html'
    context_object_name = 'replies'
    paginate_by = 20
    ordering = ['-date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author_reply'] = Reply.objects.filter(author=self.request.user).order_by('-date')
        return context


class ReplyDetails(LoginRequiredMixin, DetailView):
    model = Reply
    template_name = 'reply_details.html'
    context_object_name = 'reply'


class ReplyCreate(LoginRequiredMixin, CreateView):
    model = Reply
    template_name = 'reply_create.html'
    form_class = ReplyForm
    success_url = '/replies/'
    context_object_name = 'reply'


class ReplyEdit(LoginRequiredMixin, UpdateView):
    model = Reply
    template_name = 'reply_edit.html'
    form_class = ReplyForm
    success_url = '/replies/'
    context_object_name = 'reply'


class ReplyDelete(LoginRequiredMixin, DeleteView):
    model = Reply
    template_name = 'reply_delete.html'
    context_object_name = 'reply'
    success_url = '/replies/'


class LoginAccount(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'login_account.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(author=self.request.user).order_by('-date')
        return context

    def post(self, request):
        reply_for_change_status = Reply.objects.get(id=request.POST.get('reply_id'))
        reply_for_change_status.accept_status = True
        reply_for_change_status.save(update_fields=['accept_status'])
        return redirect('login_account')


class ReplyDeleteByPostAuthor(LoginRequiredMixin, DeleteView):
    template_name = 'reply_delete_by_post_author.html'
    success_url = '/login/'
    queryset = Reply.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = Post.objects.get(reply=context['reply'])
        return context