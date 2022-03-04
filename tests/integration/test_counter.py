from counter.counter import Counter


def test_that_counter_succesfully_extract_counter(response):
    counter = Counter(response)
    counter.extract_counter()

    assert isinstance(counter.counter, int)
    assert len(str(counter.counter)) >= 6
