class TV:
    def __init__(self):
        self.kanava = 1
        self.volyymi = 5
        self.paalla = False
    def __repr__(self):
        return f"kanava={self.kanava}, volyymi={self.volyymi}, paalla={self.paalla}"
    def power(self):
        self.paalla = not self.paalla
    def kanavaplus(self):
        if self.paalla:
            if self.kanava == 5:
                self.kanava = 1
            else:
                self.kanava += self.kanava + 1


telkku = TV()
print(telkku)
telkku.power()
print(telkku)
print("vittu mitä paskaa")