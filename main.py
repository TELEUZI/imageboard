from app import app
import view
from config import Config
app.config.from_object(Config)
if __name__ == "__main__":
    app.run()