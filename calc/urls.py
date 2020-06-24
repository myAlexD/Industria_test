from django.urls import path
from . import views as calc_view

urlpatterns = [
    path('calc/', calc_view.calc, name="calculator"),
    path('', calc_view.home, name="home")
]
