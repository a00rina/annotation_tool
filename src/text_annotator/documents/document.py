from typing import List


class Document:
    """
    Represents a text document from a linguistic corpus.

    Encapsulates raw text, language, and source information.
    Provides methods for tokenization and persistence.
    """

    def __init__(self, id: int, content: str, source: str, lang: str = 'ru'):
        self.id = id
        self.lang = lang
        self.content = content
        self.source = source
        # self.metadata = metadata or {}


    def tokenize(self) -> List[str]:
        """
        Tokenize the document content into a list of words.

        Uses a simple regex-based tokenizer that extracts alphanumeric sequences
        and converts them to lowercase.

        Returns:
            List[str]: A list of word tokens.
        """
        import re

        return re.findall(r'\w+', self.content.lower())


    def save_to_db(self, storage) -> None:
        """
        Persist the document to the provided storage backend.

        Delegates saving logic to the `storage` object, which must implement
        a compatible interface (e.g., `Storage.save_document`).

        Args:
            storage: A storage instance (e.g., SQLite-based Storage).
        """
        storage.save_document(self)
