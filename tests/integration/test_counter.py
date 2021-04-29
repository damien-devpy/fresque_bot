from counter.counter import Counter


def test_that_counter_succesfully_extract_counter(response):
    counter = Counter(response)
    counter.extract_counter()

    assert counter.counter.isdigit()
    assert len(counter.counter) >= 6
