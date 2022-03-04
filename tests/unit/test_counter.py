import pytest

from counter.counter import Counter
from counter.missingcounterexception import MissingCounterException


def test_that_counter_successfully_get_counter(content):
    counter = Counter(content)
    assert counter.counter == 327342

def test_that_counter_successfully_raise_exception_when_counter_cant_be_found(
    wrong_content,
):
    with pytest.raises(KeyError) as err:
        counter = Counter(wrong_content)
