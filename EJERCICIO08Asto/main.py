from competidor import Competidor
from observador import Observador


def main():
    print("\n--- Competidor ---\n")
    competidor = Competidor(
        "Alan Astorga",
        "21070726",
        "Profesional",
        "Equipo AstoMx"
    )

    competidor.mostrar_perfil()
    print()

    competidor.ganar_puntos(70)
    competidor.perder_puntos(30)

    print("\n--- Observador ---\n")

    observador = Observador(
        "Maria Fernanda",
        "24345700",
        "Novata",
    )
    observador.ver_partida()
    observador.ver_partida()

    print()
    observador.mostrar_perfil()

if __name__ == "__main__":
    main()
