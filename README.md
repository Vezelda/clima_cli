# CLI Weather Aplicacion 🌦️

Una aplicacion sencilla de consulta de API para obtener datos climaticos de cualquier ciudad y pais, en formatO Json, Texto o CSV, en este caso usamos la API de OpenWheaterMap y el lenguaje Python

## Caracteristicas

- Obtiene información meteorológica actual (temperatura y descripción) para una ciudad y un país determinados.
- Utiliza la API de codificación geográfica de OpenWeatherMap para convertir nombres de ciudades y países en coordenadas geográficas.

## Prerequisitos
- Tener instalado Python.
- Instalar requests (para poder hacer las consultas a la api usualmente luego de tener creado y activado tu entorno virtual seria con el comando: pip install requests
en la terminal)
- Una API key de [OpenWeatherMap](https://openweathermap.org/api). (te registras y tenes una key gratis)

## Instalacion

1- Creamos un entorno virtual: 
python3 -m venv nombre_de_tu_entorno

2- Activamos el entorno:
source nombre_de_tu_entorno/bin/activate

3- Instalamos dependencias, podes ejecutar en la terminal una vez que tengas creado y activado tu entorno virtual:
pip install requeriments.txt

4- Si bien, en mi codigo te dejo una key de OpenWheater, te recomiendo que lo cambies asi puedas manejar el tuyo, aqui abajo te dejo el link

```
OPENWEATHERMAP_API_KEY=your_api_key_here
```


## Uso

Para obtener el clima de una ciudad y un país específicos, ejecute el siguiente comando:
```
python3 weather_cli.py -l "Ciudad,Pais" -f formato deseado
```
Ejemplo
```
python wheater_cli.py "Asunción, Paraguay" -f csv
python wheater_cli.py "Asunción, Paraguay" -f json
python wheater_cli.py "Asunción, Paraguay" -f text
```

## Consideraciones

1- Solicitud de API: El script realiza una solicitud HTTP a la API de OpenWeatherMap para obtener los datos meteorológicos actuales de una ciudad especificada. Utiliza el nombre de la ciudad como parámetro de consulta y recibe la respuesta en formato JSON, la cual contiene información como la temperatura, la descripción del clima y la ubicación.

2- Manejo de errores: El script incluye un manejo de errores básico para gestionar situaciones como la falta de conexión a la red, nombres de ciudades inválidos, o cualquier otro problema durante la solicitud a la API. En caso de error, el script muestra un mensaje apropiado y finaliza la ejecución.

3- Formato de salida: El script permite al usuario elegir el formato de salida de la información meteorológica entre tres opciones: json, csv o text. Según el formato elegido, los datos se presentan de manera estructurada y legible en la terminal.

4- Argumentos de línea de comandos: El script utiliza el módulo argparse para manejar los argumentos de la línea de comandos, permitiendo al usuario especificar la ciudad para la cual desea obtener el clima, así como el formato de salida preferido.

# Agradecimientos

- **OpenWeatherMap** por proporcionar la API meteorológica que permite obtener datos de clima en tiempo real.

- **Requests** para simplificar las solicitudes HTTP en Python.

- **Argparse** para facilitar la gestión de argumentos de línea de comandos en el script.

- **Python** como lenguaje de programación que hace posible el desarrollo de esta herramienta.

5- Si tienes alguna duda podrias utilizar el comando:
```
python weather_cli.py help
```
para poder tener indicaciones de como ejecutar el programa

## Uso Automatizado

Ejecutar el run.sh 
en el caso que no te deje activar, aplicar en tu terminal este comando para darle los permisos: chmod +x run.sh

Este programa, crea el entorno virtual, activa eh instala automaticamente los archivos necesarios de requeriments.txt
Luego ejecuta el programa con un comando de muestra

