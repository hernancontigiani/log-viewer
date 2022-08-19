import os
import json
import logging
import logging.config

# https://fangpenlin.com/posts/2012/08/26/good-logging-practice-in-python/

# CONFIG:
# 1 - primero se define el formato
# 2 - luego se crea cada handler, el cual definidmos
#   --> tipo de handler (strea consola, stream archivo)
#   --> level (filtro, se escucha de aquí par aabajo)
#   --> formato (se elije alguno de los definos)
#   --> ubicacion, bytes, output, etc
# 3 --> al final de todo se define el LEVEL general y los handlers a usar

def setup_logging(default_level=logging.INFO):
    """Setup logging configuration

    """
    #os.makedirs(os.path.dirname("/var/log/test/"), exist_ok=True)
    path = 'logging.json'
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)


setup_logging()

logger = logging.getLogger(__name__)
logger.info('Hello World!')
logger.error('Page not found')