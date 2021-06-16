from app import app

class Test:
    @app.route('/test', methods=['GET'])
    def hello():
        return "Asdas"