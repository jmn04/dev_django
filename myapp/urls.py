from . import tests
from django.urls import path
from . import views

# Create your tests here.

app_name = 'myapp'
urlpatterns = [
    path('', tests.test, name='test'),
    path('index/', views.NoteIndexView.as_view(), name='index'),
    path('myapp/create/', views.NoteCreateView.as_view(), name='note_input'),
    path('myapp/create/complete/', views.NoteInputCompleteView.as_view(), name='note_input_complete'),
    path('myapp/list/', views.NoteListView.as_view(), name='note_list'),
    path('myapp/detail/<uuid:pk>/', views.NoteDetailView.as_view(), name='note_detail'),
    path('myapp/update/<uuid:pk>/', views.NoteUpdateView.as_view(), name='note_update'),
    path('myapp/delete/<uuid:pk>/', views.NoteDeleteView.as_view(), name='note_delete'),
]
