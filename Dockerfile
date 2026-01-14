# 1. Usar una imagen oficial de Python como base
FROM python:3.11-slim

# 2. Establecer el directorio de trabajo dentro del contenedor
WORKDIR /home/2asir/Escritorio/Curso/IAW/ud3_jenkins/proyecto/parte_1/

# 4. Copiar el resto del código de tu aplicación
COPY . .

# 5. Comando para ejecutar tu script
CMD ["python", "examenFernando.py"]
