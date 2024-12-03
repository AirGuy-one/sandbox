


class Extractor:
    @staticmethod
    def extract(
        source_client,
    ) -> Dict:
        return source_client.get_raw_data()
