from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from newspaper_app.models import Newspaper, Redactor, Topic  # Удалено дублирование
from newspaper_app.forms import NewspaperForm
from django.contrib.auth.decorators import login_required  # Для декораторов
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView


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

# Список тем/статей
@login_required  # Добавлен декоратор
def topic_list(request):
    topics = Topic.objects.all()  # Получаем список тем
    return render(request, 'topic_list.html', {'topics': topics})
