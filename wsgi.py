from backend import app
import logging
logging.basicConfig(format='%(levelname)s %(asctime)s: %(message)s',
                        filename='log/backend.log',
                        level=logging.DEBUG)
logging.debug("test")

if __name__ == "__main__":

    logging.debug("App started")
    app.run()
