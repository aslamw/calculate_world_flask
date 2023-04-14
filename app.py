from src import app
from waitress import serve
from werkzeug.middleware.proxy_fix import ProxyFix



if __name__ == "__main__":
    app.logger.info('Environment prod running. Port 5000')
    serve(app, host="0.0.0.0", port=5000)
    #app.run(debug=True, port=5000, host='0.0.0.0')
    