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
    sound.set_volume(0.5)
    return sound

# Shema: ["tipka na tipkovnici", "nota - not", "nota - ven", boolean, vrsta]
tipke = [
    # 1. vrsta
    ["2", funUstvariZvok('F4'), funUstvariZvok('A4'), False, 1],
    ["3", funUstvariZvok('A#4'), funUstvariZvok('D#5'), False, 1],
    ["4", funUstvariZvok('D5'), funUstvariZvok('F5'), False, 1],
    ["5", funUstvariZvok('F5'), funUstvariZvok('A5'), False, 1],
    ["6", funUstvariZvok('A#5'), funUstvariZvok('C6'), False, 1],
    ["7", funUstvariZvok('D6'), funUstvariZvok('D#6'), False, 1],
    ["8", funUstvariZvok('F6'), funUstvariZvok('F6'), False, 1],
    ["9", funUstvariZvok('A#6'), funUstvariZvok('A6'), False, 1],
    ["0", funUstvariZvok('D7'), funUstvariZvok('C7'), False, 1],
    ["'", funUstvariZvok('F7'), funUstvariZvok('D#7'), False, 1],
    ["+", funUstvariZvok('A#7'), funUstvariZvok('G7'), False, 1],
    ["backspace", funUstvariZvok('D8'), funUstvariZvok('A7'), False, 1],

    # 2. vrsta
    ["q", funUstvariZvok('C4'), funUstvariZvok('E4'), False, 2],
    ["w", funUstvariZvok('F4'), funUstvariZvok('A#4'), False, 2],
    ["e", funUstvariZvok('A4'), funUstvariZvok('C5'), False, 2],
    ["r", funUstvariZvok('C5'), funUstvariZvok('E5'), False, 2],
    ["t", funUstvariZvok('F5'), funUstvariZvok('G5'), False, 2],
    ["z", funUstvariZvok('A5'), funUstvariZvok('A#5'), False, 2],
    ["u", funUstvariZvok('C6'), funUstvariZvok('C6'), False, 2],
    ["i", funUstvariZvok('F6'), funUstvariZvok('E6'), False, 2],
    ["o", funUstvariZvok('A6'), funUstvariZvok('G6'), False, 2],
    ["p", funUstvariZvok('C7'), funUstvariZvok('A#6'), False, 2],
    ["š", funUstvariZvok('F7'), funUstvariZvok('D7'), False, 2],
    ["đ", funUstvariZvok('A7'), funUstvariZvok('E7'), False, 2],
    ["return", funUstvariZvok('C8'), funUstvariZvok('G7'), False, 2],

    # 3. vrsta
    ["a", funUstvariZvok('C4'), funUstvariZvok('F4'), False, 3],
    ["s", funUstvariZvok('E4'), funUstvariZvok('G4'), False, 3],
    ["d", funUstvariZvok('G4'), funUstvariZvok('B4'), False, 3],
    ["f", funUstvariZvok('C5'), funUstvariZvok('D5'), False, 3],
    ["g", funUstvariZvok('E5'), funUstvariZvok('F5'), False, 3],
    ["h", funUstvariZvok('G5'), funUstvariZvok('A5'), False, 3],
    ["j", funUstvariZvok('C6'), funUstvariZvok('B5'), False, 3],
    ["k", funUstvariZvok('E6'), funUstvariZvok('D6'), False, 3],
    ["l", funUstvariZvok('G6'), funUstvariZvok('F6'), False, 3],
    ["č", funUstvariZvok('C7'), funUstvariZvok('A6'), False, 3],
    ["ć", funUstvariZvok('E7'), funUstvariZvok('B6'), False, 3],
    ["ž", funUstvariZvok('G7'), funUstvariZvok('D7'), False, 3],
]

# Slike
slikaHarmonika = pygame.image.load('slike/harmonika.png')

# Pozicije
pos1 = [800, 625]
pos2 = (835, 642)
pos3 = (870, 625)


def funIgrajZvok(tipka, tip, meh):
    for infoTipka in tipke:
        if infoTipka[0] == tipka:
            infoTipka[3] = True
            if tip == "play":
                if meh == "noter":
                    infoTipka[1].play(loops=-1)
                else:
                    infoTipka[2].play(loops=-1)
            else:
                infoTipka[1].stop()
                infoTipka[2].stop()
        else:
            infoTipka[3] = False

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
            # Harmonika
            display.blit(slikaHarmonika, (0, 0))

            # Tipke
            varPosY1 = pos1[1]
            varPosY2 = pos2[1]
            varPosY3 = pos3[1]
            for tipka in tipke:
                if tipka[3]:
                    default_color = (128, 128, 128)
                else:
                    default_color = white
                if tipka[4] == 1:
                    pygame.draw.circle(display, black, (pos1[0], varPosY1), 15)
                    pygame.draw.circle(display, default_color, (pos1[0], varPosY1), 13)
                    varPosY1 -= 35

                if tipka[4] == 2:
                    pygame.draw.circle(display, black, (pos2[0], varPosY2), 15)
                    pygame.draw.circle(display, default_color, (pos2[0], varPosY2), 13)
                    varPosY2 -= 35

                if tipka[4] == 3:
                    pygame.draw.circle(display, black, (pos3[0], varPosY3), 15)
                    pygame.draw.circle(display, default_color, (pos3[0], varPosY3), 13)
                    varPosY3 -= 35


            pygame.display.update()



MainGame()