import json


with open("myfile.json", "r") as json_file:
    ourjson = json.load(json_file)


token = ourjson.get("access_token", "no se encontro el token")
tiempo = ourjson.get("expires_in", "no se encontro el tiempo")


print(f"token {token}")
print(f"tiempo restante {tiempo} segundos")
