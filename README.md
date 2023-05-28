# Programación de Computadores - UNAL
## Diccionarios

<table cellspacing="1" bgcolor="">
	<tr bgcolor="#252582">
		<th><b>Definición</b></th>
	</tr>
	<tr bgcolor="#e4e4ed">
		<td style="color:#141414">Un diccionario es una colección de parejas clave-valor donde los valores pueden ser recuperados principalmente por su clave. Cada pareja clave-valor en un diccionario es considerada un ítem o registro. En Python, un diccionario se escribe separando los ítems por comas (,) y entre llaves { }. Los diccionarrios son mutables.
	</tr>
</table>

**Ejemplo:** Colección clave-valor:
 + 22 : 'SSH'
 + 80 : 'HTTP'
 + 'edad' : 18
 + 'color' : 'rojo'
 + 'sopa' : 'Plato compuesto de un caldo y uno o más ingredientes sólidos cocidos'
 + 12100100 : "Juan María de los Santos"
 + 'primos' : [2, 3, 5, 7, 11, 13, 17, 19]
 + (3, 5, 7) : 105


**Ejemplo:** Diccionarios:
 + {22:'SSH', 23:'Telnet', 80:'HTTP', 3306:'MySQL'}
 + {"edad":40, "genero":'Masculino', "nombre":'Juan Salvador', "apellido":'Gaviota'}
 + {"producto":'Leche', "presentación":[900,1100,1300]}
 + {'compañia':'La Gallina Saraviada', "precio":{"grande":23000, "mediana":18000, "pequeña":12000}}

### Asignación
Un diccionario se puede asignar a una variable.
 + x = { } : Le asigna el diccionario vacío a la variable x.
 + puertos = {22:'SSH', 23:'Telnet', 80:'HTTP', 3306:'MySQL'}

## Operadores
### Indexación
Accede al valor de un ítem con la clave dada. Si no existe un ítem con la
clave dada en el diccionario se genera un error.

```python
puertos = {22:"SSH", 23:"Telnet", 80:"HTTP", 3306:"MySQL"}
protocolo = puertos[22]
print(protocolo)
```

```python
puertos[443] ### Que error genera?
```

Usando brackets también se puede adicionar/modificar elementos en el diccionario.

```python
puertos = {80:"HTTP", 23:"SMTP", 443:"HTTPS"}
print(puertos)
puertos[23] = "Telnet" # Modifica elemento
print(puertos)
puertos[110] = "POP" # Agrega elemento
print(puertos)
```

### Unión
El método update agrega ítems de un diccionario en otro.

```python
dict_ports1 = {22:"SSH", 80:"Http"}
dict_ports2 = {53:"DNS", 443:"https"}
print(dict_ports1)
dict_ports1.update(dict_ports2)
print(dict_ports1)
```

### Eliminación
El comando del permite eliminar el ítem con la clave dada.

```python
puertos = {22:"SSH", 23:"Telnet", 80:"HTTP", 3306:"MySQL"}
print(puertos)
del puertos[23] # Que susede si se intenta eliminar un item con un indice que no exista?
print(puertos)
```

### Comparación
Se usan los operadores convencionales (==, !=) para comparar diccionarios. Se mira si los diccionarios tienen los mismos ítems.

```python
a = {123:"Rojas", 87:"Rosas"} == {87:"Rosas", 123:"Rojas"}
print(a) # True
print({"Rosas":123} != {"rosas":123}) # True
b = {123:"Rosas", 87:"rojas"} == {"Rosas":123, 87:"rojas"}
print(b) # False
```

### Pertenencia
Es posible determinar si en un diccionario existe un ítem que tenga
asociada una clave. Se utiliza la palabra reservada *in*.

```python
puertos = {80:"HTTP", 23:"SMTP", 443:"HTTPS"}
if 80 in puertos: print("yes")
if 110 not in puertos: print("no")
else: print("yes")
```

Para recorrer un diccionario se utilizar el bucle *for*.

```python
# Recorre las llaves de un diccionario
dict_ports = {22:"SSH", 23:"telnet", 80:"Http"}
for key in dict_ports:
  print(key)
```

```python
# Recorre las llaves y los valores de un diccionario
dict_ports = {22:"SSH", 23:"telnet", 80:"Http"}
for k,v in dict_ports.items(): # tuplas
  print(k, "->", v)
```

## Métodos

### Dimension
La función len determina el número de ítems en un diccionario.

```python
puertos = {80:"HTTP", 23:"SMTP", 443:"HTTPS"}
print(len(puertos))
```

