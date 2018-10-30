from api import app
import os
from api.config import app_config
print(os.getenv('ENVIRONMENT'))
print(app_config['production'].ENVIRONMENT)

if __name__ == "__main__":
    app.run()