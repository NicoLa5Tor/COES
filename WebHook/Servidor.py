from flask import Flask, request, jsonify

app = Flask(__name__)

VERIFY_TOKEN = "hola"

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET': 
        mode = request.args.get('hub.mode')
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')

        if mode == "subscribe" and token == VERIFY_TOKEN:
            return challenge, 200
        else:
            return "Error de verificación", 403

    elif request.method == 'POST': 
        data = request.json
        print("Datos recibidos:", data) 
        return jsonify({"message": "Evento recibido"}), 200

def run_webHook():
    app.run(port=5000, debug=True) 
