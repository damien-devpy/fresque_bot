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

    assert message.message == """
    42.
    
    C'est le nombre de personnes sensibilisées par @FresqueDuClimat entre 2018 et aujourd'hui!
    
    Faites grimper le compteur !
    
    Inscrivez-vous à une Fresque du Climat: https://fresqueduclimat.org/dates-demos/
    Formez-vous à l'animation: https://fresqueduclimat.org/dates-formations/
    """

