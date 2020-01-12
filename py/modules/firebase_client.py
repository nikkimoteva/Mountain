from google.cloud import firestore


class FirebaseClient:
    def __init__(self, service_account_path):
        self.db = firestore.Client.from_service_account_json(
            service_account_path)

    def import_to_collection(self, collection, data_id, data):
        ref = self.db.collection(collection)
        ref.document(data_id).set(data)
