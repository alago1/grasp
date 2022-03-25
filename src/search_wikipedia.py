import spacy
import wikipedia

nlp = spacy.load("en_core_web_sm")
doc = nlp(
    "Maxwell's equations integral form explain how the electric charges and electric currents produce magnetic and electric fields. The equations describe how the electric field can create a magnetic field and vice versa."
)
for chunk in doc.noun_chunks:
    query = wikipedia.page(chunk.text)
    print(chunk.text, query.url)
