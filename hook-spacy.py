"""
Combined hook for spacy and its dependency libraries; should probably be separated.
"""
from PyInstaller.utils.hooks import collect_data_files
import spacy

datas = collect_data_files("spacy", False)
datas.append((spacy.util.get_data_path(), "spacy/data"))

datas.extend(collect_data_files("thinc", False))

hiddenimports = [
    "blis",
    "blis.py",
    "cymem.cymem",
    "murmurhash",
    "preshed.maps",
    "spacy._align",
    "spacy.kb",
    "spacy.lang.en",
    "spacy.lang.es",
    "spacy.lang.fr",
    "spacy.lexeme",
    "spacy.matcher._schemas",
    "spacy.morphology",
    "spacy.parts_of_speech",
    "spacy.strings",
    "spacy.syntax",
    "spacy.syntax._beam_utils",
    "spacy.syntax._parser_model",
    "spacy.syntax.arc_eager",
    "spacy.syntax.ner",
    "spacy.syntax.nn_parser",
    "spacy.syntax.nonproj",
    "spacy.syntax.stateclass",
    "spacy.syntax.transition_system",
    "spacy.tokens._retokenize",
    "spacy.tokens.morphanalysis",
    "spacy.tokens.underscore",
    "srsly.msgpack.util",
    "thinc.extra.search",
    "thinc.linalg",
    "thinc.neural._aligned_alloc",
    "thinc.neural._custom_kernels",
]
