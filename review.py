#!usr/bin/python3
""" Class Review with the necessary attributes and methods."""

from datetime import datetime

class Review:
    def __init__(self, user, place, text, rating):
        self.id = str(uuid.uuid4())
        self.user = user
        self.place = place
        self.text = text
        self.rating = rating
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.updated_at = datetime.now()

    def delete(self):
        del self

    def __str__(self):
        return f"Review({self.id}, {self.user}, {self.place}, {self.rating})"