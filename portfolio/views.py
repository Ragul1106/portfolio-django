from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib import messages
from .models import Profile, Skill, Project
from .forms import ContactForm


def home(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all()[:6]
    projects = Project.objects.all()[:6]
    return render(request, 'home.html', {
        'profile': profile,
        'skills': skills,
        'projects': projects,
    })


def about(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all()
    return render(request, 'about.html', {
        'profile': profile,
        'skills': skills,
    })


class ProjectListView(ListView):
    model = Project
    template_name = 'portfolio/projects_list.html'
    context_object_name = 'projects'
    paginate_by = 9


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'portfolio/project_detail.html'
    context_object_name = 'project'


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you — your message was sent successfully.')
            return redirect('portfolio:contact')
        else:
            messages.error(request, 'Please fix the errors below.')
    else:
        form = ContactForm()
    return render(request, 'portfolio/contact.html', {'form': form})
