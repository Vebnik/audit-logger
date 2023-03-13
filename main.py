from dotenv import load_dotenv; load_dotenv()
from os import getenv

from src.app import App
from src.models import Config

def main() -> None:

    config = Config(getenv('BOT_TOKEN'))
    app = App(config)

    app.run()


if __name__ == '__main__':
    main()

