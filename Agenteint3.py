def diagnostico_sistema_experto():
    print("Bienvenido al Sistema Experto de Diagnóstico Básico.")
    print("Por favor, ingresa los siguientes síntomas para obtener un diagnóstico.")

    # Ingresar síntomas del usuario
    tos = input("¿Tienes tos? (sí/no): ").lower() == "sí"
    fiebre = input("¿Tienes fiebre? (sí/no): ").lower() == "sí"
    dolor_cabeza = input("¿Tienes dolor de cabeza? (sí/no): ").lower() == "sí"
    dificultad_respiratoria = input("¿Tienes dificultad para respirar? (sí/no): ").lower() == "sí"
    fatiga = input("¿Tienes fatiga o cansancio extremo? (sí/no): ").lower() == "sí"

    # Diagnóstico basado en las reglas
    if tos and fiebre and dolor_cabeza and dificultad_respiratoria:
        print("\nDiagnóstico: Podrías tener una infección respiratoria o gripe grave. Es recomendable consultar a un médico inmediatamente.")
    elif tos and fiebre:
        print("\nDiagnóstico: Puede ser un resfriado o gripe común. Descanso y líquidos son recomendados.")
    elif dolor_cabeza and fatiga:
        print("\nDiagnóstico: Podrías estar experimentando estrés o fatiga. Asegúrate de descansar lo suficiente.")
    elif dificultad_respiratoria:
        print("\nDiagnóstico: La dificultad para respirar podría ser un signo de una condición más seria. Consulta con un médico.")
    elif fiebre:
        print("\nDiagnóstico: Podrías estar teniendo fiebre debido a una infección leve. Descanso y monitoreo son recomendados.")
    else:
        print("\nDiagnóstico: No parece haber síntomas graves. Mantén una buena salud y descanso si es necesario.")

# Ejecutar el sistema experto
diagnostico_sistema_experto()
