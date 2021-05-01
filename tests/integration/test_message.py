from counter.counter import Counter
from message.message import Message


def test_that_message_compute_with_counter_input(content):
    counter = Counter(content)
    counter.extract_counter()
    message = Message(counter)
    message.compute_message()

    assert message.message == f"""
    {counter.counter}.
    
    C'est le nombre de personnes sensibilisées par @FresqueDuClimat entre 2018 et aujourd'hui!
    
    Faites grimper le compteur !
    
    Inscrivez-vous à une Fresque du Climat: https://fresqueduclimat.org/dates-demos/
    Formez-vous à l'animation: https://fresqueduclimat.org/dates-formations/
    """
