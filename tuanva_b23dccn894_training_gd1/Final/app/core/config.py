from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    ProjectName: str = "MyApp"
    SQLALCHEMY_DATABASE_URI: str = "mysql+pymysql://springstudent:springstudent@localhost:3306/webpython"
    SECRET_KEY: str = "9f3a8c2b7d4e6a1c5e8f9b2a3d6c7e4f"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    CLOUDINARY_NAME: str
    CLOUDINARY_API_KEY: str
    CLOUDINARY_API_SECRET: str
    CLOUDINARY_FOLDER: str = "events"   # nên cho default để khỏi missing

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
