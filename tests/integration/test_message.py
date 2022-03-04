from counter.counter import Counter
from message.message import Message


def test_that_message_compute_with_counter_input(content):
    counter = Counter(content)
    counter.extract_counter()
    message = Message(counter)
    message.compute_message()
    counter = "{:,}".format(int(counter.counter)).replace(",", " ")
    assert (
        message.message
        == f"{counter}.\n\nC'est le nombre de personnes sensibilisées par @FresqueDuClimat entre 2018 et aujourd'hui!\n\nFaites grimper le compteur !\n\nInscrivez-vous à une Fresque du Climat 👇\n#FresqueDuClimat #GIEC https://tinyurl.com/57rd8eer"  # noqa: W503
    )
