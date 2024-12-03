from abc import ABC, abstractmethod
from datetime import datetime
from typing import *

"""
input_data = {
    "user": str,
    "documents":
        [
            "document":
                {
                    "id": str,
                    "text": str,
                    "meta_data": {
                        "inn": str,
                        "date": str
                    }
                }
        ]
}
"""

output_data = [
    {
        "{document_id}/{user_id}":
            {
                "text": str,
                "inn": int,
                "date": datetime
            }
    }
]


class DependsExtractor(ABC):
    @abstractmethod
    def extract(self):
        pass


class DependsLoader(ABC):
    @abstractmethod
    def load(self):
        pass





class ETLPipeline:
    """Сервис загрузки данных из источника
    Требования:
    - Код должен быть написан в соответствии с принципами чистой архитектуры и внедрения зависимостей
    - Код должен следовать лучшим практикам написания кода на Python
    - Необходима валидация сырых данных
    - Для зарузки данных через клиент необходимо обернуть данные в какой-либо dataclass
    - Провести рефактор класса ETLPipeline, выделить в методе main основные логики и прописать для них классы (получение данных, трансформация данных, загрузка данных)
    Нужно обратить внимание на то, что класс трансформации данных должен быть легко заменяем на аналогичный
    - добавить логгирование при ошибка и нестандратных ситуациях
    """

    def __init__(
        self,
        source_client,
        extractor: Extractor = DependsExtractor(),
        transformer: Extractor = DependsExtractor(),
        loader: Loader = DependsLoader(),
    ):
        self.extractor = extractor
        self.loader = loader
        self.transformer = transformer

    def main(
        self,
    ):
        raw_data: Dict = self.extractor.extract(self.source_client)
        users_documents = self.transformer.transform(raw_data)
        self.loader.load(users_documents)
