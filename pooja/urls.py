from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from pooja import views

urlpatterns = [
    path('', views.index, name="index"),
    path('home/', views.user_home, name="user_home"),
    path('view_category/', views.view_category, name="view_category"),
    path('view_category/<int:cid>', views.view_category, name="view_category"),
    path('product_details/', views.product_details, name="product_details"),
    path('product_details/<int:pid>', views.product_details, name="product_details"),
    path('blog_details/', views.blog_details, name="blog_details"),

    path('', views.index, name="index"),
    path('home', views.user_home, name="home"),

    #Category urls
    # path('Foods', views.foods, name="Foods"),
    # path('Clothing', views.clothing, name="Cloting"),






]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
