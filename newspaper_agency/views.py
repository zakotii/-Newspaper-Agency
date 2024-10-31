from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from newspaper_app.models import Newspaper, Redactor, Topic
from newspaper_app.forms import NewspaperForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.db.models import Q


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['newspaper_count'] = Newspaper.objects.count()
        context['redactor_count'] = Redactor.objects.count()
        context['topic_count'] = Topic.objects.count()
        context['num_visits'] = self.request.session.get("num_visits", 0) + 1
        self.request.session["num_visits"] = context['num_visits']
        context['newspapers'] = Newspaper.objects.all()
        return context


class AdminDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'admin_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'newspapers': Newspaper.objects.all(),
            'redactors': Redactor.objects.all(),
            'topics': Topic.objects.all()
        })
        return context


class NewspaperListView(LoginRequiredMixin, ListView):
    model = Newspaper
    template_name = 'newspaper_list.html'
    context_object_name = 'newspapers'
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Newspaper.objects.filter(title__icontains=query) if query else Newspaper.objects.all()


class RedactorListView(LoginRequiredMixin, ListView):
    model = Redactor
    template_name = 'redactor_list.html'
    context_object_name = 'redactors'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Redactor.objects.filter(first_name__icontains=query) if query else Redactor.objects.all()


class TopicListView(LoginRequiredMixin, ListView):
    model = Topic
    template_name = 'topic_list.html'
    context_object_name = 'topics'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Topic.objects.filter(name__icontains=query) if query else Topic.objects.all()


class NewspaperCreateView(LoginRequiredMixin, CreateView):
    model = Newspaper
    form_class = NewspaperForm
    template_name = 'newspaper_form.html'
    success_url = reverse_lazy('newspaper_list')

    def form_valid(self, form):
        messages.success(self.request, "Газета успешно создана.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Ошибка при создании газеты.")
        return super().form_invalid(form)


class RedactorCreateView(LoginRequiredMixin, CreateView):
    model = Redactor
    fields = ['first_name', 'last_name', 'email', 'hire_date']
    template_name = 'redactor_form.html'
    success_url = reverse_lazy('admin_dashboard')


class TopicCreateView(LoginRequiredMixin, CreateView):
    model = Topic
    fields = ['name']
    template_name = 'topic_form.html'
    success_url = reverse_lazy('admin_dashboard')


# Обновление и удаление
class NewspaperUpdateView(LoginRequiredMixin, UpdateView):
    model = Newspaper
    fields = ['title', 'content', 'published_date', 'topic', 'redactor']
    template_name = 'newspaper_form.html'
    success_url = reverse_lazy('admin_dashboard')


class RedactorUpdateView(LoginRequiredMixin, UpdateView):
    model = Redactor
    fields = ['first_name', 'last_name', 'email', 'hire_date']
    template_name = 'redactor_form.html'
    success_url = reverse_lazy('admin_dashboard')


class TopicUpdateView(LoginRequiredMixin, UpdateView):
    model = Topic
    fields = ['name']
    template_name = 'topic_form.html'
    success_url = reverse_lazy('admin_dashboard')


# Удаление
class NewspaperDeleteView(LoginRequiredMixin, DeleteView):
    model = Newspaper
    template_name = 'newspaper_confirm_delete.html'
    success_url = reverse_lazy('admin_dashboard')


class RedactorDeleteView(LoginRequiredMixin, DeleteView):
    model = Redactor
    template_name = 'redactor_confirm_delete.html'
    success_url = reverse_lazy('admin_dashboard')


class TopicDeleteView(LoginRequiredMixin, DeleteView):
    model = Topic
    template_name = 'topic_confirm_delete.html'
    success_url = reverse_lazy('admin_dashboard')
