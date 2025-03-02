import math

media_gol = float(input('Promedio de Goles: '))

xg = int(input('Goles esperado: '))


def distribution_poisson(media, xg):
    e = 2.78**-media
    
    #Para calcular la posibilidad de +0.5 goles
    if(xg == 1):
        probabilidad_de_k = ((media**(xg-1) * e)/ math.factorial(xg-1))
        
        probalidad_de_gol = 1 - probabilidad_de_k;
        
        probalidad_de_gol = round(probalidad_de_gol, 2)
        
        print(f'Probabilidad de que marque {xg} o más goles  es de: {probalidad_de_gol}%')
        
    #Para calcular la posibilidad de +1.5 goles
    elif(xg == 2):
        probabilidad_de_k1 = ((media**(0) * e)/ math.factorial(0))
        
        probabilidad_de_k2 = ((media**(xg-1) * e)/ math.factorial(xg-1))
        
        probalidad_de_gol = 1 - probabilidad_de_k1 - probabilidad_de_k2
        
        probalidad_de_gol = round(probalidad_de_gol, 2)
        
        print(f'Probabilidad de que marque {xg} o más goles  es de: {probalidad_de_gol}%')
    
    #Para calcular la posibilidad de +2.5 goles
    elif(xg == 3):
        probabilidad_de_k1 = ((media**(0) * e)/ math.factorial(0))
        
        probabilidad_de_k2 = ((media**(xg-2) * e)/ math.factorial(xg-2))
        
        probabilidad_de_k3 = ((media**(xg-1) * e)/ math.factorial(xg-1))
        
        probalidad_de_gol = 1 - probabilidad_de_k1 - probabilidad_de_k2 - probabilidad_de_k3
        
        probalidad_de_gol = round(probalidad_de_gol, 2)
        
        print(f'Probabilidad de que marque {xg} o más goles  es de: {probalidad_de_gol}%')
        
distribution_poisson(media_gol, xg)