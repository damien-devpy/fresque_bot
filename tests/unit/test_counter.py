import pytest

from counter.counter import Counter
from counter.missingcounterexception import MissingCounterException


def test_that_counter_successfully_get_counter(content):
    counter = Counter(content)
    counter.extract_counter()
    assert counter.counter == "157277"


def test_that_counter_successfully_raise_exception_when_counter_cant_be_found(
    wrong_content,
):
    counter = Counter(wrong_content)

    with pytest.raises(MissingCounterException) as err:
        counter.extract_counter()

    assert "Counter can't be found" in str(err)
