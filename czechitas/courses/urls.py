from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path("kontakty", views.ContactsView.as_view(), name="contacts"),
    path("o-nas", views.AboutView.as_view(), name="about"),
    path('kurzy', views.CourseListView.as_view(), name="course_list"),
    path('pobocky', views.BranchListView.as_view(), name="branch_list"),
    path('zamestnanci', views.PersonListView.as_view(), name="person_list"),
    path('kurz/<int:pk>', views.CourseDetailView.as_view(), name="course_detail")
]