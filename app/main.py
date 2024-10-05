# app/main.py
from fastapi import FastAPI, Depends
from dependency_injector.wiring import inject, Provide
from .containers import Container
from .services import GreetingService

container = Container()
app = FastAPI()


@app.get("/")
@inject
def read_root(greeting_service: GreetingService = Depends(Provide[Container.greeting_service])):
    return {"message": greeting_service.get_greeting()}


container.wire(modules=[__name__])
