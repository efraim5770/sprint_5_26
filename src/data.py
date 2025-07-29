from __future__ import annotations
import os

class Urls:

    BASE: str = os.getenv("SB_BASE_URL", "https://stellarburgers.nomoreparties.site")
    MAIN_PATH: str = "/"
    REGISTER_PATH: str = "/register"
    LOGIN_PATH: str = "/login"
    FORGOT_PASSWORD_PATH: str = "/forgot-password"
    PROFILE_PATH: str = "/account/profile"

    @classmethod
    def main(cls) -> str:
        return cls.BASE + cls.MAIN_PATH

    @classmethod
    def register(cls) -> str:
        return cls.BASE + cls.REGISTER_PATH

    @classmethod
    def login(cls) -> str:
        return cls.BASE + cls.LOGIN_PATH

    @classmethod
    def forgot_password(cls) -> str:
        return cls.BASE + cls.FORGOT_PASSWORD_PATH

    @classmethod
    def profile(cls) -> str:
        return cls.BASE + cls.PROFILE_PATH

class TestUser:

    name: str = "Test Testov"
    login: str = "test_testov777@inbox.ru"
    password: str = "test_testov"
