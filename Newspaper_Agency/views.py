from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from newspaper_app.models import Newspaper
from newspaper_app.forms import NewspaperForm

# Список газет
def newspaper_list(request):
    newspapers = Newspaper.objects.all()
    return render(request, 'newspaper_list.html', {'newspapers': newspapers})

# Создание новой газеты
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
