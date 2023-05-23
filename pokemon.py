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