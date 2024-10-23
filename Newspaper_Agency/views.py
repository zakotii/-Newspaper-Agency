from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from newspaper_app.models import Newspaper, Redactor, Topic  # Удалено дублирование
from newspaper_app.forms import NewspaperForm
from django.contrib.auth.decorators import login_required  # Для декораторов
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView
from django.db.models import Q


class TopicListView(ListView):
    model = Topic
    template_name = 'topic_list.html'
    context_object_name = 'topics'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(Q(name__icontains=query))
        return queryset


@login_required
def admin_dashboard(request):
    newspapers = Newspaper.objects.all()
    redactors = Redactor.objects.all()
    topics = Topic.objects.all()

    context = {
        'newspapers': newspapers,
        'redactors': redactors,
        'topics': topics
    }
    
    return render(request, 'admin_dashboard.html', context)

# Обновление газеты
class NewspaperUpdateView(UpdateView):
    model = Newspaper
    fields = ['title', 'content', 'published_date', 'topic', 'redactor']
    template_name = 'newspaper_form.html'
    success_url = reverse_lazy('admin_dashboard')

# Удаление газеты
class NewspaperDeleteView(DeleteView):
    model = Newspaper
    template_name = 'newspaper_confirm_delete.html'
    success_url = reverse_lazy('admin_dashboard')


# Обновление редактора (Redactor)
class RedactorUpdateView(UpdateView):
    model = Redactor
    fields = ['first_name', 'last_name', 'email', 'hire_date']
    template_name = 'redactor_form.html'
    success_url = reverse_lazy('admin_dashboard')


# Создание нового редактора (Redactor)
class RedactorCreateView(CreateView):
    model = Redactor
    fields = ['first_name', 'last_name', 'email', 'hire_date']
    template_name = 'redactor_form.html'
    success_url = reverse_lazy('admin_dashboard')

# Удаление редактора (Redactor)
class RedactorDeleteView(DeleteView):
    model = Redactor
    template_name = 'redactor_confirm_delete.html'
    success_url = reverse_lazy('admin_dashboard')


# Создание новой темы (Topic)
class TopicCreateView(CreateView):
    model = Topic
    fields = ['name']
    template_name = 'topic_form.html'
    success_url = reverse_lazy('admin_dashboard')

# Обновление темы (Topic)
class TopicUpdateView(UpdateView):
    model = Topic
    fields = ['name']
    template_name = 'topic_form.html'
    success_url = reverse_lazy('admin_dashboard')

# Удаление темы (Topic)
class TopicDeleteView(DeleteView):
    model = Topic
    template_name = 'topic_confirm_delete.html'
    success_url = reverse_lazy('admin_dashboard')


def home(request):
    # Подсчитываем количество газет, редакторов и статей
    newspaper_count = Newspaper.objects.count()
    redactor_count = Redactor.objects.count()
    topic_count = Topic.objects.count()

    # Передаем эти данные в шаблон
    context = {
        'newspaper_count': newspaper_count,
        'redactor_count': redactor_count,
        'topic_count': topic_count,
    }

    return render(request, 'home.html', context)

# Список газет
@login_required  # Добавлен декоратор
def newspaper_list(request):
    newspapers = Newspaper.objects.all()
    return render(request, 'newspaper_list.html', {'newspapers': newspapers})

# Классовое представление с ограничением доступа
class NewspaperListView(LoginRequiredMixin, ListView):
    model = Newspaper
    template_name = 'newspaper_list.html'
    context_object_name = 'newspapers'  # Убедитесь, что используете это имя в шаблоне

# Создание новой газеты
@login_required  # Добавлен декоратор
def newspaper_create(request):
    if request.method == "POST":
        form = NewspaperForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Газета успешно создана.")
            return redirect('newspaper_list')
        else:
            messages.error(request, "Ошибка при создании газеты. Проверьте введённые данные.")
    else:
        form = NewspaperForm()
    return render(request, 'newspaper_form.html', {'form': form})

# Обновление газеты
@login_required  # Добавлен декоратор
def newspaper_update(request, pk):
    newspaper = get_object_or_404(Newspaper, pk=pk)
    if request.method == "POST":
        form = NewspaperForm(request.POST, instance=newspaper)
        if form.is_valid():
            form.save()
            messages.success(request, "Газета успешно обновлена.")
            return redirect('newspaper_list')
        else:
            messages.error(request, "Ошибка при обновлении газеты. Проверьте введённые данные.")
    else:
        form = NewspaperForm(instance=newspaper)
    return render(request, 'newspaper_form.html', {'form': form})

# Список редакторов
@login_required  # Добавлен декоратор
def redactor_list(request):
    redactors = Redactor.objects.all()
    return render(request, 'redactor_list.html', {'redactors': redactors})


@login_required
def topic_list(request):
    query = request.GET.get('q')  # Получаем поисковый запрос, если он есть
    if query:
        # Если запрос есть, ищем темы по части строки (name содержит query)
        topics = Topic.objects.filter(Q(name__icontains=query))
    else:
        # Если запроса нет, показываем все темы
        topics = Topic.objects.all()

    return render(request, 'topic_list.html', {'topics': topics})
