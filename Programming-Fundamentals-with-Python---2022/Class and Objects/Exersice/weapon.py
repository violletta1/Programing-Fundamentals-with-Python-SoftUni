# Create a class Weapon. The __init__ method should receive a number of bullets (integer).
# Create an attribute called bullets to store that number. The class should also have the following methods:
# shoot()
# If there are bullets in the weapon, reduce them by 1 and return a message "shooting..."
# If there are no bullets left, return: "no bullets left"
# __repr__()
# Returns "Remaining bullets: {amount_of_bullets}"
# You can read more about the method here: link
class Weapon:
    def __init__(self, number_bullets):
        self.number_bullets = number_bullets

    def shoot(self):
        if self.number_bullets < 0:



