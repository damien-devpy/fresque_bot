
class Message:
    """Comptute pre registered message with inputs"""

    MESSAGE = """
    {counter}.
    
    C'est le nombre de personnes sensibilisées par @FresqueDuClimat entre 2018 et aujourd'hui!
    
    Faites grimper le compteur !
    
    Inscrivez-vous à une Fresque du Climat: https://fresqueduclimat.org/dates-demos/
    Formez-vous à l'animation: https://fresqueduclimat.org/dates-formations/
    """

    def __init__(self, counter):
        
        self.counter = counter.counter
        self.message = None

    def compute_message(self):
        self.message = self.MESSAGE.format(counter=self.counter)
