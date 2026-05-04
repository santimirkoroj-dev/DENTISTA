import streamlit as st

TREATMENTS = ["Control", "Arreglo de caries", "Ortodoncia", "Extraccion"]

PACIENTES = [
    ("Ana Lopez", 101, "08:00", "Control"),
    ("Bruno Diaz", 115, "08:30", "Arreglo de caries"),
    ("Carla Perez", 122, "09:00", "Ortodoncia"),
    ("Diego Gomez", 130, "09:30", "Extraccion"),
    ("Elena Ruiz", 142, "10:00", "Control"),
    ("Facundo Arias", 150, "10:30", "Ortodoncia"),
    ("Gabriela Soto", 157, "11:00", "Arreglo de caries"),
    ("Hugo Mendez", 164, "11:30", "Ortodoncia"),
    ("Ines Castro", 175, "12:00", "Control"),
    ("Javier Molina", 181, "12:30", "Extraccion"),
    ("Karina Flores", 192, "13:00", "Arreglo de caries"),
    ("Luis Rojas", 203, "13:30", "Ortodoncia"),
    ("Maria Silva", 214, "14:00", "Control"),
    ("Nicolas Varela", 227, "14:30", "Extraccion"),
    ("Olga Nunez", 231, "15:00", "Ortodoncia"),
    ("Pablo Leon", 238, "15:30", "Control"),
    ("Quintin Bravo", 245, "16:00", "Arreglo de caries"),
    ("Rocio Vega", 251, "16:30", "Ortodoncia"),
    ("Sofia Pena", 262, "17:00", "Extraccion"),
    ("Tomas Beltran", 274, "17:30", "Control"),
    ("Ursula Diaz", 286, "18:00", "Ortodoncia"),
    ("Valentina Paredes", 290, "18:30", "Arreglo de caries"),
    ("Walter Sosa", 299, "19:00", "Control"),
]


def calcular_estadisticas(pacientes):
    total = len(pacientes)
    ortodoncia = sum(1 for _, _, _, tratamiento in pacientes if tratamiento == "Ortodoncia")
    antes_16 = sum(1 for _, _, horario, _ in pacientes if int(horario.split(":")[0]) < 16)
    porcentajes = {
        tratamiento: round(sum(1 for p in pacientes if p[3] == tratamiento) * 100 / total, 2) if total else 0
        for tratamiento in TREATMENTS
    }
    socio_mayor = max(pacientes, key=lambda p: p[1])
    primero = min(pacientes, key=lambda p: int(p[2].split(":")[0]) * 60 + int(p[2].split(":")[1]))

    return {
        "total": total,
        "conteo_ortodoncia": ortodoncia,
        "promedio_ortodoncia": round(ortodoncia / total, 2) if total else 0,
        "antes_16": antes_16,
        "porcentajes": porcentajes,
        "socio_mayor": socio_mayor,
        "primero": primero,
    }


def main():
    st.set_page_config(page_title="Dentista - Datos en memoria", layout="wide")
    st.title("Actividad del dentista")

    st.markdown("## Objetivos de la actividad")
    st.markdown(
        "- Disenar un programa que procese multiples datos estructurados.  \n"
        "- Aplicar estructuras de control y condicionales aprendidas hasta el modulo actual.  \n"
        "- Desarrollar algoritmos orientados a la recoleccion, analisis y presentacion de estadisticas.  \n"
        "- Fortalecer la capacidad de planificacion, interpretacion y sintesis de datos en problemas reales."
    )

    st.markdown("---")
    st.markdown("## Consigna")
    st.markdown(
        "Un dentista solo atiende a 23 pacientes por dia. Los datos que se registran de cada paciente son: Nombre, Numero de socio, Horario (entre 8:00 y 20:00 hs), Tratamiento realizado (Control, Arreglo de caries, Ortodoncia, Extraccion)."
    )

    st.markdown("---")
    st.subheader("Datos cargados en el codigo")
    st.dataframe(
        [
            {
                "Nombre": nombre,
                "Numero de socio": numero_socio,
                "Horario": horario,
                "Tratamiento": tratamiento,
            }
            for nombre, numero_socio, horario, tratamiento in PACIENTES
        ],
        use_container_width=True,
    )

    st.markdown("---")
    stats = calcular_estadisticas(PACIENTES)

    st.subheader("Resultados solicitados")
    st.write(f"- Promedio de pacientes que se realizan Ortodoncia: {stats['promedio_ortodoncia']} ({stats['conteo_ortodoncia']} de {stats['total']})")
    st.write(f"- Cantidad de pacientes atendidos antes de las 16:00 hs: {stats['antes_16']}")
    st.write("- Porcentaje de pacientes por tipo de tratamiento:")
    for tratamiento, porcentaje in stats["porcentajes"].items():
        st.write(f"  - {tratamiento}: {porcentaje}%")

    socio_mayor = stats["socio_mayor"]
    st.write(f"- Nombre y tratamiento del socio con el numero de afiliado mas alto: {socio_mayor[0]} - {socio_mayor[3]} (N° {socio_mayor[1]})")

    primero = stats["primero"]
    st.write(f"- Nombre y numero del socio que se atiende mas temprano: {primero[0]} - N° {primero[1]} (Horario {primero[2]})")

    st.markdown("---")
    st.caption("Los datos se guardan solo en memoria dentro de este codigo, sin usar SQLite.")


if __name__ == "__main__":
    main()
