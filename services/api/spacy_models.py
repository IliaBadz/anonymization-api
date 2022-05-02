import spacy


def load_models() -> dict:
    models = {
        "en_sm": spacy.load('api/ml/models/en_sm'),
        "fr_sm": spacy.load("api/ml/models/fr_sm"),
    }

    print("models loaded from disk")
    return models
