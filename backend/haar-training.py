import cv2
import matplotlib.pyplot as plt
from flask import Flask, jsonify, send_file, request
from flask_cors import CORS
import os
import tempfile

app = Flask(__name__)
CORS(app)

# Plotar imagem
def MostrarImagemComDeteccoes(imagem, objetos_detectados, cor=(0, 255, 0), nome="Imagem"):
    for (x, y, w, h) in objetos_detectados:
        cv2.rectangle(imagem, (x, y), (x + w, y + h), cor, 2)
    # Salva a imagem resultante
    cv2.imwrite(os.path.join(tempfile.gettempdir(), 'image_result.png'), imagem)

# Aplicar Haar Cascade
def AplicarClassificador(caminho_classificador, imagem, escala=1.1, vizinhos=5, min_tamanho=(30, 30)):
    classificador = cv2.CascadeClassifier(caminho_classificador)
    if classificador.empty():
        raise ValueError(f"Erro ao carregar o classificador XML: {caminho_classificador}")

    cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    objetos_detectados = classificador.detectMultiScale(cinza, scaleFactor=escala, minNeighbors=vizinhos, minSize=min_tamanho)
    return objetos_detectados

@app.route('/upload_image', methods=['POST'])
def upload_image():
    # Verificar se o arquivo de imagem foi enviado na requisição
    if 'image' not in request.files:
        return jsonify({"error": "Nenhuma imagem foi enviada."}), 400
    elif 'choice' not in request.values: 
        return jsonify({"error": "Nenhuma opção de detecção escolhida.."}), 400
    
    file = request.files['image']
    choice = request.values['choice']
    
    # Salvar o arquivo temporariamente
    temp_dir = tempfile.gettempdir()
    image_path = os.path.join(temp_dir, file.filename)
    file.save(image_path)

    # Carregar e processar a imagem
    imagem_rosto = cv2.imread(image_path)
    if imagem_rosto is None:
        return jsonify({"error": "Erro ao carregar a imagem."}), 500

    parametros = {
        'Rosto': [(1.1, 5)],
    }
    if choice == "Face":
        xmlfile = 'backend/assets/myfacedetector.xml'
    elif choice == "Eyes":
        xmlfile = 'backend/assets/haarcascade_eye.xml'
    else:
        return jsonify({"error": "Nenhuma opção de detecção escolhida."}), 400

    try:
        for escala, vizinhos in parametros['Rosto']:
            objetos_rosto = AplicarClassificador(xmlfile, imagem_rosto, escala=escala, vizinhos=vizinhos)
            MostrarImagemComDeteccoes(imagem_rosto.copy(), objetos_rosto, nome="Resultado")
            
        return jsonify({"message": "Imagem processada com sucesso", "image_path": os.path.join(temp_dir, 'image_result.png')})
    except ValueError as e:
        return jsonify({"error": str(e)}), 500

@app.route('/get_image', methods=['GET'])
def get_image():
    temp_dir = tempfile.gettempdir()
    image_path = os.path.join(temp_dir, 'image_result.png')
    if os.path.exists(image_path):
        return send_file(image_path, mimetype='image/png')
    return jsonify({"error": "Imagem não encontrada"}), 404

if __name__ == '__main__':
    app.run(debug=True)
