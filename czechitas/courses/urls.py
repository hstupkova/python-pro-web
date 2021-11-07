from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path("kontakty", views.ContactsView.as_view(), name="contacts"),
    path("o-nas", views.AboutView.as_view(), name="about"),
    path('kurzy', views.CourseListView.as_view(), name="course_list")
]