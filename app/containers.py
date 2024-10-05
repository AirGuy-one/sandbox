# app/containers.py
from dependency_injector import containers, providers
from .services import GreetingService


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    greeting_service = providers.Singleton(GreetingService)
