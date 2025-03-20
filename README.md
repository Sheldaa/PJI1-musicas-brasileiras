# 🎵 Projeto Integrador I - Músicas brasileiras
Este repositório tem como objetivo a criação e organização de um dataset voltado para o reconhecimento de emoções em letras de músicas. O conjunto de dados estruturado aqui servirá como base para futuras análises e modelagens, possibilitando estudos na interseção entre processamento de linguagem natural (NLP) e sentimentos musicais.
## Objetivos
* Compreensão das emoções base e das ferramentas disponíveis.
* Desenvolvimento de código para extração e armazenamento das letras.
* Estabelecimento da compreensão e organização base para o projeto.
* Inicialização das extrações das letras.
* Realização de testes preliminares para compreensão das ferramentas.
## Processo de Construção do Dataset
1. Seleção de Gênero e Bandas
   * Gênero escolhido: Rock, com ênfase em Rock Alternativo/indie e Rock Pop.
   * Escolha de 20 bandas representativas.
2. Divisão de Bandas por Gênero e Época
   * Organização das bandas selecionadas considerando o gênero musical e a época de atuação.
3. Extração das Letras
   * Implementação de código para extrair as letras das músicas das 20 bandas selecionadas.
4. Pré-processamento de Dados
   * Remoção de StopWords.
   * Lematização.
   * Aplicação de Token.
   * Exploração dos dados para compreensão da estrutura.
5. Montagem do Dataset
   * Inicialização da montagem do dataset manualmente.
   * Registro de informações como nome da música, ano, álbum e banda por meio de pesquisas em plataformas de música (Letras, Vagalume, Spotify).
6. Utilização da Plataforma Letras
   * Extração específica das letras por meio da plataforma Letras para enriquecer o dataset.
## Informações sobre os arquivos deste repositório
1. **Pasta Datasets** 

O dataset em questão trata-se de um conjunto de músicas brasileiras do estilo rock/indie/pop, algumas lançadas antes dos anos 2000 e outras lançados depois dos anos 2000. Aqui estão algumas informações:
* Arquivo BD_bandas: Dataset principal com 330 músicas e contendo as colunas: músicas, ano, albuns e bandas.
* Arquivo lyrics_data: Possui todas as letras das músicas.
* Arquivo lyrics_data_lematizado_sem_pontuacao: possui as colunas Letras,Letras_sem_stopwords_pontuacao,Letras_tokenizadas e Letras_lematizadas.
* Arquivo word_ranking: possui as palavras e a contagem delas em ordem decrescente.
* Arquivo bag_of_words: possui a coleção de palavras.
2. **Pasta Letras**
  * Esta pasta contém as letras extraídas das 20 bandas com todos os arquivos no formato .json.
3. **Pasta Códigos**
    * coleta.py: arquivo com o código principal para a coleta das letras de músicas.
    * armazenar.py: arquivo que contém o código utilizado para armazenar todas as letras em um só arquivo .csv.
    * remover_stopwords.py: arquivo com o código utilizado para remover stop words e pontuação.
    * lematizar.py: arquivo com o código utilizado para aplicar lematização.
    * aplicando_token.py: arquivo com o código em que foi feita a aplicação de token.
    * contagem.py: arquivo com o código utilizado para gerar o ranking de palavras.
    * bag_words.py: arquivo com o código utilizado para gerar a coleção de palavras.
## Análises
1. **Proporção de Músicas por Bandas**
   ![Figure_1](https://github.com/Sheldaa/Projeto-Integrador-I/assets/128556185/f8de284c-099a-4882-b746-d76402737c27)
2. **TOP 10 Palavras**
   ![Figure_2](https://github.com/Sheldaa/Projeto-Integrador-I/assets/128556185/fcd6e162-67ba-45bd-bb89-4f110f5fe153)


## Próximos passos
Este conjunto de dados montado servirá como base para análises mais aprofundadas no reconhecimento de emoções nas letras de músicas. Ao decorrer dos próximos trabalhos serão implementadas técnicas de processamento de linguagem natural para alcançar os objetivos finais do projeto.

