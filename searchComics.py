from marvel import Marvel
import pandas as pd
import json 


m = Marvel("e502a7076004ede33794d63e5b6eb3ab","c91c6bf2b630f402c49f99acefd60527ce3290d7")
characters = m.characters

## Buscador de personajes ingresados por el usuario

print("1.-Personaje ")
print("2.-Comic ")
filter = input("Elige tu filtro: ")

match filter:
    case "1":
        print(">Personaje")
        name = input("Ingresa el nombre del personaje: ")
        if name != "":
            all_characters = m.characters.all(nameStartsWith=name)
            for i in range(len(all_characters["data"]["results"])):
                print(all_characters["data"]["results"][i]["id"],
                all_characters["data"]["results"][i]["name"],
                all_characters["data"]["results"][i]["thumbnail"],
                all_characters["data"]["results"][i]["comics"])

            """
            json_data =json.dumps(data)
            print(json_data)

            with open('response.json', 'r') as f:
                json_data = json.load(f)
                print(json_data)
            """
        else:
            all_characters = m.characters.all(limit = 100) #Si agregamos en el limit mas de 100 la API marca un error 409
            #print(all_characters)

            for i in range(len(all_characters["data"]["results"])):
                print(all_characters["data"]["results"][i]["id"],
                all_characters["data"]["results"][i]["name"],
                all_characters["data"]["results"][i]["thumbnail"],
                all_characters["data"]["results"][i]["comics"])
    case "2":
        print(">Comic")
        name = input("Ingresa el nombre del comic: ")
        if name != "":
            all_characters = m.comics.all(title = name)
            for i in range(len(all_characters["data"]["results"])):
                print(all_characters["data"]["results"][i]["id"],
                all_characters["data"]["results"][i]["title"],
                all_characters["data"]["results"][i]["thumbnail"],
                all_characters["data"]["results"][i]["modified"])
        else:
            all_characters = m.comics.all(limit = 100)
            #print(all_characters)

            for i in range(len(all_characters["data"]["results"])):
                print(all_characters["data"]["results"][i]["id"],
                all_characters["data"]["results"][i]["title"],
                all_characters["data"]["results"][i]["thumbnail"],
                all_characters["data"]["results"][i]["modified"])
        



