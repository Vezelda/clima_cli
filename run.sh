#!/bin/bash

# Mensaje inicial
echo "Iniciando el script de configuración y prueba..."
echo

# Crear el entorno virtual si no existe
if [ ! -d "wheatervenv" ]; then
    echo "Creando entorno virtual..."
    python3 -m venv wheatervenv
    echo "Entorno virtual creado."
else
    echo "El entorno virtual ya existe."
fi

echo
echo "--------------------------------------------------"
echo

# Activar el entorno virtual
echo "Activando el entorno virtual..."
source wheatervenv/bin/activate
echo "Entorno virtual activado."

echo
echo "--------------------------------------------------"
echo

# Verificar si requirements.txt existe
if [ -f "requirements.txt" ]; then
    # Comprobar si los paquetes están instalados
    echo "Verificando las dependencias..."
    REQ_INSTALLED=true

    # Leer el archivo requirements.txt
    while IFS= read -r line; do
        # Ignorar líneas vacías y comentarios
        if [[ -z "$line" || "$line" == \#* ]]; then
            continue
        fi

        PACKAGE=$(echo "$line" | cut -d'=' -f 1)  # Obtener el nombre del paquete sin versión

        # Comprobar si el paquete está instalado
        if ! pip show "$PACKAGE" > /dev/null 2>&1; then
            echo "Paquete $PACKAGE no está instalado. Instalando..."
            REQ_INSTALLED=false
            break
        fi
    done < "requirements.txt"

    # Si algún paquete no está instalado, proceder a la instalación
    if [ "$REQ_INSTALLED" = true ]; then
        echo "Todas las dependencias ya están instaladas."
    else
        echo "Instalando dependencias..."
        pip install -r requirements.txt
        echo "Dependencias instaladas."
    fi
else
    echo "No se encontró requirements.txt. Por favor, verifica el archivo."
    deactivate
    exit 1
fi

echo
echo "--------------------------------------------------"
echo

# Ejecutar el programa con parámetros de prueba
echo "Ejecutando el programa con parámetros de prueba..."
python weather_cli.py -l "Asunción, Paraguay" -f text
echo "Programa ejecutado."

echo
echo "--------------------------------------------------"
echo

# Desactivar el entorno virtual
echo "Desactivando el entorno virtual..."
deactivate
echo "Entorno virtual desactivado."

echo
echo "--------------------------------------------------"
echo

# Mensaje final
echo "Proceso completo."
