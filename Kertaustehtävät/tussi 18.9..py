class Tussi:
    def __init__(self, vari: str):
        self.vari = vari
        self.mustemaara = 5
        self.korkkipaalla = True
    def __repr__(self):
        return f"{self.vari}, {self.mustemaara}, {self.korkkipaalla}"
    def korkkikiinni(self):
        self.korkkipaalla = True
    def korkkiauki(self):
        self.korkkipaalla = False
    def piirra(self):
        if not self.korkkipaalla and self.mustemaara > 0:
            print(f"Piirrän {self.vari}")
            self.mustemaara = self.mustemaara - 1
            return True
        else:
            print("En piirrä!")
            return False




tussi = Tussi("Pinkki")
print(tussi)
tussi.korkkiauki()
print(tussi)

tussi.piirra()
print(tussi)
tussi.piirra()
tussi.piirra()
tussi.piirra()
tussi.piirra()
tussi.piirra()