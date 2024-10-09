meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL": "Una respuesta a una broma",
            "SHEESH": "Ligera desaprobación",
            "CREEPY": "Aterrador, siniestro",
            "AGGRO": "Ponerse agresivo/enojado",
            }
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
if word in meme_dict.keys():
    # Si se encuentra la palabra, mostramos su significado  
    print(meme_dict[word])
else:
    # Si no se encuentra, indicamos que no está en el diccionario
    print("la palabra no esta en nuestro diccionario")
