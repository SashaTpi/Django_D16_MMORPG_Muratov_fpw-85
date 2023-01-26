from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView

from .filters import NoteFilter, ResponseFilter
from .forms import NoteForm, ResponseForm
from .models import *


class NoteMain(ListView):
    model = Note
    template_name = 'main.html'
    context_object_name = 'notes'
    ordering = ['post_date']
    paginate_by = 5


class NoteCreate(CreateView):
    template_name = 'note_create.html'
    form_class = NoteForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class NoteDelete(DeleteView):
    template_name = 'note_delete.html'
    queryset = Note.objects.all()
    success_url = reverse_lazy('main')


class NoteDetail(DetailView):
    template_name = 'note_detail.html'
    queryset = Note.objects.all()
    form = ResponseForm
    extra_context = {'form': ResponseForm}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        note_author = Note.objects.get(id=pk).user
        current_user = self.request.user

        if current_user.is_authenticated:
            if note_author == self.request.user:
                context['pole_response'] = False
                context['message_response'] = False
                context['edit_delete'] = True
            elif Response.objects.filter(user_response=self.request.user).filter(note=pk).exists():
                context['pole_response'] = False
                context['message_response'] = True
                context['edit_delete'] = False
            else:
                context['pole_response'] = True
                context['message_response'] = False
                context['edit_delete'] = False

        return context

    def post(self, request, *args, **kwargs):
        form = ResponseForm(request.POST)
        if form.is_valid():
            form.instance.note_id = self.kwargs.get('pk')
            form.instance.user_response = self.request.user
            form.save()
            return redirect(request.META.get('HTTP_REFERER'))


class NoteEdit(UpdateView):
    template_name = 'note_edit.html'
    form_class = NoteForm

    def get_object(self, **kwargs):
        pk = self.kwargs.get('pk')
        return Note.objects.get(pk=pk)


class NoteSearch(ListView):
    model = Note
    template_name = 'note_search.html'
    context_object_name = 'note'
    ordering = ['post_date'] #'-datetime'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filters'] = NoteFilter(self.request.GET, queryset=self.get_queryset())
        return context


class ResponseList(ListView):
    template_name = 'user_response.html'
    context_object_name = 'responses'
    ordering = ['-datetime']

    def get_queryset(self, **kwargs):
        user_id = self.request.user.id
        return Response.objects.filter(note__user=user_id).filter(status_del=False).filter(status_add=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.request.user.id
        context['filter'] = ResponseFilter(self.request.GET, queryset=self.get_queryset())
        context['new_response'] = Response.objects. \
            filter(note__user=user_id).filter(status_del=False).filter(status_add=False)
        context['del_response'] = Response.objects.filter(note__user=user_id).filter(status_del=True)
        context['add_response'] = Response.objects.filter(note__user=user_id).filter(status_add=True)
        return context


class ResponseAccept(View):
    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        resp = Response.objects.get(pk=pk)
        resp.status_add = 1
        resp.status_del = 0
        resp.save()

        return redirect('response')


class ResponseRemove(View):
    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        qaz = Response.objects.get(id=pk)
        qaz.status_del = 1
        qaz.status_add = 0
        qaz.save()

        return redirect('response')


class ProtectNoteCreate(LoginRequiredMixin, NoteCreate):
    permission_required = ('create',)


class ProtectNoteDelete(LoginRequiredMixin, NoteDelete):
    permission_required = ('delete',)


class ProtectNoteEdit(LoginRequiredMixin, NoteEdit):
    permission_required = ('edit',)


class ProtectResponseList(LoginRequiredMixin, ResponseList):
    permission_required = ('response',)


class ProtectResponseAccept(LoginRequiredMixin, ResponseAccept):
    permission_required = ('accept',)


class ProtectResponseRemove(LoginRequiredMixin, ResponseRemove):
    permission_required = ('remove',)
