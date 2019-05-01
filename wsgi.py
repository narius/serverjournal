from backend import app
import logging


if __name__ == "__main__":
    logging.basicConfig(format='%(levelname)s %(asctime)s: %(message)s',
                        filename='log/backend.log',
                        level=logging.INFO)
    logging.debug("App started")
    app.run()
