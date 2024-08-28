import requests
import argparse
import sys
import json

# Cargar configuración desde config.json
try:
    with open("config.json") as config_file:
        config = json.load(config_file)
        API_KEY = config.get("API_KEY")
        BASE_URL = config.get("BASE_URL")
except FileNotFoundError:
    print(
        "Error: No se encontró el archivo 'config.json'. Asegúrate de que exista en el directorio actual.",
        file=sys.stderr,
    )
    sys.exit(1)
except json.JSONDecodeError:
    print(
        "Error: No se pudo leer el archivo 'config.json'. Asegúrate de que esté en formato JSON válido.",
        file=sys.stderr,
    )
    sys.exit(1)


# El resto de tu código permanece igual...
def show_help():
    help_text = """
    Uso: python weather_cli.py -l <ubicación> [-f <formato>]

    Descripción:
      Obtén el clima actual para una ciudad especificada usando la API de OpenWeatherMap.

    Argumentos:
      -l, --location    Nombre de la ciudad o región para obtener el clima (obligatorio).
      -f, --format      Formato de salida (opciones: text, json, csv). Por defecto es 'text'.

    Ejemplos:
      python weather_cli.py -l "Asunción, Paraguay" -f json
      python weather_cli.py --location "Central, Paraguay" --format csv

    Formatos disponibles:
      text  - Formato por defecto, muestra la información en texto claro.
      json  - Muestra la información en formato JSON.
      csv   - Muestra la información en formato CSV.
    """
    print(help_text)
    sys.exit(0)


def get_weather(city):
    try:
        response = requests.get(f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            print(f"Error: Ubicación '{city}' no encontrada.", file=sys.stderr)
        else:
            print(f"Error HTTP ocurrido: {http_err}", file=sys.stderr)
    except Exception as err:
        print(f"Ocurrió un error: {err}", file=sys.stderr)
    sys.exit(1)


def output_weather(data, format_type):
    weather_info = {
        "ubicacion": f"{data['name']}, {data['sys']['country']}",
        "temperatura": f"{data['main']['temp']} °C",
        "descripcion": data["weather"][0]["description"],
    }

    if format_type == "json":
        print(json.dumps(weather_info, indent=2, ensure_ascii=False))
    elif format_type == "csv":
        print(
            f"ubicacion,temperatura,descripcion\n"
            f"{weather_info['ubicacion']},{weather_info['temperatura']},{weather_info['descripcion']}"
        )
    else:
        print(
            f"Clima en {weather_info['ubicacion']}:\n"
            f"Temperatura: {weather_info['temperatura']}\n"
            f"Condición: {weather_info['descripcion']}"
        )


def main():
    parser = argparse.ArgumentParser(add_help=False)  # Desactiva la ayuda automática
    parser.add_argument(
        "-l",
        "--location",
        type=str,
        required=True,
        help="Nombre de la ciudad o región para obtener el clima.",
    )
    parser.add_argument(
        "-f",
        "--format",
        type=str,
        choices=["json", "csv", "text"],
        default="text",
        help="Formato de salida: text (predeterminado), json o csv.",
    )

    try:
        args = parser.parse_args()

        weather_data = get_weather(args.location)
        output_weather(weather_data, args.format)
    except argparse.ArgumentError as e:
        print(f"Error: {e.message}", file=sys.stderr)
        print("Usa 'python weather_cli.py help' para ver más detalles.")
        sys.exit(1)
    except argparse.ArgumentTypeError as e:
        print(f"Error en el tipo de argumento: {e}", file=sys.stderr)
        print("Usa 'python weather_cli.py help' para ver más detalles.")
        sys.exit(1)
    except SystemExit as e:
        if e.code != 0:  # Solo sugerir ayuda si hubo un error
            print("Ocurrió un error al procesar los argumentos.")
            print("Usa 'python weather_cli.py help' para ver más detalles.")
        sys.exit(e.code)


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] in ["-h", "--help", "help"]:
        show_help()
    main()
