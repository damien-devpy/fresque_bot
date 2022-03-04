import pytest

from counter.counter import Counter


def test_that_counter_successfully_get_counter(content):
    assert Counter(content).counter == 327342


def test_that_counter_successfully_raise_exception_when_counter_cant_be_found(
    wrong_content,
):
    with pytest.raises(KeyError):
        Counter(wrong_content)
