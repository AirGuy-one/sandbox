class Loader:
    def __init__(
        self,
        destination_client,
    ):
        self.destination_client = destination_client

    def load(
        self,
        users_documents,
    ) -> None:
        self.destination_client.load(users_documents)
