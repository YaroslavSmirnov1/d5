from django.urls import path
from .views import NewsList, NewsDetailView, NewsSearch, NewsSearch, AddNews, ChangeNews, DeleteNews

urlpatterns = [
    path('', NewsList.as_view()),
    path('<int:pk>', NewsDetailView.as_view()),
    path('search/', NewsSearch.as_view(), name='news_search'),

    path('add/', AddNews.as_view(), name='news_add'),
    path('edit/<int:pk>', ChangeNews.as_view(), name='news_edit'),
    path('delete/<int:pk>', DeleteNews.as_view(), name='news_delete'),

]
