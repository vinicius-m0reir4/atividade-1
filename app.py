from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Isso permite que a API seja acessada de qualquer domínio

@app.route('/health', methods=['GET'])
def health_check():
    """Endpoint para verificar se a API está funcionando"""
    return jsonify({
        "status": "success",
        "message": "API funcionando corretamente"
    })

@app.route('/me', methods=['GET'])
def get_student_info():
    """Endpoint para retornar informações do aluno"""
    student_info = {
        "nome": "Vinicius Moreira de Souza",
        "email": "lache1235@gmail.com",
        "curso": "Sistemas de Informação",
        "GitHub": "https://github.com/vinicius-m0reir4",
        "cidade": "Juazeiro do Norte - CE",
        "interesses": ["programação", "tecnologia", "APIs", "Flask", "Python"]
    }
    return jsonify(student_info)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)