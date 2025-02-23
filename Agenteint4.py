import random

def recomendar_pelicula():
    # Diccionario de películas organizadas por género
    peliculas = {
        "acción": ["Mad Max: Fury Road", "Die Hard", "The Dark Knight", "John Wick"],
        "comedia": ["The Hangover", "Superbad", "Step Brothers", "Monty Python and the Holy Grail"],
        "drama": ["Forrest Gump", "The Shawshank Redemption", "The Pursuit of Happyness", "A Beautiful Mind"],
        "ciencia ficción": ["Inception", "The Matrix", "Interstellar", "Blade Runner 2049"],
        "terror": ["The Conjuring", "A Nightmare on Elm Street", "The Exorcist", "Get Out"],
        "romántica": ["The Notebook", "Pride and Prejudice", "La La Land", "Titanic"]
    }

    # Solicitar al usuario su género favorito
    print("Géneros disponibles: acción, comedia, drama, ciencia ficción, terror, romántica.")
    genero = input("¿Cuál es tu género favorito? ").lower()

    # Verificar si el género ingresado es válido
    if genero in peliculas:
        # Elegir una película aleatoria del género seleccionado
        pelicula_recomendada = random.choice(peliculas[genero])
        print(f"\n¡Te recomiendo ver la película: {pelicula_recomendada}!")
    else:
        print("\nLo siento, no tenemos recomendaciones para ese género. Por favor, elige uno de los géneros disponibles.")

# Ejecutar el agente de recomendación
recomendar_pelicula()
