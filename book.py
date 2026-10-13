class Book:
    def __init__(self, id, title, author, copies=1, available_copies=1):
        self.id = id
        self.title = title
        self.author = author
        self.copies = copies
        self.available_copies = available_copies

    def get_dict(self):
        return {
        "id": self.id,
        "title": self.title,
        "author": self.author,
        "copies": self.copies,
        "available_copies": self.available_copies
    }

    @staticmethod
    def create_dict(id, title, author, copies=0, available_copies=0):
        return {
        "id": id,
        "title": title,
        "author": author,
        "copies": copies,
        "available_copies": available_copies
    }