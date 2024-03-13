# Importa
from get_module import request_get
import templates as t

# Paso 4: Función para construir el HTML
def build_html(url):
    # Realiza una solicitud GET a la URL proporcionada
    response = request_get(url)
    # Inicializa una cadena vacía para almacenar el contenido HTML generado
    texto = ''
    # Itera sobre los resultados de la respuesta
    for resultados in response:
        ...

    return t.html_template.substitute(body=texto)  # Devuelve el HTML completo utilizando la plantilla html_template

if __name__ == '__main__':
    # Paso 5: Construye el HTML y escribe en un archivo
    ...
