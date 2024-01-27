class Book:
    def __init__(self, name, author):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"{self.__class__.__name__}: {self.name} by {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.author}')"


class PaperBook(Book):
    def __init__(self, name, author, pages):
        super().__init__(name, author)
        self._pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Pages must be a positive integer.")
        self._pages = value

    def __str__(self):
        return f"{super().__str__()}, {self.pages} pages"

    def __repr__(self):
        return f"{super().__repr__()}, pages={self.pages}"


class AudioBook(Book):
    def __init__(self, name, author, duration):
        super().__init__(name, author)
        self._duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Duration must be a positive number.")
        self._duration = value

    def __str__(self):
        return super().__str__() + f", {self.duration} hours"

    def __repr__(self):
        return super().__repr__() + f", duration={self.duration}"


# Пример
paper_book = PaperBook("Преступление и наказание", "Федор Достоевский", 500)
audio_book = AudioBook("Мастер и Маргарита", "Михаил Булгаков", 15.75)

print(paper_book)
print(repr(paper_book))

print(audio_book)
print(repr(audio_book))