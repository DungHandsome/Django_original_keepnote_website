from django.shortcuts import render, redirect
from django.contrib import messages
from .form import NoteForm
from .models import note
# Create your views here.
def index(request):
    item_list = note.objects.order_by("-date")
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note')
    form = NoteForm()

    page = {
        "forms": form,
        "list": item_list,
        "title": "KEEP NOTE"
    }
    return render(request, 'note/index.html', page)


def remove(request, item_id):
    item = note.objects.get(id = item_id)
    item.delete()
    messages.info(request, "Chúc mừng 1 note của bạn đã đăng xuất khỏi server trái đất")
    return redirect('note')