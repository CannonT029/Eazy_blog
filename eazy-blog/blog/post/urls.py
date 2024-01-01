from django.urls import path


from . import views



urlpatterns =[
      path('search/', views.search, name='search'),
      path('<slug:category_slug>/<slug:slug>', views.detail, name='post_detail'),
      path('<slug:slug>/', views.category, name='category_detail'),
      path('<slug:slug>/edit/', views.edit_post, name='edit_post'),
      path('<slug:slug>/delete/', views.delete, name='delete_post'),

]