### Consultar 
Se puede obtener el valor de un ítem a partir de la llave con el método get. Adicionalmente, se puede decir que retornar si no se encuentra un ítem con dicha clave.

```python
dict1 = {"a":1, "b":2, "c":3}
print(dict1.get("a"))
print(dict1.get("d", "clave no encontrada."))
```

### Minimo y maximo
El método max/min obtiene la máxima/mínima clave de los ítems en el
diccionario.

```python
puertos = {80:"HTTP", 23:"SMTP", 443:"HTTPS"}
print(max(puertos))
print(min(puertos))
# Que pasa cuando las llaves no son numericas?
```

### Llaves y valores
El método keys obtiene una lista con todas las claves de los ítems de un diccionario, mientras el método values obtiene todos los valores.

```python
dict1 = {"a":1, "b":2, "c":3}
print(list(dict1.keys()))
print(list(dict1.values()))
```

### Conversión a diccionarios
El método dict permite convertir listas de listas y listas de tuplas a diccionarios.

```python
puertos = [[80, "http"], [20, "ftp"], [23, "telnet"]]
d_port = dict(puertos)
print(d_port)
puertos = [(20, "ftp"), (80, "http"), (23, "telnet")]
d_port = dict(puertos)
print(d_port)
```

### Elmininación de entradas
El método clear se usa para eliminar todo ítem de un diccionario.

```python
dict_ports = {22:"SSH", 23:"telnet", 80:"Http"}
print(dict_ports)
dict_ports.clear()
print(dict_ports)
```

### Copiar
El método copy se usa para copiar un diccionario.

```python
port = {80:"HTTP", 23:"SMTP", 443:"HTTPS"}
copy_port = port.copy()
false_copy = port
print(port)
print(copy_port)
print(false_copy)
```

## JSON (JavaScript Object Notation)
<table cellspacing="1" bgcolor="">
	<tr bgcolor="#252582">
		<th><b>Definición</b></th>
	</tr>
	<tr bgcolor="#e4e4ed">
		<td style="color:#141414">Es un estándar utilizado para el intercambio de información entre aplicaciones. Es un formato de archivo de texto que es fácil de leer tanto por humanos como por máquinas. JSON está basado estructuralmente en el lenguaje de programación JavaScript y por su definición simple, se puede usar en diferentes lenguajes de programación.
	</tr>
</table>

