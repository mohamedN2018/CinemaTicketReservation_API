"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from tickets import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('guests', views.viewsets_guest)
router.register('movies', views.viewsets_movie)
router.register('reservations', views.viewsets_reservation)

urlpatterns = [
    path('admin/', admin.site.urls),

    # 1
    path('django/jsonenmodel/', views.on_rest_no_model),

    # 2
    path('django/jsonenfrommodel/', views.no_rest_from_model),

    # 3 GET POST from rest framework function based view @api_view
    path('rest/fbv/', views.FBV_List),

    # 3.2 GET PUT DELETE from rest framework function based view @api_view
    path('rest/fbv/<int:pk>/', views.FBV_pK),

    # 4.1 GET POST from rest framework class based view view APIview
    path('rest/cbv/', views.CBV_List.as_view()),

    # 4.2 GET PUT DELETE from rest framework class based view APIview
    path('rest/cbv/<int:pk>/', views.CBV_pK.as_view()),

    # 5.1 mixins list
    path('rest/mixins/', views.mixins_list.as_view()),

    # 5.2 mixins get retrieve update delete
    path('rest/mixins/<int:pk>/', views.mixins_detail.as_view()),

    # 6.1 generic list
    path('rest/generic/', views.Generic_List.as_view()),

    # 6.2 generic get retrieve update delete
    path('rest/generic/<int:pk>/', views.Generic_pK.as_view()),

    #viewsets
    path('rest/viewsets/', include(router.urls))

]
