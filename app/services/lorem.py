from lorem_text import lorem


def generate_words(count: int = 30) -> str:
    return lorem.words(count)


def generate_sentence() -> str:
    return lorem.sentence()


def generate_paragraphs(count: int = 1) -> str:
    return lorem.paragraphs(count)