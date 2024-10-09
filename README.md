# Classificador Haar-Cascade para detecção de Rostos
## Daniel Andre Marinho e Mateus Simeão

Este projeto implementa um **classificador Haar-Cascade** para **detecção de rostos**, baseado no tutorial disponível em [Tutorial de Classificadores Haar-Like](https://github.com/felipecbarelli/livro-visao-computacional/blob/master/tutoriais/creating-a-cascade-of-haar-like-classifiers.pdf). O classificador é treinado para detectar rostos em imagens e foi aplicado utilizando o **OpenCV** para o processamento das imagens e a detecção.
A interface gráfica foi implementada em **Angular** para permitir a interação do usuário com o sistema através de um frontend.

### Treinamento
- O treinamento foi realizado seguindo as instruções [Tutorial](https://github.com/felipecbarelli/livro-visao-computacional/blob/master/tutoriais/creating-a-cascade-of-haar-like-classifiers.pdf) disponibilizado como material para desenvolvimento do projeto.
- Foram utilizadas imagens positivas de rostos e imagens negativas de ambientes aleatórios em preto e branco.
- O arquivo resultante do classificador foi salvo como o XML [myfacedetector.xml](https://github.com/mateussimeao/haar-cascade-classifier/blob/main/backend/assets/myfacedetector.xml), que será utilizado posteriormente para realizar as detecções.

### Aplicação
- O classificador treinado é utilizado através de uma [aplicação backend Flask em python do **OpenCV**](https://github.com/mateussimeao/haar-cascade-classifier/blob/main/backend/haar-training.py), processando a imagem em tom de cinza e realizando a detecção de rostos através das funções AplicarClassificador() e MostrarImagemComDeteccoes().

### Exibição dos Resultados
- Uma interface front-end foi desenvolvida em **Angular** para permitir que o usuário carregue imagens e visualize os rostos detectados.
- A interação com o back-end é feita por meio de chamadas HTTP, onde as imagens processadas são enviadas para o servidor local e retornadas com as detecções visíveis.

- Para executar o classificador é nécessario acessar a pasta de frontend e executar a aplicação.
- `cd frontend`
- `ng serve`
- Em seguida a partir do diretório raiz do repositório deve ser acessado o backend e executar o arquivo [haar-training.py](https://github.com/mateussimeao/haar-cascade-classifier/blob/main/backend/haar-training.py).
- `cd backend`


#### Demonstração da aplicação:
![Demo](backend/assets/demonstracao.gif)