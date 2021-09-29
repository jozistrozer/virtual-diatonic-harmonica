import pygame

pygame.init()

# Konstante
WIDTH = 1024
HEIGHT = 768
white = (255, 255, 255)
black = (0, 0, 0)
red = (200, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 255)

# Inicializacija prikaza.
display = pygame.display.set_mode((WIDTH, HEIGHT))

# Zvok
pygame.mixer.pre_init(frequency=44100, size=-16, channels=8, buffer=512)
pygame.mixer.init()

def funUstvariZvok(nota):
    sound = pygame.mixer.Sound('zvok/' + nota + '.wav')
    sound.set_volume(0.05)
    return sound

# Shema: ["tipka na tipkovnici", "nota - not", "nota - ven"]
tipke = [
    # 1. vrsta
    ["2", funUstvariZvok('F4'), funUstvariZvok('A4')],
    ["3", funUstvariZvok('A#4'), funUstvariZvok('D#5')],
    ["4", funUstvariZvok('D5'), funUstvariZvok('F5')],
    ["5", funUstvariZvok('F5'), funUstvariZvok('A5')],
    ["6", funUstvariZvok('A#5'), funUstvariZvok('C6')],
    ["7", funUstvariZvok('D6'), funUstvariZvok('D#6')],
    ["8", funUstvariZvok('F6'), funUstvariZvok('F6')],
    ["9", funUstvariZvok('A#6'), funUstvariZvok('A6')],
    ["0", funUstvariZvok('D7'), funUstvariZvok('C7')],
    ["'", funUstvariZvok('F7'), funUstvariZvok('D#7')],
    ["+", funUstvariZvok('A#7'), funUstvariZvok('G7')],
    ["backspace", funUstvariZvok('D8'), funUstvariZvok('A7')],

    # 2. vrsta
    ["q", funUstvariZvok('C4'), funUstvariZvok('E4')],
    ["w", funUstvariZvok('F4'), funUstvariZvok('A#4')],
    ["e", funUstvariZvok('A4'), funUstvariZvok('C5')],
    ["r", funUstvariZvok('C5'), funUstvariZvok('E5')],
    ["t", funUstvariZvok('F5'), funUstvariZvok('G5')],
    ["z", funUstvariZvok('A5'), funUstvariZvok('A#5')],
    ["u", funUstvariZvok('C6'), funUstvariZvok('C6')],
    ["i", funUstvariZvok('F6'), funUstvariZvok('E6')],
    ["o", funUstvariZvok('A6'), funUstvariZvok('G6')],
    ["p", funUstvariZvok('C7'), funUstvariZvok('A#6')],
    ["š", funUstvariZvok('F7'), funUstvariZvok('D7')],
    ["đ", funUstvariZvok('A7'), funUstvariZvok('E7')],
    ["return", funUstvariZvok('C8'), funUstvariZvok('G7')],

    # 3. vrsta
    ["a", funUstvariZvok('C4'), funUstvariZvok('F4')],
    ["s", funUstvariZvok('E4'), funUstvariZvok('G4')],
    ["d", funUstvariZvok('G4'), funUstvariZvok('B4')],
    ["f", funUstvariZvok('C5'), funUstvariZvok('D5')],
    ["g", funUstvariZvok('E5'), funUstvariZvok('F5')],
    ["h", funUstvariZvok('G5'), funUstvariZvok('A5')],
    ["j", funUstvariZvok('C6'), funUstvariZvok('B5')],
    ["k", funUstvariZvok('E6'), funUstvariZvok('D6')],
    ["l", funUstvariZvok('G6'), funUstvariZvok('F6')],
    ["č", funUstvariZvok('C7'), funUstvariZvok('A6')],
    ["ć", funUstvariZvok('E7'), funUstvariZvok('B6')],
    ["ž", funUstvariZvok('G7'), funUstvariZvok('D7')],
]


def funIgrajZvok(tipka, tip, meh):
    for infoTipka in tipke:
        if infoTipka[0] == tipka:
            if tip == "play":
                if meh == "noter":
                    infoTipka[1].play(loops=-1)
                else:
                    infoTipka[2].play(loops=-1)
            else:
                infoTipka[1].stop()
                infoTipka[2].stop()

# Glavni razred.
class MainGame:
    def __init__(self):
        self.main()

    def main(self):
        loop = True
        meh = "noter"
        while loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit(1)

                if event.type == pygame.KEYDOWN:
                    funIgrajZvok(pygame.key.name(event.key), "play", meh)

                if event.type == pygame.KEYUP:
                    funIgrajZvok(pygame.key.name(event.key), "stop", meh)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        meh = "ven"
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        meh = "noter"


            display.fill(white)
            pygame.display.update()
MainGame()