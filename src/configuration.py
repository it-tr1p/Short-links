import os
from dotenv import load_dotenv
from dataclasses import dataclass
from sqlalchemy.engine import URL

load_dotenv()


@dataclass
class DatabaseConfig:
    """Database connection variables"""

    name: str = os.getenv("DB_NAME")
    user: str = os.getenv("DB_USERNAME", "docker")
    passwd: str = os.getenv("DB_PASSWORD", None)
    port: int = os.getenv("DB_PORT")
    host: str = os.getenv("DB_HOST", "localhost")

    driver: str = "asyncpg"
    database_system: str = "postgresql"

    def build_connection_url(self) -> str:
        """This method create a connection string"""
        return URL.create(
            drivername=f"{self.database_system}+{self.driver}",
            username=self.user,
            database=self.name,
            password=self.passwd,
            port=self.port,
            host=self.host,
        ).render_as_string(hide_password=False)


@dataclass
class BotConfig:
    """Bot configuration"""

    token: str = os.getenv("BOT_TOKEN")


@dataclass
class Configuration:
    """All in one configuration's class"""

    db = DatabaseConfig()
    bot = BotConfig()


conf = Configuration()
