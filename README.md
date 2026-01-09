# HelpBank - Site Institucional de Empréstimo Consignado

## 📋 Descrição

Site institucional completo para empréstimo consignado com foco em conversão, credibilidade e confiança. Desenvolvido com HTML5, CSS3 e Python (Flask).

## 🎨 Design

### Paleta de Cores
- **Roxo (#6944ba)**: Cor principal
- **Laranja (#dd7d18)**: Chamadas para ação (CTA)
- **Verde Água (#5fb49b)**: Destaques, selos de confiança e ícones

## 🚀 Como Executar

### Requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Instalação

1. **Clone ou copie os arquivos para seu computador**

2. **Navegue até a pasta do projeto**
   ```bash
   cd helpbank
   ```

3. **Crie um ambiente virtual (recomendado)**
   ```bash
   python -m venv venv
   ```

4. **Ative o ambiente virtual**
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Mac/Linux:
     ```bash
     source venv/bin/activate
     ```

5. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

6. **Execute a aplicação**
   ```bash
   python app.py
   ```

7. **Acesse no navegador**
   ```
   http://localhost:5000
   ```

## 📁 Estrutura de Arquivos

```
helpbank/
├── app.py                 # Backend Flask
├── requirements.txt       # Dependências Python
├── README.md             # Documentação
├── templates/            # Templates HTML
│   └── index.html       # Página principal
└── static/              # Arquivos estáticos
    ├── css/
    │   └── style.css    # Estilos CSS
    └── images/          # Pasta para suas imagens
```

## 🎯 Funcionalidades

### Seções do Site
1. **Navbar**: Menu de navegação responsivo
2. **Hero Section**: Primeira impressão com CTA destacado
3. **Benefícios**: Por que escolher a HelpBank
4. **Público-Alvo**: Quem pode contratar
5. **Simulação**: Botão direto para WhatsApp
6. **Credibilidade**: Selos de confiança
7. **Contato**: Formulário e informações
8. **Footer**: Rodapé com links e créditos

### Recursos Técnicos
- ✅ Design responsivo (mobile-first)
- ✅ Animações suaves e interativas
- ✅ Integração com WhatsApp
- ✅ Formulário de contato funcional
- ✅ API RESTful com Flask
- ✅ Código limpo e comentado

## 📱 WhatsApp

O botão de simulação redireciona para o WhatsApp com mensagem pré-preenchida:
- **Número**: (21) 99631-0471

## 🎨 Personalização

### Alterando Cores
Edite as variáveis CSS no arquivo `static/css/style.css`:
```css
:root {
    --color-primary: #6944ba;    /* Roxo */
    --color-secondary: #dd7d18;  /* Laranja */
    --color-accent: #5fb49b;     /* Verde água */
}
```

### Alterando Textos
Edite o arquivo `templates/index.html` e modifique os textos conforme necessário.

### Adicionando Imagens
1. Coloque suas imagens na pasta `static/images/`
2. Referencie no HTML:
   ```html
   <img src="{{ url_for('static', filename='images/sua-imagem.jpg') }}" alt="Descrição">
   ```

## 📊 API Endpoints

### POST /api/contato
Envia mensagem de contato
```json
{
  "nome": "João Silva",
  "email": "joao@email.com",
  "telefone": "21999999999",
  "mensagem": "Gostaria de mais informações"
}
```

### POST /api/simulacao
Calcula simulação de empréstimo
```json
{
  "valor": 10000,
  "parcelas": 24
}
```

## 🔧 Troubleshooting

### Erro: Porta já em uso
Se a porta 5000 estiver ocupada, altere no `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=8000)  # Use outra porta
```

### Erro: Módulo não encontrado
Certifique-se de que instalou as dependências:
```bash
pip install -r requirements.txt
```

## 📝 Próximos Passos

1. ✅ Substituir informações fictícias por dados reais
2. ✅ Adicionar suas próprias imagens
3. ✅ Configurar envio real de emails no formulário
4. ✅ Integrar com banco de dados (MongoDB, PostgreSQL, etc.)
5. ✅ Adicionar Google Analytics
6. ✅ Implementar SSL para HTTPS
7. ✅ Deploy em servidor (Heroku, AWS, DigitalOcean, etc.)

## 👩‍💻 Desenvolvido Por

**Jeniffer Maximo**

---

## 📄 Licença

© 2026 HelpBank – Todos os direitos reservados