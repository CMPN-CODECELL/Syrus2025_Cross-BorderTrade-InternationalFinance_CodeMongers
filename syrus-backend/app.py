from flask import Flask
from flask_cors import CORS
# from routes.trade import trade_blueprint
# from routes.compliance import compliance_blueprint

app = Flask(__name__)
CORS(app)

@app.get("/")
def home():
    return "Syrus Backend Default Route"
# app.register_blueprint(trade_blueprint, url_prefix="/trade")
# app.register_blueprint(compliance_blueprint, url_prefix="/compliance")

if __name__ == "__main__":
    app.run(debug=True)
