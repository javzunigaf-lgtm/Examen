def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opción: "))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Debe seleccionar una opción válida")
        except ValueError:
            print("Debe seleccionar una opción válida")


def cupos_genero(genero, peliculas, cartelera):
    total_cupos = 0
    genero_buscado = genero.lower()
    
    for codigo in peliculas:
        if peliculas[codigo][1].lower() == genero_buscado:
            total_cupos = total_cupos + cartelera[codigo][1]
            
    print(f"El total de cupos disponibles es: {total_cupos}")


def busqueda_precio(p_min, p_max, peliculas, cartelera):
    resultados = []
    
    for codigo in cartelera:
        precio = cartelera[codigo][0]
        cupos = cartelera[codigo][1]
        
        if p_min <= precio <= p_max and cupos > 0:
            titulo = peliculas[codigo][0]
            formato = f"{titulo}--{codigo}"
            resultados.append(formato)
            
    if len(resultados) == 0:
        print("No hay películas en ese rango de precios.")
    else:
        resultados.sort()
        print(f"Las películas encontradas son: {resultados}")


def buscar_codigo(codigo, cartelera):
    cod_buscado = codigo.upper()
    for cod in cartelera:
        if cod.upper() == cod_buscado:
            return True
    return False


def actualizar_precio(codigo, nuevo_price, peliculas, cartelera):
    if buscar_codigo(codigo, cartelera):
        cod_buscado = codigo.upper()
        for cod in cartelera:
            if cod.upper() == cod_buscado:
                cartelera[cod][0] = nuevo_price
                return True
    return False


def validar_codigo(codigo, cartelera):
    if codigo.strip() == "":
        return False
    if buscar_codigo(codigo, cartelera):
        return False
    return True

def validar_titulo(titulo):
    return titulo.strip() != ""

def validar_genero(genero):
    return genero.strip() != ""

def validar_duracion(duracion_str):
    try:
        duracion = int(duracion_str)
        return duracion > 0
    except ValueError:
        return False

def validar_clasificacion(clasificacion):
    return clasificacion == 'A' or clasificacion == 'B' or clasificacion == 'C'

def validar_idioma(idioma):
    return idioma.strip() != ""

def validar_es_3d(opcion_3d):
    return opcion_3d.lower() == 's' or opcion_3d.lower() == 'n'

def validar_precio(precio_str):
    try:
        precio = int(precio_str)
        return precio > 0
    except ValueError:
        return False

def validar_cupos(cupos_str):
    try:
        cupos = int(cupos_str)
        return cupos >= 0
    except ValueError:
        return False


def agregar_pelicula(codigo, titulo, genero, duracion, clasificacion, idioma, es_3d, precio, cupos, peliculas, cartelera):
    if buscar_codigo(codigo, cartelera):
        return False
    
    formato_3d = False
    if es_3d.lower() == 's':
        formato_3d = True
        
    peliculas[codigo] = [titulo, genero, int(duracion), clasificacion, idioma, formato_3d]
    cartelera[codigo] = [int(precio), int(cupos)]
    return True


def eliminar_pelicula(codigo, peliculas, cartelera):
    if buscar_codigo(codigo, cartelera):
        cod_buscado = codigo.upper()
        clave_real = ""
        for cod in cartelera:
            if cod.upper() == cod_buscado:
                clave_real = cod
        
        del peliculas[clave_real]
        del cartelera[clave_real]
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

    ejecutando = True
    while ejecutando:
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
                    
                    if p_min >= 0 and p_max >= 0 and p_min <= p_max:
                        busqueda_precio(p_min, p_max, peliculas, cartelera)
                        break
                    else:
                        print("Debe ingresar valores enteros válidos (mínimo menor o igual al máximo)")
                except ValueError:
                    print("Debe ingresar valores enteros")
                    
        elif opcion == 3:
            resp = 's'
            while resp.lower() == 's':
                cod = input("Ingrese código de película: ")
                
                while True:
                    try:
                        n_precio = int(input("Ingrese nuevo precio: "))
                        if n_precio > 0:
                            break
                        else:
                            print("El precio debe ser un entero positivo.")
                    except ValueError:
                        print("Debe ingresar un valor entero.")
                
                if actualizar_precio(cod, n_precio, peliculas, cartelera):
                    print("Precio actualizado")
                else:
                    print("El código no existe")
                    
                resp = input("¿Desea actualizar otro precio (s/n)?: ")
                
        elif opcion == 4:
            c = input("Ingrese código de película: ")
            t = input("Ingrese título: ")
            g = input("Ingrese género: ")
            dur = input("Ingrese duración (minutos): ")
            cl = input("Ingrese clasificación: ")
            idm = input("Ingrese idioma: ")
            es_3 = input("¿Es 3D? (s/n): ")
            pre = input("Ingrese precio: ")
            cup = input("Ingrese cupos: ")
            
            if not validar_codigo(c, cartelera):
                print("Error: Código inválido o ya existente.")
            elif not validar_titulo(t):
                print("Error: El título no puede estar vacío.")
            elif not validar_genero(g):
                print("Error: El género no puede estar vacío.")
            elif not validar_duracion(dur):
                print("Error: La duración debe ser un entero mayor a cero.")
            elif not validar_clasificacion(cl):
                print("Error: La clasificación debe ser exactamente 'A', 'B' o 'C'.")
            elif not validar_idioma(idm):
                print("Error: El idioma no puede estar vacío.")
            elif not validar_es_3d(es_3):
                print("Error: En 'Es 3D' debe ingresar 's' o 'n'.")
            elif not validar_precio(pre):
                print("Error: El precio debe ser un número entero mayor a cero.")
            elif not validar_cupos(cup):
                print("Error: Los cupos deben ser un entero mayor o igual a cero.")
            else:
                exito = agregar_pelicula(c, t, g, dur, cl, idm, es_3, pre, cup, peliculas, cartelera)
                if exito:
                    print("Película agregada")
                else:
                    print("El código ya existe")
                    
        elif opcion == 5:
            cod = input("Ingrese código de película a eliminar: ")
            if eliminar_pelicula(cod, peliculas, cartelera):
                print("Película eliminada")
            else:
                print("El código no existe")
                
        elif opcion == 6:
            print("Programa finalizado.")
            ejecutando = False

main()