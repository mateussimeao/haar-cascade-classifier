import cv2
import matplotlib.pyplot as plt

#Plotar imagem
def MostrarImagemComDeteccoes(imagem, objetos_detectados, cor=(0, 255, 0), nome="Imagem"):
    for (x, y, w, h) in objetos_detectados:
        cv2.rectangle(imagem, (x, y), (x + w, y + h), cor, 2)
    plt.figure(figsize=(10, 6))
    plt.imshow(cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB))
    plt.title(nome)
    plt.axis("off")
    plt.show()

#Aplicar Haar Cascade
def AplicarClassificador(caminho_classificador, imagem, escala=1.1, vizinhos=5, min_tamanho=(30, 30)):
    classificador = cv2.CascadeClassifier(caminho_classificador)
    if classificador.empty():
        raise ValueError(f"Erro ao carregar o classificador XML: {caminho_classificador}")
    
    cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    objetos_detectados = classificador.detectMultiScale(cinza, scaleFactor=escala, minNeighbors=vizinhos, minSize=min_tamanho)
    return objetos_detectados

#Parâmetros
parametros = {
    'Rosto': [(1.1, 5)],
}

#Lista de imagens
imagens = [
    {'nome': 'imagem_teste.jpeg', 'caminho': 'src/app/imagem_teste.jpeg'},
    {'nome': 'imagem_teste2.jpg', 'caminho': 'src/app/imagem_teste2.jpg'}
]

xmlfile = 'src/app/myfacedetector.xml'

#Processar as imagens
for imagem_info in imagens:
    imagem_rosto = cv2.imread(imagem_info['caminho'])
    
    if imagem_rosto is None:
        print(f"Erro ao carregar a imagem: {imagem_info['caminho']}. Verifique o caminho.")
    else:
        try:
            for escala, vizinhos in parametros['Rosto']:
                objetos_rosto = AplicarClassificador(xmlfile, imagem_rosto, escala=escala, vizinhos=vizinhos)
                MostrarImagemComDeteccoes(imagem_rosto.copy(), objetos_rosto, nome=f"{imagem_info['nome']} - Rosto Detectado (escala={escala}, vizinhos={vizinhos})")
        except ValueError as e:
            print(e)
