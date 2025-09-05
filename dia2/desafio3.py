import math

class FiguraGeometrica:

    def areaCirculo(self, raio):
        areaCirculo = math.pi * math.pow(raio, 2)
        return areaCirculo
    
    def areaTriangulo(self, base, altura):
        areaTriangulo = (base * altura) / 2
        return areaTriangulo

    def hipotenusa(self, cateto_oposto, cateto_adjacente):
        return math.sqrt(math.pow(cateto_oposto, 2) + math.pow(cateto_adjacente, 2))
    
results = FiguraGeometrica()

area_do_circulo = float(input("Digite o raio para saber a área do círculo: "))
area1 = results.areaCirculo(area_do_circulo)
print(f"Área do circulo: {area1} \n")

base = float(input("Digite a base: "))
altura = float(input("Digite a altura: "))
area2 = results.areaTriangulo(base, altura)
print(f"Área do triângulo: {area2} \n")

cat_oposto = float(input("Digite o cateto oposto: "))
cat_adjacente = float(input("Digite o cateto adjacente: "))
area3 = results.areaTriangulo(cat_oposto, cat_adjacente)
print(f"Hipotenusa: {area3}")