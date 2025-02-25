class Person: 
    
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def hit(self, who): 
        self.hp -= who.damage

    def alive(self): 
        return self.hp > 0
    
    def __invariant__(self):
        """Ensure that the internal state of the Person object is valid."""
        assert self.damage > 0, f"{self.name} must have damage greater than 0."
        assert self.hp >= 0, f"{self.name} has invalid HP: {self.hp} (should not be negative)."
        assert self.alive() == (self.hp > 0), f"{self.name}'s alive() function is incorrect."