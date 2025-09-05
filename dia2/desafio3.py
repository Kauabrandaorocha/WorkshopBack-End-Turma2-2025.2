import math

class FiguraGeometrica:

    def areaCirculo(raio):
        areaCirculo = math.pi * math.pow(raio, 2)
        return areaCirculo
    
    def areaTriangulo(base, altura):
        areaTriangulo = (base * altura) / 2
        return areaTriangulo

    def hipotenusa(cateto_oposto, cateto_adjacente):
        return math.sqrt(math.pow(cateto_oposto, 2) + math.pow(cateto_adjacente, 2))