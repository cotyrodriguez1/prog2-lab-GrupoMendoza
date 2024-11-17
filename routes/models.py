# Importa la clase models desde Django, que se usa para definir los modelos de base de datos
from django.db import models

# Define la clase 'City', que representará una ciudad en la base de datos
class City(models.Model):
    
    # 'name' es un campo de texto (cadena de caracteres) para el nombre de la ciudad
    name = models.CharField(max_length=100)
    
    # 'descripcion' es un campo de texto que permite una descripción detallada de la ciudad
    # Puede estar vacío (blank=True) y ser nulo (null=True)
    descripcion = models.TextField(blank=True, null=True, help_text="Breve descripción de la ciudad")
    
    # 'atracciones' es un campo de texto para describir las atracciones turísticas de la ciudad
    # También puede estar vacío y nulo
    atracciones = models.CharField(max_length=100, blank=True, null=True, help_text="Atracciones turísticas")
    
    # 'mejor_epoca_para_visitar' es un campo de texto donde se indica la mejor época para visitar la ciudad
    # Puede estar vacío y ser nulo
    mejor_epoca_para_visitar = models.CharField(max_length=50, blank=True, null=True, help_text="Mejor época para visitar")
    
    # 'clima_promedio' es un campo de texto para describir el clima promedio de la ciudad
    # También puede estar vacío y nulo
    clima_promedio = models.CharField(max_length=50, blank=True, null=True, help_text="Clima promedio")


    # Este método __str__ se usa para representar la ciudad como una cadena, normalmente se usa para las vistas en el panel de administración o en otras representaciones
    def __str__(self):
        # Devuelve el nombre de la ciudad como la representación en texto
        return f"{self.name}"

# Define la clase 'Route', que representará una ruta entre dos ciudades en la base de datos
class Route(models.Model):
    
    # 'start_city' es una relación de clave foránea a un objeto de la clase 'City'
    # Se usa 'related_name' para poder referirse a la relación desde el modelo 'City' de una forma más legible
    start_city = models.ForeignKey(City, related_name='route_start', on_delete=models.CASCADE)
    
    # 'end_city' es otra relación de clave foránea a un objeto de la clase 'City', indicando el destino de la ruta
    # También se usa 'related_name' para poder acceder a la relación desde el modelo 'City'
    end_city = models.ForeignKey(City, related_name='route_end', on_delete=models.CASCADE)
    
    # 'distance' es un campo de tipo flotante que representa la distancia de la ruta en kilómetros
    distance = models.FloatField()

    # Este método __str__ define cómo se representará la ruta como una cadena de texto
    def __str__(self):
        # Devuelve una representación en texto de la ruta como: "Ciudad de origen -> Ciudad de destino (distancia km)"
        return f"{self.start_city.name} -> {self.end_city.name} ({self.distance} km)"
    
def obtener_rutas_desde_ciudad(ciudad_destino_id):
    # Obtener la ciudad de destino por su ID
    ciudad_destino = City.objects.get(id=ciudad_destino_id)
    
    # Obtener todas las rutas que terminan en la ciudad de destino
    rutas_desde_destino = ciudad_destino.route_end.all()
    
    # Imprimir las rutas
    for ruta in rutas_desde_destino:
        print(ruta)