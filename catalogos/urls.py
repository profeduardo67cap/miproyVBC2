from django.urls import path
from catalogos.views import OficinaView, OficinaCreate, OficinaUpdate, OficinaDelete, PlacasCreate, PlacasDelete, PlacasUpdate, PlacasView, PropietarioCreate, PropietarioDelete, PropietarioUpdate, PropietarioView, VehiculoCreate, VehiculoDelete, VehiculoUpdate, VehiculoView

from catalogos import views 


urlpatterns = [
    path('oficina/list', OficinaView.as_view(), name='oficinaList'),
    path('oficina/create', OficinaCreate.as_view(), name='oficinaCreate'),     
    path('oficina/edit/<int:pk>', OficinaUpdate.as_view(), name='oficinaEdit'),
    path('oficina/delete/<int:pk>', OficinaDelete.as_view(), name='oficinaDelete'),
    

    path('vehiculo/list', VehiculoView.as_view(), name='vehiculoList'),
    path('vehiculo/create', VehiculoCreate.as_view(), name='vehiculoCreate'),     
    path('vehiculo/edit/<int:pk>', VehiculoUpdate.as_view(), name='vehiculoEdit'),
    path('vehiculo/delete/<int:pk>', VehiculoDelete.as_view(), name='vehiculoDelete'),
    
    path('propietario/list', PropietarioView.as_view(), name='propietarioList'),
    path('propietario/create', PropietarioCreate.as_view(), name='propietarioCreate'),     
    path('propietario/edit/<int:pk>', PropietarioUpdate.as_view(), name='propietarioEdit'),
    path('propietario/delete/<int:pk>', PropietarioDelete.as_view(), name='propietarioDelete'),
    
    path('placa/list', PlacasView.as_view(), name='placaList'),
    path('placa/create', PlacasCreate.as_view(), name='placaCreate'),     
    path('placa/edit/<int:pk>', PlacasUpdate.as_view(), name='placaEdit'),
    path('placa/delete/<int:pk>', PlacasDelete.as_view(), name='placaDelete'),
    
 
    
    
#     #Rutas para CRUD de Placa
#     path('placa/list', views.placaList, name='placaList'),
#     path('placa/create', views.placaCreate, name='placaCreate'),        
    
]
