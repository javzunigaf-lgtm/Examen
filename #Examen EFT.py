#Ejercicio EFT

def validar_codigo(codigo, peliculas):
    if codigo.strip() == "": 
        return False
    if codigo.upper() in peliculas: 
        return False
    return True

def validar_titulo(titulo):
    return titulo.strip() != ""

def validar_genero(genero):
    return genero.strip() != ""

def validar_duracion(duracion):
    return duracion > 0

def validar_clasificacion(clasificacion):
    return clasificacion.upper() in ['A', 'B', 'C']

def validar_idioma(idioma):
    return idioma.strip() != ""

def validar_es_3d(es_3d):
    return es_3d.lower() in ['s', 'n']

def validar_precio(precio):
    return precio > 0

def validar_cupos(cupos):
    return cupos >= 0

def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opción: "))
            if opcion >= 1 and opcion <= 6:
                return opcion
            print("Debe seleccionar una opción válida")
        except ValueError:
            print("Debe seleccionar una opción válida")


def cupos_genero(genero, peliculas, cartelera):
    total_cupos = 0
    for codigo in peliculas:
        if peliculas[codigo][1].lower() == genero.lower():
            if codigo in cartelera:
                total_cupos += cartelera[codigo][1]
    print(f"El total de cupos disponibles es: {total_cupos}")


def busqueda_precio(p_min, p_max, peliculas, cartelera):
    resultados = []
    for codigo in cartelera:
        precio = cartelera[codigo][0]
        cupos = cartelera[codigo][1]
        
        if precio >= p_min and precio <= p_max and cupos > 0:
            titulo = peliculas[codigo][0]
            resultados.append(f"{titulo}--{codigo}")
            
    if len(resultados) > 0:
        resultados.sort()
        print(f"Las películas encontradas son: {resultados}")
    else:
        print("No hay películas en ese rango de precios.")


def buscar_codigo(codigo, cartelera):
    return codigo.upper() in cartelera


def actualizar_precio(codigo, nuevo_precio, cartelera):
    if buscar_codigo(codigo, cartelera):
        cartelera[codigo.upper()][0] = nuevo_precio
        return True
    return False


def agregar_pelicula(codigo, titulo, genero, duracion, clasificacion, idioma, es_3d, precio, cupos, peliculas, cartelera):
    cod_upper = codigo.upper()
    if cod_upper in peliculas:
        return False
    
    if es_3d.lower() == 's':
        valor_3d = True
    else:
        valor_3d = False
        
    peliculas[cod_upper] = [titulo, genero, duracion, clasificacion.upper(), idioma, valor_3d]
    cartelera[cod_upper] = [precio, cupos]
    return True


def eliminar_pelicula(codigo, peliculas, cartelera):
    cod_upper = codigo.upper()
    if buscar_codigo(cod_upper, cartelera):
        del peliculas[cod_upper]
        del cartelera[cod_upper]
        return True
    return False


def main():
    peliculas = {
        'P101': ['Luz de Otoño', 'drama', 110, 'B', 'Español', False],
        'P102': ['Noche Neón', 'acción', 125, 'C', 'Ingles', True],
        'P103': ['Planeta Agua', 'documental', 90, 'A', 'Español', False],
        'P104': ['Risa Total', 'comedia', 105, 'A', 'Español', True],
        'P105': ['Código Zero', 'thriller', 118, 'C', 'Ingles', True],
        'P106': ['Viaje Lunar', 'ciencia ficción', 132, 'B', 'Ingles', False]
    }

    cartelera = {
        'P101': [5990, 40],
        'P102': [7990, 0],
        'P103': [4990, 25],
        'P104': [6990, 12],
        'P105': [8990, 8],
        'P106': [7490, 3]
    }

    menu = True
    while menu:
        print("\n========== MENÚ PRINCIPAL ==========")
        print("1. Cupos por género")
        print("2. Búsqueda de películas por rango de precio")
        print("3. Actualizar precio de película")
        print("4. Agregar película")
        print("5. Eliminar película")
        print("6. Salir")
        print("=====================================")
        
        
        opcion = leer_opcion()

        if opcion == 1:
            gen = input("Ingrese género a consultar: ")
            cupos_genero(gen, peliculas, cartelera)

        elif opcion == 2:
            while True:
                try:
                    p_min = int(input("Ingrese precio mínimo: "))
                    p_max = int(input("Ingrese precio máximo: "))
                    busqueda_precio(p_min, p_max, peliculas, cartelera)
                    break
                except ValueError:
                    print("Debe ingresar valores enteros")

        elif opcion == 3:
            resp = 's'
            while resp.lower() == 's':
                cod = input("Ingrese código de película: ")
                try:
                    n_precio = int(input("Ingrese nuevo precio: "))
                    if actualizar_precio(cod, n_precio, cartelera):
                        print("Precio actualizado")
                    else:
                        print("El código no existe")
                except ValueError:
                    print("Debe ingresar un precio entero.")
                resp = input("¿Desea actualizar otro precio (s/n)?: ")

        elif opcion == 4:
            cod = input("Ingrese código de película: ")
            tit = input("Ingrese título: ")
            gen = input("Ingrese género: ")
            
            try:
                dur = int(input("Ingrese duración (minutos): "))
                cla = input("Ingrese clasificación: ")
                idi = input("Ingrese idioma: ")
                es_3d = input("¿Es 3D? (s/n): ")
                pre = int(input("Ingrese precio: "))
                cup = int(input("Ingrese cupos: "))
                
                if not validar_codigo(cod, peliculas):
                    print("Error en el código.")
                elif not validar_titulo(tit):
                    print("Error en el título.")
                elif not validar_genero(gen):
                    print("Error en el género.")
                elif not validar_duracion(dur):
                    print("Error en la duración.")
                elif not validar_clasificacion(cla):
                    print("Error en la clasificación.")
                elif not validar_idioma(idi):
                    print("Error en el idioma.")
                elif not validar_es_3d(es_3d):
                    print("Error en formato 3D.")
                elif not validar_precio(pre):
                    print("Error en el precio.")
                elif not validar_cupos(cup):
                    print("Error en los cupos.")
                else:
                    agregar_pelicula(cod, tit, gen, dur, cla, idi, es_3d, pre, cup, peliculas, cartelera)
                    print("Película agregada")
            except ValueError:
                print("Error: Duración, precio y cupos deben ser números enteros.")

        elif opcion == 5:
            cod = input("Ingrese código de película: ")
            if eliminar_pelicula(cod, peliculas, cartelera):
                print("Película eliminada")
            else:
                print("El código no existe")

        elif opcion == 6:
            print("Programa finalizado.")
            menu = False

main()