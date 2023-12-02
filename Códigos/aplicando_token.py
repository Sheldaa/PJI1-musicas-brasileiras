import pandas as pd
from nltk.tokenize import word_tokenize

# Certifique-se de baixar o modelo de tokenização da NLTK na primeira execução
import nltk
nltk.download('punkt')

# Carregar o DataFrame lyrics_data (certifique-se de substituir 'caminho/do/seu/arquivo.csv' pelo caminho correto)
lyrics_data = pd.read_csv('lyrics_data_sem_stopwords_pontuacao.csv')

# Aplicar tokenização à coluna 'Letras'
lyrics_data['Letras_tokenizadas'] = lyrics_data['Letras_sem_stopwords_pontuacao'].apply(word_tokenize)

# Salvar o novo DataFrame em um arquivo CSV (certifique-se de ajustar o nome do arquivo conforme necessário)
lyrics_data.to_csv('lyrics_data_tokenizado.csv', index=False)

# Exibir o DataFrame tokenizado
print("\nDataFrame com tokenização aplicada:")
print(lyrics_data[['Letras_tokenizadas']])
