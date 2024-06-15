from django.shortcuts import render,redirect
from .models import Note,Entry
from .forms import Noteform

from django.contrib.auth.decorators import login_required

from django.views import View
from django.views.generic import ListView,DetailView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

def index(request):
    return render(request,'notes/index.html')

class indexView(View):
    
    template_name='notes/index.html'
    
    def get(self,request,*args,**kwargs):
        return render(request,self.template_name,{'title':'make NOTE of your EVERYTHING'})

@login_required
def notes(request):
    
    notes=Note.objects.order_by('-date_added')
    
    context={'notes':notes}
    
    return render(request,'notes/notes.html',context)

class notesListView(LoginRequiredMixin,ListView):
    model=Note
    template_name='notes/notes.html'
    context_object_name='notes'

@login_required
def note(request,note_id):
    note=Note.objects.get(id=note_id)
    entries=note.entry_set.order_by('date_added')
    
    context={'note':note,'entries':entries}
    
    return render(request,'notes/note.html',context)

class noteDetailView(DetailView):
    model=Note
    pk_url_kwarg='id'
    template_name='notes/note.html'
    context_object_name='note'
    

@login_required 
def new_note(request):
    if request.method !='POST':
        form=Noteform()
    else:
        form=Noteform(data=request.POST)
        if form.is_valid():
            new_note=form.save()
            new_note.save()
            return redirect('notes:notes')
    context={'form':form}
    return render(request,'notes/new_note.html',context)

class newNoteCreateView(CreateView):
    model=Note
    form_class=Noteform
    template_name='notes/new_note.html'
    success_url=reverse_lazy('notes:notes')