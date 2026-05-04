# DENTISTA

Aplicación web desarrollada en Python con Streamlit para gestionar el registro de pacientes de un dentista.

## Características

- Permite almacenar datos de hasta 23 pacientes por día.
- Cada paciente incluye:
  - Nombre
  - Número de socio
  - Horario (entre 8:00 y 20:00)
  - Tratamiento realizado (Control, Arreglo de caries, Ortodoncia, Extracción)
- Calcula las estadísticas solicitadas por la consigna:
  - Promedio de pacientes que se realizan ortodoncia
  - Cantidad de pacientes atendidos antes de las 16:00
  - Porcentaje de pacientes por tipo de tratamiento
  - Nombre y tratamiento del socio con el número de afiliado más alto
  - Nombre y número del socio que se atiende más temprano

## Ejecutar la app

```bash
python -m streamlit run app.py
```
