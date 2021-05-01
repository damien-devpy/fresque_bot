from message.message import Message


class MockCounter:

    def __init__(self, *args, **kwargs):
        pass

    @property
    def counter(self):
        return '42'

def test_that_message_compute_with_input():
    counter = MockCounter()
    message = Message(counter)
    message.compute_message()

    assert message.message == "42.\n\nC'est le nombre de personnes sensibilisées par @FresqueDuClimat entre 2018 et aujourd'hui!\n\nFaites grimper le compteur !\n\nInscrivez-vous à une Fresque du Climat 👇 https://tinyurl.com/2zp9938a"

