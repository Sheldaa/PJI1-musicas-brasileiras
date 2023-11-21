import pandas as pd
from collections import Counter
import spacy

# Carregar o DataFrame lyrics_data (certifique-se de substituir 'caminho/do/seu/arquivo.csv' pelo caminho correto)
lyrics_data = pd.read_csv('lyrics_data_lematizado_sem_pontuacao.csv')

# Carregar o modelo spaCy para o português
nlp = spacy.load('pt_core_news_sm')

# Função para tokenizar e contar palavras
def count_unique_words(text):
    doc = nlp(text)
    lemmatized_words = [token.lemma_.lower() for token in doc if token.is_alpha]
    return Counter(lemmatized_words)

# Aplicar a função de contagem à coluna 'Letras_lematizadas'
lyrics_data['Contagem_Palavras'] = lyrics_data['Letras_lematizadas'].apply(count_unique_words)

# Calcular a contagem total de palavras no conjunto de dados
total_word_count = sum(lyrics_data['Contagem_Palavras'], Counter())

# Criar um DataFrame para o ranking de palavras
word_ranking = pd.DataFrame(total_word_count.items(), columns=['Palavra', 'Contagem'])

# Classificar o DataFrame por contagem de palavras em ordem decrescente
word_ranking = word_ranking.sort_values(by='Contagem', ascending=False)

# Salvar o ranking de palavras como um novo conjunto de dados sem incluir a coluna 'Contagem_Palavras'
word_ranking.to_csv('word_ranking.csv', index=False)

# Exibir o ranking de palavras
print("Ranking de Palavras:")
print(word_ranking)
