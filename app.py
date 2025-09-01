from flask import Flask
from controllers.notificacion_controller import notificacion_bp

app = Flask(__name__)
app.register_blueprint(notificacion_bp)

if __name__ == "__main__":
    app.run(port=5005, debug=True)
