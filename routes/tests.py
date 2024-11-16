from django.test import TestCase
from .models import City, Route
from .utils import get_shortest_path

class DijkstraAlgorithmTest(TestCase):
    def setUp(self):
        # crea las ciudades
        self.mdza = City.objects.create(name="MDZA")  #mendoza
        self.uspta = City.objects.create(name="USPTA")    #uspallata
        self.gc = City.objects.create(name="GC")    #godoy cruz
        self.lh = City.objects.create(name="LH")    #las heras
        self.ldc = City.objects.create(name="LDC")    #lujan de cuyo
        
        #crea las rutas con las distancias dadas
        Route.objects.create(start_city=self.mdza, end_city=self.gc, distance=6.0)
        Route.objects.create(start_city=self.mdza, end_city=self.lh, distance=4.4)
        Route.objects.create(start_city=self.mdza, end_city=self.ldc, distance=18.4)
        Route.objects.create(start_city=self.mdza, end_city=self.uspta, distance=120.5)

        #agrega rutas directas adicionales entre otras ciudades
        Route.objects.create(start_city=self.mdza, end_city=self.lh, distance=10.0)
        Route.objects.create(start_city=self.gc, end_city=self.lh, distance=5.0)  
        Route.objects.create(start_city=self.lh, end_city=self.uspta, distance=50.0) 
        Route.objects.create(start_city=self.gc, end_city=self.ldc, distance=15.0)   

    def test_direct_route(self):
        #prueba una ruta directa donde no se necesita pasar por otra ciudad
        path, distance = get_shortest_path(self.mdza, self.gc)
        expected_path = [self.mdza, self.gc]
        expected_distance = 6.0

        self.assertEqual(path, expected_path)
        self.assertEqual(distance, expected_distance)

    def test_indirect_route_via_mendoza(self):
        #prueba una ruta donde el camino más corto es directo a las heras
        path, distance = get_shortest_path(self.mdza, self.lh)
        expected_path = [self.mdza, self.lh]
        expected_distance = 4.4

        self.assertEqual(path, expected_path)
        self.assertAlmostEqual(distance, expected_distance)

    def test_shortest_path_via_uspallata(self):
        #prueba que el algoritmo elija la ruta más corta pasando por Uspallata
        path, distance = get_shortest_path(self.mdza, self.lh)
        expected_path = [self.mdza, self.uspta, self.lh]  #ruta que pasa por Uspallata
        expected_distance = 120.5 + 50.0  #distancia total: mdza a uspta + ustda a lh

        self.assertEqual(path, expected_path)
        self.assertEqual(distance, expected_distance)

    def test_path_with_multiple_stops(self):
        #prueba una ruta más compleja que pasa por múltiples ciudades
        path, distance = get_shortest_path(self.mdza, self.uspta)
        expected_path = [self.mdza, self.uspta]
        expected_distance = 120.5  #distancia de mdza a uspta

        self.assertEqual(path, expected_path)
        self.assertAlmostEqual(distance, expected_distance, places=1)
