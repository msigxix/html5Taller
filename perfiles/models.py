from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from unittest.util import _MAX_LENGTH
from django.urls import reverse


class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=255, blank=True)
    web = models.URLField(blank=True)

    # Python 3
    def __str__(self): 
        return self.usuario.username

@receiver(post_save, sender=User)
def crear_usuario_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(usuario=instance)

@receiver(post_save, sender=User)
def guardar_usuario_perfil(sender, instance, **kwargs):
    instance.perfil.save()



class campus (models.Model):
    id_campus = models.AutoField(primary_key=True)
    cam_nombre= models.CharField(max_length=50)
    cam_descripcion = models.CharField(max_length=50)
    cam_longitud = models.CharField(max_length=50)
    cam_latitud = models.CharField(max_length=50)
    
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.cam_nombre
    
    
    @property
    def coordenadas(self):
        "Devuelve las coordenas del campus"
        return '%s %s' % (self.cam_longitud, self.cam_latitud)
    
class carreras (models.Model):
    id_carrera = models.AutoField(primary_key=True)
    car_nombre= models.CharField(max_length=50)
    
    
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.car_nombre   
    
    
class periodoslectivos (models.Model):
    id_periodo = models.AutoField(primary_key=True)
    per_descripcion= models.CharField(max_length=50)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.per_descripcion
    
class estudiantesresumen (models.Model):
    id_estudianter = models.AutoField(primary_key=True)
    est_inscritos= models.IntegerField()
    est_prematriculados = models.IntegerField()
    est_matriculados = models.IntegerField()
    id_campus = models.ForeignKey(campus, on_delete=models.CASCADE)
    id_carrera = models.ForeignKey(carreras, on_delete=models.CASCADE)
    id_periodo = models.ForeignKey(periodoslectivos, on_delete=models.CASCADE)
    
class asignaturasresumen (models.Model):
    id_asignaturar = models.AutoField(primary_key=True)
    asi_aprobadas= models.IntegerField()
    asi_reprobados = models.IntegerField()
    asi_anulados = models.IntegerField()
    asi_retiros = models.IntegerField()
    id_campus = models.ForeignKey(campus, on_delete=models.CASCADE)
    id_carrera = models.ForeignKey(carreras, on_delete=models.CASCADE)
    id_periodo = models.ForeignKey(periodoslectivos, on_delete=models.CASCADE)
    
class consultatablas(models.Manager):
    def with_counts(self):
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute("""
                Select cam_nombre campus,car_nombre carrera,per_descripcion periodo, est_inscritos inscritos, est_prematriculados prematriculados, est_matriculados matriculados from perfiles_campus, perfiles_carreras, perfiles_periodoslectivos, perfiles_estudiantesresumen where id_campus = id_campus_id and id_periodo = id_periodo_id and id_carrera = id_carrera_id and id_periodo = id_periodo_id""")
            result_list = []
            for row in cursor.fetchall():
                p = self.model(campus=row[0], carrera=row[1], periodo=row[2])
                p.num_responses = row[3]
                result_list.append(p)
        return result_list
    
from django.db import connection

def my_sql(self):
    with connection.cursor() as cursor:
        cursor.execute("UPDATE bar SET foo = 1 WHERE baz = %s", [self.baz])
        cursor.execute("SELECT foo FROM bar WHERE baz = %s", [self.baz])
        row = cursor.fetchone()

    return row    
    
    
    
