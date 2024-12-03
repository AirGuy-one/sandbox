from abc import ABC, abstractmethod


class ShardManager(ABC):
    @abstractmethod
    def manage(self):
        pass


class MySQLShardManager(ShardManager):
    def __init__(self, config: str):
        self.config = config

    def manage(self):
        print(f"Managing MySQL shard with config: {self.config}")


class PostgresShardManager(ShardManager):
    def __init__(self, config: str):
        self.config = config

    def manage(self):
        print(f"Managing Postgres shard with config: {self.config}")
