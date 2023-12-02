import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import nltk

nltk.download('stopwords')
nltk.download('punkt')

const_words = ['ti','tô','mim','tão','tanto','de', 'a', 'o', 'que', 'e', 'do', 'da', 'em', 'um', 'para', 'e', 'com', 'nao', 'uma', 'os', 'no', 'se', 'na', 'por', 'mais', 'as', 'dos', 'como', 'mas', 'foi', 'ao', 'ele', 'das', 'tem', 'a', 'seu', 'sua', 'ou', 'ser', 'quando', 'muito', 'ha', 'nos', 'ja', 'esta', 'eu', 'tambem', 'so', 'pelo', 'pela', 'ate', 'isso', 'ela', 'entre', 'era', 'depois', 'sem', 'mesmo', 'aos', 'ter', 'seus', 'quem', 'nas', 'me', 'esse', 'eles', 'estao', 'voce', 'tinha', 'foram', 'essa', 'num', 'nem', 'suas', 'meu', 'as', 'minha', 'tem', 'numa', 'pelos', 'elas', 'havia', 'seja', 'qual', 'sera', 'nos', 'tenho', 'lhe', 'deles', 'essas', 'esses', 'pelas', 'este', 'fosse', 'dele', 'tu', 'te', 'voces', 'vos', 'lhes', 'meus', 'minhas', 'teu', 'tua', 'teus', 'tuas', 'nosso', 'nossa', 'nossos', 'nossas', 'dela', 'delas', 'esta', 'estes', 'estas', 'aquele', 'aquela', 'aqueles', 'aquelas', 'isto', 'aquilo', 'estou', 'esta', 'estamos', 'estao', 'estive', 'esteve', 'estivemos', 'estiveram', 'estava', 'estavamos', 'estavam', 'estivera', 'estiveramos', 'esteja', 'estejamos', 'estejam', 'estivesse', 'estivessemos', 'estivessem', 'estiver', 'estivermos', 'estiverem', 'hei', 'ha', 'havemos', 'hao', 'houve', 'houvemos', 'houveram', 'houvera', 'houveramos', 'haja', 'hajamos', 'hajam', 'houvesse', 'houvessemos', 'houvessem', 'houver', 'houvermos', 'houverem', 'houverei']

lyrics_data = pd.read_csv('lyrics_data.csv')

# Função para remover stopwords e pontuações de uma string
def remove_stopwords_and_punctuation(text):
    stop_words = set(const_words + stopwords.words('portuguese'))
    words = word_tokenize(text)
    filtered_words = [word.lower() for word in words if word.lower() not in stop_words and word.lower() not in string.punctuation]
    return ' '.join(filtered_words)

# Aplicar a função de remoção de stopwords e pontuações à coluna 'Letras'
lyrics_data['Letras_sem_stopwords_pontuacao'] = lyrics_data['Letras'].apply(remove_stopwords_and_punctuation)

# Salvar o novo DataFrame em um arquivo CSV (certifique-se de ajustar o nome do arquivo conforme necessário)
lyrics_data.to_csv('lyrics_data_sem_stopwords_pontuacao.csv', index=False)

# Exibir o DataFrame original e o DataFrame com stopwords e pontuações removidas
print("DataFrame original:")
print(lyrics_data[['Letras']])

print("\nDataFrame com stopwords e pontuações removidas:")
print(lyrics_data[['Letras_sem_stopwords_pontuacao']])

