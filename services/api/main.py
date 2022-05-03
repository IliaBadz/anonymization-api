from copy import deepcopy

from api.ml.models.spacy_models import load_models
from api.ml.models.data_models import EntitiesOut, UserRequestIn

from fastapi import FastAPI


models = load_models()

app = FastAPI()


@app.post("/entities", response_model=EntitiesOut)
def extract_entities(user_request: UserRequestIn):
    text = user_request.text
    language = user_request.model_language
    model_size = user_request.model_size

    model_key = language + "_" + model_size

    model = models[model_key]
    doc = model(text)

    entities = [
        {
            'start': ent.start_char,
            'end': ent.end_char,
            'type': ent.label_,
            'text': ent.text,
        } for ent in doc.ents
    ]

    anonymized_text = list(deepcopy(text))

    for entity in entities:
        start = entity['start']
        end = entity['end']
        anonymized_text[start:end] = "X" * (end - start)

    anonymized_text = ''.join(anonymized_text)
    return {'entities': entities, 'anonymized_text': anonymized_text}
