import pandas as pd
from collections import Counter
import spacy

# Carregar o DataFrame lyrics_data (certifique-se de substituir 'caminho/do/seu/arquivo.csv' pelo caminho correto)
lyrics_data = pd.read_csv('lyrics_data_tokenizado.csv')

# Carregar o modelo spaCy para o português
nlp = spacy.load('pt_core_news_sm')

# Função para lematizar e remover pontuações
def lemmatize_and_remove_punctuation(text):
    doc = nlp(text)
    lemmatized_words = [token.lemma_.lower() for token in doc if token.is_alpha]
    return ' '.join(lemmatized_words)

# Aplicar a função de lematização e remoção de pontuações à coluna 'Letras_tokenizadas'
lyrics_data['Letras_lematizadas'] = lyrics_data['Letras_tokenizadas'].apply(lemmatize_and_remove_punctuation)

# Salvar o novo DataFrame em um arquivo CSV (certifique-se de ajustar o nome do arquivo conforme necessário)
lyrics_data.to_csv('lyrics_data_lematizado_sem_pontuacao.csv', index=False)

# Exibir o DataFrame original e o DataFrame com lematização e remoção de pontuações
print("\nDataFrame com lematização e remoção de pontuações:")
print(lyrics_data[['Letras_lematizadas']])
