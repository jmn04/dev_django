from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from .forms import NoteForm
from .models import NoteTable
from django.shortcuts import get_object_or_404
from django.utils import timezone
import cgi

# Create your views here.
class NoteIndexView(TemplateView):
    template_name = 'index.html'

class NoteCreateView(CreateView):
    template_name = 'note_input.html'
    form_class = NoteForm
    success_url = reverse_lazy('myapp:note_input_complete')

class NoteInputCompleteView(TemplateView):
    template_name = 'note_input_complete.html'

class NoteListView(ListView):
    template_name = 'note_list.html'
    model = NoteTable

class NoteDetailView(DetailView):
    template_name = 'note_detail.html'
    model = NoteTable

class NoteUpdateView(UpdateView):
    template_name = 'note_update.html'
    model = NoteTable
    fields = ('title','image', 'text')
    success_url = reverse_lazy('myapp:note_list')

    def form_valid(self, form):
        note = form.save(commit=False)
        note.updated_at = timezone.now()
        note.save()
        return super().form_valid(form)

class NoteDeleteView(DeleteView):
    template_name = 'note_delete.html'
    model = NoteTable
    success_url = reverse_lazy('myapp:note_list')

# def index(request):
#     notes = NoteTable.objects.all().order_by('-updated_datetime')
#     return render(request, 'myapp/templates/index.html', { 'notes': notes })

# def note_input(request):
#     return render(request, 'myapp/templates/note_input.html')

# def note_input_complete(request, note_id):
#     note = get_object_or_404(NoteTable, id=note_id)
#     return render(request, 'myapp/templates/note_input_complete.html', {'note': note})


#自作
def memoCreateView(request):
    template_name="note_input.html"

    if request.POST:
        title = request.POST["title"]
        f = cgi.FieldStorage()
        text = f.getfirst("text")
        image = request.POST["image"]
        if request.FILES:
            image = request.FILES.get("image")
        # content = request.POST["content"]

    #受け取った値で必要な処理を行います
        
    return render(request, template_name)