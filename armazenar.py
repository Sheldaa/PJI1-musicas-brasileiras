import json
import pandas as pd
from collections import Counter



# Inicializar um vetor para armazenar as letras
all_lyrics = []
all_lyrics.clear()

# Função para adicionar letras de músicas de um arquivo ao vetor
def add_lyrics_from_file(file_path):
    # Carregar o conteúdo do arquivo
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Extrair apenas as letras das músicas e adicionar ao vetor
    for item in data:
       # all_lyrics.append(item['lyric'])
       lyric = item['lyric']
       if lyric not in all_lyrics:
            all_lyrics.append(lyric)
       else:
           print("já existe")
    


# Adicionar letras de músicas de diferentes arquivos
add_lyrics_from_file("lyrics1.json")  # Adiciona do arquivo lyrics.json (o original)
add_lyrics_from_file("lyrics2.json")
add_lyrics_from_file("lyrics3.json")
add_lyrics_from_file("lyrics4.json")
add_lyrics_from_file("lyrics5.json")
add_lyrics_from_file("lyrics6.json")
add_lyrics_from_file("lyrics7.json")
add_lyrics_from_file("lyrics8.json")
add_lyrics_from_file("lyrics9.json")
add_lyrics_from_file("lyrics10.json")
add_lyrics_from_file("lyrics11.json")
add_lyrics_from_file("lyrics12.json")
add_lyrics_from_file("lyrics13.json")
add_lyrics_from_file("lyrics14.json")
add_lyrics_from_file("lyrics15.json")
add_lyrics_from_file("lyrics16.json")
add_lyrics_from_file("lyrics17.json")
add_lyrics_from_file("lyrics18.json")
add_lyrics_from_file("lyrics19.json")
add_lyrics_from_file("lyrics20.json")





# Exibir ou realizar operações adicionais com o vetor 'all_lyrics'
#print(all_lyrics)


primeira_posicao = all_lyrics[1]
print("Primeira posição:", primeira_posicao)

# Tamanho do vetor
print(len(all_lyrics))

# Verificando se tem letras duplicadas
contagem = Counter(all_lyrics)
duplicatas = [letra for letra, count in contagem.items() if count > 1]

if duplicatas:
    print("Letras de música duplicadas:", duplicatas)
else:
    print("Não há letras de música duplicadas.")


# Transformando em dataset
lyrics_data = pd.DataFrame({'Letras': all_lyrics})

lyrics_data.to_csv("lyrics_data.csv", index=False)

print(lyrics_data)