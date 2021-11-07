from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from . import models

class IndexView(TemplateView):
    template_name = "index.html"

class ContactsView(TemplateView):
    template_name = "contacts.html"

class AboutView(TemplateView):
    template_name = "about.html"

class CourseListView(ListView):
    model = models.Course
    template_name = "course_list.html"