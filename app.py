from app import *
import os

# Run Server
if __name__ == '__main__':
    app.run(
        host = os.environ.get("APP_HOST"), 
        port = os.environ.get("APP_PORT"), 
        debug = os.environ.get("APP_DEBUG")
    )  