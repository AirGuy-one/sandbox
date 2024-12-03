from fastapi import FastAPI, Depends

app = FastAPI()


class ShardManager:
    def __init__(self, config: str):
        self.config = config

    def manage(self):
        print(f"Managing shard with config: {self.config}")


@app.get("/")
async def read_shard_info(shard_manager: ShardManager = Depends(ShardManager)):
    shard_manager.manage()
    return {"message": "Shard info displayed"}

