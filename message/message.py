class Message:
    """Compute pre registered message with inputs"""

    MESSAGE = "{counter}.\n\nC'est le nombre de personnes sensibilisées par @FresqueDuClimat entre 2018 et aujourd'hui!\n\nFaites grimper le compteur !\n\nInscrivez-vous à une Fresque du Climat 👇 #FresqueDuClimat #ClimateCollage #GIEC #ClimateEducation https://tinyurl.com/2zp9938a"

    def __init__(self, counter):

        self.message = None
        self.counter = self._format_counter(counter.counter)

    def compute_message(self):
        self.message = self.MESSAGE.format(counter=self.counter)

    def _format_counter(self, counter):
        return "{:,}".format(int(counter)).replace(",", " ")
