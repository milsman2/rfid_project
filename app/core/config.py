"""
All imports
"""

import logging
import os
import secrets
from enum import Enum
from functools import lru_cache
from typing import Optional
from pydantic import BaseSettings

logger = logging.getLogger(__name__)

class EnvironmentEnum(str, Enum):
    """Production key for environment"""
    PRODUCTION = "production"
    LOCAL = "local"

class GlobalConfig(BaseSettings):
    """Standard configurations"""
    TITLE: str = "The Punters League REST API"
    DESCRIPTION: str = "A REST API for DevOps Focused Full Stack Fantasy Punting"
    JWT_SECRET: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    ALGORITHM = "HS256"
    ENVIRONMENT: EnvironmentEnum
    DEBUG: bool = False
    TESTING: bool = False
    TIMEZONE: str = "CDT"
    API_V1_STR = "/api/v1"

    class Config:
        """Standardize input"""
        case_sensitive = True

class LocalConfig(GlobalConfig):
    """Local configurations."""

    DEBUG: bool = True
    ENVIRONMENT: EnvironmentEnum = EnvironmentEnum.LOCAL


class ProdConfig(GlobalConfig):
    """Production configurations."""

    DEBUG: bool = False
    ENVIRONMENT: EnvironmentEnum = EnvironmentEnum.PRODUCTION


class FactoryConfig:
    def __init__(self, environment: Optional[str]):
        self.environment = environment

    def __call__(self) -> GlobalConfig:
        if self.environment == EnvironmentEnum.LOCAL.value:
            return LocalConfig()
        return ProdConfig()


@lru_cache()
def get_configuration() -> GlobalConfig:
    """Factory function to pass inputs for environment"""
    return FactoryConfig(os.environ.get("ENVIRONMENT"))()


settings = get_configuration()
