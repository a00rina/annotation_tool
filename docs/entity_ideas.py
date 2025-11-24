from typing import List, Dict, Any


class Document:
    def __init__(self, id: int, content: str, source: str, lang: str = "ru"):
        self.id = id
        self.lang = lang
        self.content = content
        self.source = source
        # self.metadata = metadata or {}

    def tokenize(self) -> List[str]:
        """
        return: tokens from text(documents)
        """
        pass

    def save_to_db(self, storage) -> None:
        """
        save to database
        :param storage: Storage
        :return: None
        """
        pass


class Annotation:
    def __init__(self, document_id: int, annotator_name: str, annotation_type: str, data: Dict[str, Any]):
        self.document_id = document_id
        self.annotator_name = annotator_name
        self.annotation_type = annotation_type
        self.data = data

    def to_conllu(self) -> str:
        return ""


class Analyzer:
    def __init__(self):
        self.name = "base"

    def analyze(self, text: str):
        pass

    def get_supported_types(self) -> List[str]:
        pass


class StanzaAnalyzer(Analyzer):

    def __init__(self, lang: str = "ru"):
        super().__init__()
        self.name = "stanza"
        self.lang = lang

    def analyze(self, text: str):
        pass



class Storage:

    def __init__(self, db_path: str = "annotations.db"):
        self.db_path = db_path

    def save_document(self, doc: Document):
        # save id?
        pass

    def save_annotation(self, annot: Annotation):
        pass

    def get_documents(self, doc_id:int):
        return []


class Analytics:

    def __init__(self, storage: Storage):
        self.storage = storage

    def get_statistics(self, doc_ids: List[int]):
        pass

    def plot_entity_frequency(self) -> None:
        pass