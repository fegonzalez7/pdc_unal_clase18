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

Para trabajar con objetos tipo JSON se importa el módulo `json`:
```python
import json
```

### Serialización

### Deserialización


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




