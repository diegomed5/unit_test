from src.models.Language_model import Language_model

def test_get_language_not_none():
    languages=Language_model.get_language()
    assert languages != None

def test_get_language_has_elements():
    languages=Language_model.get_language()
    assert len(languages) > 0

def test_get_language_check_elements_length():
    languages=Language_model.get_language()
    for language in languages:
        assert len(language) > 0