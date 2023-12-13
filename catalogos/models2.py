from django.db import models

# Create your models here.
class Profesor(models.Model):
    numero = models.IntegerField(default=0, null=False, help_text="Numero del profesor")
    nombre = models.CharField(max_length=50, blank=True, null=True)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return '%s  %s' % (self.numero, self.nombre)
    
    def __save__(self):
        self.nombre = self.nombre.upper()
        super(Profesor, self.save())
        
    class meta:
        verbose_name_plural = "PROFESORES"
        db_table = 'profesores'
        
    