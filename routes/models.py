from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True, help_text="Breve descripción de la ciudad")
    atracciones = models.CharField(max_length=100, blank=True, null=True, help_text="Atracciones turísticas")
    mejor_epoca_para_visitar = models.CharField(max_length=50, blank=True, null=True, help_text="Mejor época para visitar")
    clima_promedio = models.CharField(max_length=50, blank=True, null=True, help_text="Clima promedio")# Clima promedio

    def __str__(self):
        return f"{self.name}"

class Route(models.Model):
    start_city = models.ForeignKey(City, related_name='route_start', on_delete=models.CASCADE)
    end_city = models.ForeignKey(City, related_name='route_end', on_delete=models.CASCADE)
    distance = models.FloatField()

    def __str__(self):
        return f"{self.start_city.name} -> {self.end_city.name} ({self.distance} km)"




