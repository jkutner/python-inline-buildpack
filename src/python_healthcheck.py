import os
import requests
from flask import Flask

def create():
    # Create paths for healthcheck ports to respond healthy
    app_health = Flask(__name__)
    port = os.environ.get("health_port", 8081)
    app_port = os.environ.get("port", 8080)

    @app_health.route("/manage/health", methods=["GET"])
    @app_health.route("/manage/ready", methods=["GET"])
    def health_probe():
        api_url = f"http://localhost:{app_port}/hello"
        response = requests.get(api_url)
        if response.status_code == 200:
            return "ok", 200
        return "unhealthy", 500

    return app_health, port

# Do stuff
if __name__ == "__main__":
    app_health, port = create()
    app_health.run(host="0.0.0.0", port=port, debug=False)