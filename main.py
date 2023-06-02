from flask import Flask, jsonify
import speedtest

app = Flask(__name__)

# instanciando a biblioteca...
teste = speedtest.Speedtest()

# rota de teste de download
@app.route('/download')
def teste_download():
    download = teste.download()
    # converte para MegaByte
    resultado = download / 10**6
    # retorna o resultado em MegaByte com apenas duas casas decimais
    return jsonify({"message": f"Download: {resultado:.2f}"})

# rota de teste de upload
@app.route('/upload')
def teste_upload():
    upload = teste.upload()
    # converte para MegaByte
    resultado = upload / 10**6 
    # retorna o resultado em MegaByte com apenas duas casas decimais
    return jsonify({"message": f"Upload: {resultado:.2f}"})

# rota de teste de ping
@app.route('/ping')
def ping():
    ping = teste.results.ping
    return jsonify({"message": f"Ping: {ping}"})


if "__main__" == __name__:
    app.run(debug=True)