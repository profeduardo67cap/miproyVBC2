from django import forms 
from .models import Vehiculo, Propietario, Oficina, Placa

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class' : 'form-control'})
            
class PropietarioForm(forms.ModelForm):
    class Meta:
        model = Propietario
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class' : 'form-control'})            
            
class OficinaForm(forms.ModelForm):
    class Meta:
        model = Oficina
        fields = '__all__' 
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['nombre'].widget.attrs.update({'class': 'form-control'})
        self.fields['ciudad'].widget.attrs.update({'class': 'form-control'})
        self.fields['telefono'].widget.attrs.update({'class': 'form-select'})
        self.fields['responsable'].widget.attrs.update({'class': 'form-check'})
        self.fields['cp'].widget.attrs.update({'class': 'form-control'})
        
class PlacaForm(forms.ModelForm):
    class Meta:
        model = Placa
        
        fields = [
            'numero',
            'numTC',
            'fechaAlta',
            'fechaBaja',
            'estatus',
            'vehiculo',
            'propietario',
            'oficina'
        ] 
        
        labels = {
            'numero': 'Numero',
            'numTC': 'No. de Tarjeta de circulación',
            'fechaAlta': 'Fecha de Alta de la Placa',
            'estatus': 'Estatus',
            'vehiculo': 'Vehiculo',
            'propietario': 'Propietario del Vehiculo',
            'oficina':'Oficina Recaudadora'
        }
        
        '''
        fechaAlta = forms.DateField(
            label = "Fecha de alta de la placa:",
            widget = forms.DateInput(attrs={'class':'form-control', 'type': 'date'})           
        )
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['fechaAlta'].initial = datetime.date.today()
        
        
        widget = {
            'numero' : forms.TextInput(),
            'numTC' : forms.TextInput(),
            'estatus' : forms.Select(),
            'vehiculo' : forms.Select(),
            'propietario' : forms.TextInput(),
            'oficina' : forms.TextInput()     
        }
        '''
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['numero'].widget.attrs.update({'class': 'form-control'})
        self.fields['numTC'].widget.attrs.update({'class': 'form-control'})
        self.fields['fechaAlta'].widget.attrs.update({'class': 'form-control','type': 'date'})
        self.fields['fechaBaja'].widget.attrs.update({'class': 'form-control', 'type':'date'})
        self.fields['estatus'].widget.attrs.update({'class': 'form-select'})
        self.fields['vehiculo'].widget.attrs.update({'class': 'form-control'})
        self.fields['propietario'].widget.attrs.update({'class': 'form-control'})
        self.fields['oficina'].widget.attrs.update({'class': 'form-control'})
    