from django.db import models
from django.utils import timezone
 
# Create your models her
class Vehiculo(models.Model):
    niv = models.CharField(max_length=20, null=False, help_text="Indica NIV del vehiculo")
    noMotor = models.CharField(max_length=30, blank=True)
    marca = models.CharField(max_length=40)
    linea = models.CharField(max_length=40)
    modelo = models.IntegerField(default=0)
    
    def __str__(self):
        return "%s - %s - %s - %s" % (self.niv, self.marca, self.linea, self.modelo)
    
    def __save__(self):
        self.niv = self.niv.upper()
        self.noMotor = self.noMotor.upper()
        super(Vehiculo, self.save())
        
    class Meta:
        db_table = 'vehiculos'
        verbose_name = 'Vehiculo'
        verbose_name_plural = 'VEHICULOS'
        
class Propietario(models.Model):
    rfc = models.CharField(max_length=20)
    nombre = models.CharField(max_length=30) 
    apPaterno = models.CharField(max_length=30)
    apMaterno = models.CharField(max_length=30)
    email = models.EmailField()
    curp = models.CharField(max_length=20)
    direccion = models.CharField(max_length=60)
    cp = models.CharField(max_length=5)
    edad = models.IntegerField(default=0)
    
    def __str__(self):
        return "%s %s %s" % (self.nombre, self.apPaterno, self.apMaterno)
    
    def __save__(self):
        self.rfc = self.rfc.upper()
        self.curp = self.curp.upper()
        super(Propietario, self.save())
        
class Oficina(models.Model):
    nombre = models.CharField(max_length=40)
    ciudad = models.CharField(max_length=30)
    telefono = models.CharField(max_length=15)
    responsable = models.CharField(max_length=40, null=True)
    cp = models.CharField(max_length=5, default=0)
    
    def __str__(self):
        return "%s" % (self.nombre)
    
class Placa(models.Model):
    numero = models.CharField(max_length=20)
    numTC = models.CharField(max_length=20)
    fechaAlta = models.DateTimeField(default=timezone.now)
    fechaBaja = models.DateTimeField(default=timezone.now)
    estatus = models.BooleanField(default=True) #True= Alta, Flase=Baja
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE) 
    oficina =  models.ForeignKey(Oficina, on_delete=models.CASCADE)
    
    def __str__(self):
        return "%s %s %s" % (self.numero, self.vehiculo, self.propietario)
    
    
    
        
        
    