import os

import dotenv


dotenv.load_dotenv()


APP_HOST: str = os.getenv('APP_HOST', '127.0.0.1')
APP_PORT: int = int(os.getenv('APP_PORT', '8000'))
