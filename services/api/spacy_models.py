import spacy


def load_models() -> dict:
    models = {
        "en_sm": spacy.load('en_core_web_sm'),
        "fr_sm": spacy.load("fr_core_news_sm"),
    }

    print("models loaded from disk")
    return models
