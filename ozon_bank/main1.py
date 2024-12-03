from fastapi import FastAPI, Depends


class Database:
    def connect(self):
        return "Соединение с базой данных"


class Service:
    def __init__(self, db: Database):
        self.db = db

    def get_data(self):
        return self.db.connect()


app = FastAPI()


def get_database():
    return Database()


@app.get("/")
def read_data(
    service: Service = Depends(get_database),
):
    return service.get_data()
