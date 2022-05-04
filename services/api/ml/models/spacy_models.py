import spacy


def load_models() -> dict:
    models = {
        'en_sm': spacy.load('en_core_web_sm'),
        'en_md': spacy.load('en_core_web_md'),
    }

    return models
