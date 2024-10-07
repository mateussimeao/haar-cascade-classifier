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
    classificador = cv2.CascadeClassifier(cv2.data.haarcascades + caminho_classificador)
    cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    objetos_detectados = classificador.detectMultiScale(cinza, scaleFactor=escala, minNeighbors=vizinhos, minSize=min_tamanho)
    return objetos_detectados

def main():

    #parametros
    parametros = {
        'Rosto': [(1.1, 5)],
    }

    imagem_rosto = cv2.imread('src/app/imagem_teste.jpeg')
    if imagem_rosto is None:
        print("Erro ao carregar a imagem de rosto. Verifique o caminho.")
    else:
        for escala, vizinhos in parametros['Rosto']:
            objetos_rosto = AplicarClassificador('haarcascade_frontalface_default.xml', imagem_rosto, escala=escala, vizinhos=vizinhos)
            MostrarImagemComDeteccoes(imagem_rosto.copy(), objetos_rosto, nome=f"Rosto Detectado (escala={escala}, vizinhos={vizinhos})")
        return 0


if __name__ == "__main__":
    SystemExit(main())
