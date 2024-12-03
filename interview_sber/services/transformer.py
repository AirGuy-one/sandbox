class Transformator:
    def transform(
        self,
        raw_data,
    ) -> Dict:
        user_id: str = raw_data["user"] if "user" in raw_data.keys() else ""
        documents: List = raw_data["documents"] if "documents" in raw_data.keys() else []
        if int(user_id) < 0 or "":
            return None
        if documents == []:
            return None

        users_documents = []
        for document in documents:
            users_documents.append({
                f"{document['id']}/{user_id}": {
                    "text": document["text"],
                    "inn": int(document["meta_date"]["inn"]),
                    "date": datetime.strtime(document["meta_date"]["date"])
                }
            })

        return
