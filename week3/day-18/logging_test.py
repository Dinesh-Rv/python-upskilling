import logging 
from logging.handlers import RotatingFileHandler
from burger_shop import BurgerShop

logger = logging.getLogger("orders")
logger.setLevel(logging.DEBUG)

console = logging.StreamHandler()
console.setLevel(logging.WARNING)

file = RotatingFileHandler(
    "app.log",
    maxBytes=5*1024*1024,
    backupCount=3
    )

file.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d -%(message)s"
)
console.setFormatter(formatter)
file.setFormatter(formatter)

logger.addHandler(console)
logger.addHandler(file)

try:
    shop = BurgerShop("Test Shop", {
            "Classic": 180,
            "Premium": 200,
            "Loaded": 250,
            "Fries": 100
        })
    shop.add_to_cart("Classic", -1)
except Exception as e:
    logger.error(f"Error: {e}", exc_info=True)
finally:
    logger.info("Shop process completed")