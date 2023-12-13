from django.shortcuts import render, HttpResponse, redirect
from .models import Vehiculo, Propietario, Oficina, Placa
from .forms import VehiculoForm, PropietarioForm, OficinaForm, PlacaForm

# Create your views here.
def homeCatalogos(request):
    return render(request, 'homeCatalogos.html')

# -----------------------------------------------------------------------------
def vehiculoList(request):
    vehiculos = Vehiculo.objects.all()  # uso de queryset's de Django
    data = {'vehiculos' : vehiculos}
    return render(request, "vehiculoList.html", data)

def vehiculoCreate(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('vehiculoList')
    else:
        form = VehiculoForm()
    return render (request, 'vehiculoCrear.html', {'form' :  form})

def vehiculoUpdate(request):
    return HttpResponse("<h4>Módulo para modificar dats de un Aula... </h4>")

def vehiculoDelete(request):
    return HttpResponse("<h5>Elimianndo vehiculo !!! </h5>")

# -----------------------------------------------------------------------------

def propietarioList(request):
    propietarios = Propietario.objects.all()  # uso de queryset's de Django
    data = {'propietarios' : propietarios}
    return render(request, "propietarioList.html", data)

def propietarioCreate(request):
    if request.method == 'POST':
        form = PropietarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('propietarioList')
    else:
        form = PropietarioForm()
    return render (request, 'propietarioCrear.html', {'form' :  form})


# ==========================  CRUD PARA EL MODELO << Oficina >> =============================

def oficinaList(request):
    
    oficinas = Oficina.objects.all().filter(ciudad='Apizaco')
    
    numOficinas = Oficina.objects.count()
    data = {'oficinas' : oficinas,
            'numOficinas' : numOficinas
    }
    return render(request, 'oficinaList.html', data)

def oficinaCreate(request):
    if request.method == 'POST':            # Formulario con datos,  listo para guardarse
        form = OficinaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('oficinaList')
    else:                                      # Acabas de igresar al formulario para captura
        form = OficinaForm()
    return render (request, 'oficinaCreate.html', {'form' :  form})

def oficinaEdit(request, id):
    oficina = Oficina.objects.get(id=id)        # Se obtiene la oficina segun su ID
    if request.method == 'GET':
        form = OficinaForm(instance = oficina)  # Pinta form con datos ya existentes
    else:
        form = OficinaForm(request.POST, instance=oficina)   # Se ha hecho modificacion
        if form.is_valid():
            form.save()
        return redirect ('oficinaList')
    return render (request, 'oficinaCreate.html', {'form':form})   # Manda a traer form para editar

def oficinaDelete(request, id):
    oficina = Oficina.objects.get(id=id)
    if request.method == 'POST':            # Se confirma Eliminar
        oficina.delete()                    # Se borra registro de la BD
        return redirect('oficinaList')
    return render(request, 'oficinaDelete.html', {'oficina' : oficina})

# ========================================================================
    

def placaList(request):
    placas = Placa.objects.all()
    data = {'placas' : placas}
    return render(request, 'placaList.html', data)

def placaCreate(request):
    if request.method == 'POST':
        form = PlacaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('placaList')
    else:
        form = PlacaForm()
    return render (request, 'placaCrear.html', {'form' :  form})
