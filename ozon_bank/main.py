from fastapi import FastAPI


class Database:
    def connect(self):
        return "Соединение с базой данных"


class Service:
    def __init__(self):
        self.db = Database()

    def get_data(self):
        return self.db.connect()


app = FastAPI()


@app.get("/")
def read_data():
    service = Service()
    return service.get_data()
