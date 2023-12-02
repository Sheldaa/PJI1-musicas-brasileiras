import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
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
    return ' '.join(lemmatized_words)

# Aplicar a função de contagem à coluna 'Letras_lematizadas'
lyrics_data['Letras_lematizadas1'] = lyrics_data['Letras_lematizadas'].apply(count_unique_words)

# Usar CountVectorizer para criar um Bag of Words
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(lyrics_data['Letras_lematizadas1'])

# Criar um DataFrame com as palavras como colunas e as contagens como valores
bow_df = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())

# Salvar o DataFrame do Bag of Words como um novo conjunto de dados
bow_df.to_csv('bag_of_words.csv', index=False)

# Exibir o DataFrame do Bag of Words
print("Bag of Words DataFrame:")
print(bow_df)
