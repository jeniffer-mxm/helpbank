from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Configurações
app.config['SECRET_KEY'] = 'helpbank-secret-key-2026'

@app.route('/')
def index():
    """Página inicial do site HelpBank"""
    return render_template('index.html')

@app.route('/api/contato', methods=['POST'])
def contato():
    """Endpoint para processar formulário de contato"""
    try:
        data = request.get_json()
        nome = data.get('nome')
        email = data.get('email')
        telefone = data.get('telefone')
        mensagem = data.get('mensagem')
        
        # Aqui você pode adicionar lógica para salvar em banco de dados
        # ou enviar email
        
        return jsonify({
            'success': True,
            'message': 'Mensagem enviada com sucesso! Entraremos em contato em breve.'
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'message': 'Erro ao enviar mensagem. Tente novamente.'
        }), 500

@app.route('/api/simulacao', methods=['POST'])
def simulacao():
    """Endpoint para processar simulação de empréstimo"""
    try:
        data = request.get_json()
        valor = data.get('valor')
        parcelas = data.get('parcelas')
        
        # Cálculo fictício - você pode ajustar a lógica
        taxa_juros = 1.5  # 1.5% ao mês
        valor_total = float(valor) * (1 + (taxa_juros/100 * int(parcelas)))
        valor_parcela = valor_total / int(parcelas)
        
        return jsonify({
            'success': True,
            'valor_solicitado': float(valor),
            'parcelas': int(parcelas),
            'valor_parcela': round(valor_parcela, 2),
            'valor_total': round(valor_total, 2),
            'taxa_juros': taxa_juros
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'message': 'Erro ao calcular simulação.'
        }), 500


if __name__ == "__main__":
    app.run(debug=True)