Un objeto JSON es un diccionario, donde para cada ítem:
 + La clave debe ser una cadena de caracteres delimitada por comillas dobles (")
 + El campo del valor puede ser un número (no se distingue entre enteros, reales u otros), un valor de verdad (en JavaScript se usan las palabras reservadas true y false), una cadena de caracteres (usando comillas dobles como delimitador), un elemento nulo (null), o una lista de estos mismos elementos o nuevamente un objeto JSON (un
diccionario con estas propiedades |definido recursivamente|).

**Ejemplos:**
```Javascript
{
	"Nombre": "Douglas",
	"Apellido": "Crockford",
	"pasatiempos": ["trotar", "bucear", "cantar"],
	"edad": 64,
	"empleado": false,
	"jefe": null,
	"hijos": [{"Nombre": "Alice", "edad": 16}, {"Nombre": "Bob", "edad": 8}]
}
```

### Diccionarios vs Archivos JSON
Diferencias: 

1. No todo diccionario en Python es un objeto JSON: Los diccionarios en Python pueden tener como claves números, cadenas delimitadas por el apóstrofe o tuplas. Los objetos JSON sólo permite cadenas de caracteres delimitadas únicamente por comillas dobles.

2. Un objeto JSON es \casi" un diccionario en Python, diccionario que usa las palabras false, true, null y no las de Python True, False, None.

3. Es claro, que muchos objetos JSON se pueden escribir directamente en Python, pero no todos y viceversa.

```Javascript
// JSON
{
	"Nombre": "Douglas",
	"Apellido": "Crockford",
	"pasatiempos": ["trotar", "bucear", "cantar"],
	"edad": 64,
	"empleado": false,
	"jefe": null,
	"hijos": [{"Nombre": "Alice", "edad": 16}, {"Nombre": "Bob", "edad": 8}]
}
```

```python
# Diccionario
{
	"Nombre": "Douglas",
	"Apellido": "Crockford",
	"pasatiempos": ["trotar", "bucear", "cantar"],
	"edad": 64,
	"empleado": False,
	"jefe": None,
	"hijos": [{"Nombre": "Alice", "edad": 16}, {"Nombre": "Bob", "edad": 8}]
}
```

### Correspondencias

<table border="1">
  <tr>
    <td><b>Python Dict</b></td>
    <td><b>JSON</b></td>
  </tr>
  <tr>
    <td>dict</td>
    <td>object</td>
  </tr>
  <tr>
    <td>tuple, list</td>
    <td>array</td>
  </tr>
  <tr>
    <td>str</td>
    <td>string</td>
  </tr>
  <tr>
    <td>int, float</td>
    <td>Number</td>
  </tr>
  <tr>
    <td>True, False</td>
    <td>true, false</td>
  </tr>
  <tr>
    <td>None</td>
    <td>null</td>
  </tr>
</table>

Para trabajar con objetos tipo JSON se importa el módulo `json`:
```python
import json
```

### Serialización
El proceso de transformar datos en series de bytes para ser enviados por una red o ser guardados como archivo se conoce como serializacion. Los archivos JSON se pueden serializar. La librera json expone el metodo *dump()* para escribir datos en un archivo.

```python
import json

# Diccionario en python
data = {
	"cientifico": {
	"nombre": "Alan Mathison Turing",
	"edad": "41"
	}
}

# Guardar archivo
writeFile = open('data_file.json', "w")
json.dump(data, writeFile)
writeFile.close()

# Alternativamente se puede
# with open("json/data_file.json", "w") as write_file:
	# json.dump(data, write_file)

# Imprimir JSON
json_string = json.dumps(data, indent = 2)
print(json_string)
```

### Deserialización
Consiste es tomar un archivo tipo JSON y convertirlo a un objeto tratable dentro de un lenguaje de programación. Es el equivalente a cargar el archivo JSON.

```python
import json

# Cargar archivo
readFile = open('data_file.json', "r")
data = json.loads(readFile)
readFile.close()

print(data)
# print(json.dumps(data, indent=2))
```

### Pretty Print
Es un módulo para imprimir de forma "bonita" un JSON en Python.

```python
import json
from pprint import pprint

# Cargar archivo
readFile = open('data_file.json', "r")
data = json.loads(readFile)
readFile.close()

pprint(data)
```

### JSON de Internet
Dado que el JSON sirve para comunicación de datos en internet, es muy comun solicitar (hacer requests) a servicios para que respondan con información en JSON. En *python* se requiere el módulo `requests`, el cual permite solicitar información a una URL (*endpoint*).  


**Ejemplo:** Pokeapi:
```python
import json
import requests

url = 'https://pokeapi.co/api/v2/pokemon/'

def buscarPokemonNum(num : int):
  print(url)
  peticion = requests.get(url+str(num))
  print(peticion.status_code)

  return json.loads(peticion.content)

if __name__ == "__main__":
  respuesta = buscarPokemonNum(1)
	# print(json.dumps(respuesta, indent=2))
	print(dict(respuesta).keys())
```

### Validación de JSON
A través de esta [herramienta](https://jsonlint.com/) se puede validar y con esta [otra](https://jsonformatter.curiousconcept.com/#) visualizar si un archivo cumple el estándar JSON.

## Reto 13
1. Desarrollar un algoritmo que imprima de manera ascendente los valores (todos del mismo tipo) de un diccionario.
2. Desarrollar una funcion que reciba dos diccionarios como parametros y los mezcle, es decir, que se construya un nuevo diccionario con las llaves de los dos diccionarios; si hay una clave repetida en ambos diccionarios, se debe asignar el valor que tenga la clave en el primer diccionario.
3. Dado el JSON:
```JSON
{
	"jadiazcoronado":{
		"nombres": "Juan Antonio",
		"apellidos": "Daz Coronado",
		"edad":19,
		"colombiano":true,
		"deportes":["Futbol","Ajedrez","Gimnasia"]
	},
	"dmlunasol":{
		"nombres": "Dorotea Maritza",
		"apellidos": "Luna Sol",
		"edad":25,
		"colombiano":false,
		"deportes":["Baloncesto","Ajedrez","Gimnasia"]
	}
}
```
 Cree un programa que lea de un archivo con dicho JSON y: 
 - Imprima los nombres completos (nombre y apellidos) de las personas que practican el deporte ingresado por el usuario.
 - Imprima los nombres completos (nombre y apellidos) de las personas que esten en un rango de edades dado por el usuario.

4. El siguiente código contiene un JSON con el pronostivo detallado del clima para 8 días:

```python
import json

# Cargar archivo
jsonString = '''
{\"dt\": {\"0\": 1685116800, \"1\": 1685203200, \"2\": 1685289600, \"3\": 1685376000, \"4\": 1685462400, \"5\": 1685548800, \"6\": 1685635200, \"7\": 1685721600}, \"sunrise\": {\"0\": 1685097348, \"1\": 1685183745, \"2\": 1685270143, \"3\": 1685356542, \"4\": 1685442942, \"5\": 1685529342, \"6\": 1685615743, \"7\": 1685702145}, \"sunset\": {\"0\": 1685143042, \"1\": 1685229458, \"2\": 1685315875, \"3\": 1685402291, \"4\": 1685488708, \"5\": 1685575124, \"6\": 1685661541, \"7\": 1685747958}, \"moonrise\": {\"0\": 1685118300, \"1\": 1685207460, \"2\": 1685296620, \"3\": 1685385720, \"4\": 1685474880, \"5\": 1685564220, \"6\": 1685653740, \"7\": 1685743500}, \"moonset\": {\"0\": 0, \"1\": 1685164320, \"2\": 1685253000, \"3\": 1685341560, \"4\": 1685430120, \"5\": 1685518740, \"6\": 1685607600, \"7\": 1685696640}, \"moon_phase\": {\"0\": 0.22, \"1\": 0.25, \"2\": 0.28, \"3\": 0.31, \"4\": 0.35, \"5\": 0.38, \"6\": 0.41, \"7\": 0.45}, \"pressure\": {\"0\": 1011, \"1\": 1012, \"2\": 1012, \"3\": 1012, \"4\": 1012, \"5\": 1012, \"6\": 1012, \"7\": 1011}, \"humidity\": {\"0\": 85, \"1\": 61, \"2\": 68, \"3\": 74, \"4\": 84, \"5\": 66, \"6\": 81, \"7\": 82}, \"dew_point\": {\"0\": 23.93, \"1\": 22.5, \"2\": 23.67, \"3\": 23.35, \"4\": 24.22, \"5\": 22.73, \"6\": 23.18, \"7\": 22.93}, \"velViento\": {\"0\": 3.56, \"1\": 5.07, \"2\": 5.38, \"3\": 3.95, \"4\": 4.74, \"5\": 3.75, \"6\": 4.08, \"7\": 5.94}, \"dirViento\": {\"0\": 188, \"1\": 14, \"2\": 21, \"3\": 23, \"4\": 40, \"5\": 330, \"6\": 176, \"7\": 168}, \"wind_gust\": {\"0\": 6.47, \"1\": 8.86, \"2\": 8.95, \"3\": 6.12, \"4\": 7.17, \"5\": 5.4, \"6\": 5.13, \"7\": 9.67}, \"weather\": {\"0\": [{\"id\": 501, \"main\": \"Rain\", \"description\": \"lluvia moderada\", \"icon\": \"10d\"}], \"1\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"2\": [{\"id\": 501, \"main\": \"Rain\", \"description\": \"lluvia moderada\", \"icon\": \"10d\"}], \"3\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"4\": [{\"id\": 501, \"main\": \"Rain\", \"description\": \"lluvia moderada\", \"icon\": \"10d\"}], \"5\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"6\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"7\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}]}, \"clouds\": {\"0\": 100, \"1\": 82, \"2\": 99, \"3\": 100, \"4\": 100, \"5\": 59, \"6\": 100, \"7\": 100}, \"pop\": {\"0\": 1.0, \"1\": 0.65, \"2\": 0.98, \"3\": 0.86, \"4\": 1.0, \"5\": 0.62, \"6\": 0.93, \"7\": 0.95}, \"prcp\": {\"0\": 40.0, \"1\": 1.65, \"2\": 14.01, \"3\": 5.07, \"4\": 16.55, \"5\": 2.17, \"6\": 2.77, \"7\": 1.73}, \"uvi\": {\"0\": 10.14, \"1\": 12.78, \"2\": 12.73, \"3\": 8.44, \"4\": 0.59, \"5\": 1.0, \"6\": 1.0, \"7\": 1.0}, \"temp.day\": {\"0\": 26.62, \"1\": 30.95, \"2\": 30.17, \"3\": 28.37, \"4\": 27.22, \"5\": 29.78, \"6\": 26.83, \"7\": 26.36}, \"tmpMin\": {\"0\": 25.64, \"1\": 24.64, \"2\": 25.84, \"3\": 25.56, \"4\": 25.72, \"5\": 24.86, \"6\": 25.96, \"7\": 25.47}, \"tmpMax\": {\"0\": 27.16, \"1\": 31.1, \"2\": 30.2, \"3\": 29.5, \"4\": 28.87, \"5\": 29.78, \"6\": 28.96, \"7\": 28.25}, \"temp.night\": {\"0\": 25.67, \"1\": 27.39, \"2\": 26.24, \"3\": 27.2, \"4\": 25.92, \"5\": 27.14, \"6\": 26.56, \"7\": 25.66}, \"temp.eve\": {\"0\": 25.91, \"1\": 28.73, \"2\": 27.42, \"3\": 28.27, \"4\": 27.94, \"5\": 29.29, \"6\": 28.96, \"7\": 28.12}, \"temp.morn\": {\"0\": 26.5, \"1\": 24.64, \"2\": 26.13, \"3\": 25.72, \"4\": 26.04, \"5\": 24.86, \"6\": 25.98, \"7\": 25.57}, \"feels_like.day\": {\"0\": 26.62, \"1\": 34.99, \"2\": 34.96, \"3\": 32.03, \"4\": 30.67, \"5\": 33.62, \"6\": 29.45, \"7\": 26.36}, \"feels_like.night\": {\"0\": 26.56, \"1\": 30.98, \"2\": 26.24, \"3\": 30.62, \"4\": 26.84, \"5\": 30.16, \"6\": 26.56, \"7\": 26.45}, \"feels_like.eve\": {\"0\": 26.85, \"1\": 32.49, \"2\": 30.94, \"3\": 31.8, \"4\": 31.51, \"5\": 33.17, \"6\": 32.64, \"7\": 31.18}, \"feels_like.morn\": {\"0\": 26.5, \"1\": 25.48, \"2\": 26.13, \"3\": 26.62, \"4\": 26.04, \"5\": 25.73, \"6\": 25.98, \"7\": 26.4}, \"date\": {\"0\": 1685098800000, \"1\": 1685185200000, \"2\": 1685271600000, \"3\": 1685358000000, \"4\": 1685444400000, \"5\": 1685530800000, \"6\": 1685617200000, \"7\": 1685703600000}, \"main\": {\"0\": \"Rain\", \"1\": \"Rain\", \"2\": \"Rain\", \"3\": \"Rain\", \"4\": \"Rain\", \"5\": \"Rain\", \"6\": \"Rain\", \"7\": \"Rain\"}, \"description\": {\"0\": \"lluvia moderada\", \"1\": \"lluvia ligera\", \"2\": \"lluvia moderada\", \"3\": \"lluvia ligera\", \"4\": \"lluvia moderada\", \"5\": \"lluvia ligera\", \"6\": \"lluvia ligera\", \"7\": \"lluvia ligera\"}, \"icono\": {\"0\": \"10d\", \"1\": \"10d\", \"2\": \"10d\", \"3\": \"10d\", \"4\": \"10d\", \"5\": \"10d\", \"6\": \"10d\", \"7\": \"10d\"}, \"alertPrecip\": {\"0\": \"X\", \"1\": \"-\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"alertAlertas\": {\"0\": \"-\", \"1\": \"-\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"alertVelViento\": {\"0\": \"-\", \"1\": \"-\", \"2\": \"X\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"alertTmpMax\": {\"0\": \"-\", \"1\": \"-\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"X\", \"6\": \"-\", \"7\": \"-\"}, \"alertTmpMin\": {\"0\": \"-\", \"1\": \"X\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"recomendaciones\": {\"lluvias\": \"Realice una revisi\\u00f3n y limpieza a la red de desague y canales existentes ENTER8 Cuente con una estaci\\u00f3n de bombeo, que debe estar ubicada en el punto m\\u00e1s bajo del predio. Aseg\\u00farese de encender y probar el sistema de bombeo al menos una vez al mes y hacer un mantenimiento mensual al equipo de bombeoENTER8 Los productos alojados en zonas de almacenamiento deben mantenersen sobre estibas - estanterias, con el fin de que no entren en contacto directo con el agua.\", \"vientos\": \"-\", \"temperatura\": \"-\"}}
'''
data = json.loads(jsonString)
```

Revise los campos: 'alertAlertas', 'alertPrecip', 'alertTmpMax', 'alertTmpMin', 'alertVelViento'. Para cada uno identifique si se presentan alertas ({0: x} indica que el día 0 habra un fenomeno de la alerta en cuestión, {1:"-"} indica que no habrá ningun fenomeno climatico). En caso que se presente una alerta obtenga la fecha del campo 'dt' ([aquí](https://stackoverflow.com/questions/3682748/converting-unix-timestamp-string-to-readable-date) pueden revisar como se convierte de UTC a fecha), así como los parametros relevantes del evento (e.g. si es un fenomeno de lluvias, busqye el nivel de lluvia, si es vientos, la velocidad del viuento). Al final deberá imprimir las fechas de alerta, el tipo de alerta y las variables asociadas.

5. A través de un programa conectese a al menos 3 [API's ](https://apipheny.io/free-api/), obtenga el JSON, imprimalo y extraiga los pares de llave : valor.





