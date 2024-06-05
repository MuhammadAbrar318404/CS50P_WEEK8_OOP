import pytest
from seasons import calculate_words

def test_calculate_words_valid():
    assert calculate_words("2002-08-24") == "eleven million, four hundred fifty-three thousand, seven hundred sixty"

def test_calculate_words_invalid():
    with pytest.raises(SystemExit):
        calculate_words("January 1, 1999")
    with pytest.raises(SystemExit):
        calculate_words("1999.01.01")
    with pytest.raises(SystemExit):
        calculate_words("1999-10-99")
    with pytest.raises(SystemExit):
        calculate_words("cat")
