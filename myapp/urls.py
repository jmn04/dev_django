from . import tests
from . import blog
from . import flatpages
from django.urls import path
from . import views

# Create your tests here.

app_name = 'myapp'
urlpatterns = [
    path('', tests.test, name='test'),
    path('blog/', blog.blog, name='blog'),
    path('flatpages/', flatpages.flatpages, name='flatpages'),
    path('index/', views.NoteIndexView.as_view(), name='index'),
    path('myapp/create/', views.NoteCreateView.as_view(), name='note_input'),
    path('myapp/create/complete/', views.NoteInputCompleteView.as_view(), name='note_input_complete'),
    path('myapp/list/', views.NoteListView.as_view(), name='note_list'),
    path('myapp/detail/<uuid:pk>/', views.NoteDetailView.as_view(), name='note_detail'),
    path('myapp/update/<uuid:pk>/', views.NoteUpdateView.as_view(), name='note_update'),
    path('myapp/delete/<uuid:pk>/', views.NoteDeleteView.as_view(), name='note_delete'),
    # path('', views.NoteIndexView.as_view(), name='index'),
    # path('', views.NoteCreateView.as_view(), name='note_input'),
    # path('', views.NoteInputCompleteView.as_view(), name='note_input_complete'),
    # path('', views.index, name='index'),
    # path('', views.note_input, name='note_input'),
    # path('', views.note_input_complete, name='note_input_complete'),
    # path('',views.NoteIndexView.index(), name='index'),
    # path('note_input', views.NoteCreateView.note_input(), name='note_input'),
    # path('<int:id>', views.NoteInputCompleteView.note_input_complete(), name='note_input_complete')
]
