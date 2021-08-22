from genderclf import __version__
from genderclf import GenderClassifier


def test_version():
    assert __version__ == "0.0.1"


def test_genderclf_for_male():
    g = GenderClassifier()
    g.name = "Hemant"
    result = g.predict()
    assert result == "Male"


def test_genderclf_for_female():
    g = GenderClassifier()
    g.name = "Hansa"
    result = g.predict()
    assert result == "Female"
