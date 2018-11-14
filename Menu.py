import pygame as p

class Menu:

    def __init__(self, list={"0": {
        "x": 120,
        "y": 140,
        "Text": "Start",
        "Color": [250, 250, 30],
        "Color1": [120, 30, 30]
    }}):
        self.list = list
        self.point = 0
        self.color = (255, 0, 0)
        self.background = (0, 0, 0)
        self.music = '1.mp3'
        self.font = p.font.Font('12172.ttf', 50)

    def render(self, poverhnost, font, num_punkt):
        for i in self.list:
            if str(num_punkt) == i:
                poverhnost.blit(font.render(self.list[i]["Text"], 1, self.list[i]["Color1"]),
                                (self.list[i]["x"], self.list[i]["y"]))
            else:
                poverhnost.blit(font.render(self.list[i]["Text"], 1, self.list[i]["Color"]),
                                (self.list[i]["x"], self.list[i]["y"]))

    def ask(self, Window, question):
        p.font.init()
        text = ""
        self.inputText(Window, question + ": " + text)
        while True:
            p.time.wait(0)
            event = p.event.poll()

            if event.type != p.KEYDOWN:
                continue
            if event.key == p.K_BACKSPACE:
                text = text[0:-1]
            elif event.key == p.K_RETURN:
                break
            else:
                text += format(event.unicode)

            self.inputText(Window, question + ": " + text)

        return text

    def menu(self, Window):
        done = True
        point = 0
        while done:
            if self.point != 3:
                Window.fill((0, 100, 200))
                self.render(Window, self.font, str(point))

                for e in p.event.get():
                    if e.type == p.KEYDOWN:
                    # if e.key == p.K_ESCAPE:
                    #   done = False
                        if e.key == p.K_UP:
                            if point > 0:
                                point -= 1
                        if e.key == p.K_DOWN:
                            if point < len(self.list) - 1:
                                point += 1
                        if e.key == p.K_SPACE and point == 0:
                            done = False
                            self.point = point
                        if e.key == p.K_SPACE and point == 1:
                            done = False
                            self.point = point
                            # save game sql

                        if e.key == p.K_SPACE and point == 2:
                            done = False
                            self.point = point
                        if e.key == p.K_SPACE and point == 3:
                            done = False
                            self.point = point
                        if e.key == p.K_SPACE and point == 4:
                            self.point = point
                            exit()

                    if e.type == p.MOUSEBUTTONDOWN and e.button == 1:
                        if point == 0:
                            done = False
                    if self.point != 3:
                        p.display.flip()

    def inputText(self, Window, message):

        Window.fill((0, 100, 200))
        rect = p.Rect([50, 200, 180, 25])

        center = Window.get_rect().left
        rect.left = center

        if len(message) != 0:
            Window.blit(self.font.render(message, 1, (255, 255, 224)), rect.topleft)
        p.display.flip()

    def Setting(self, Window, Play, Enemy, basic):
        done = True
        point = 0
        list = ["green", "red", "blue"]
        value = [(124, 252, 0), (255, 0, 0), (0, 0, 255)]
        listMusic = ["First", "two", "three"]
        valueMusic = ['1.mp3', '2.mp3', '3.mp3']
        idColor = 0
        idMusic = 0
        while done:
            Window.fill((0, 100, 200))
            self.render(Window, self.font, point)

            for e in p.event.get():
                if e.type == p.KEYDOWN:
                    # if e.key == p.K_ESCAPE:
                    #   done = False
                    if e.key == p.K_UP:
                        point -= 1
                    if e.key == p.K_DOWN:
                        point += 1
                    if e.key == p.K_SPACE:

                        if point == 0:
                            self.color = value[idColor]
                            Play.setColor(value[idColor])
                            Enemy.setColor(value[idColor])
                        elif point == 1:
                            self.background = value[idColor]
                            basic.setColor(value[idColor])
                        elif point == 2:
                            self.music = valueMusic[idMusic]
                        self.point = point
                    if e.key == p.K_SPACE and point == 3:
                        self.point = point
                        done = False
                    elif e.key == p.K_LEFT:
                        idColor -= 1
                        idMusic -= 1
                        if idColor < 0:
                            idColor = 2
                        if idMusic < 0:
                            idMusic = 2
                        if point == 0:
                            self.list['0']["Text"] = "Color men " + list[idColor]

                        elif point == 1:
                            self.list['1']["Text"] = "Background " + list[idColor]
                        elif point == 2:
                            self.list['2']["Text"] = "Music " + listMusic[idMusic]
                    elif e.key == p.K_RIGHT:
                        idColor += 1
                        idMusic += 1
                        if idColor > len(list) - 1:
                            idColor = 0
                        if idMusic > len(listMusic) - 1:
                            idMusic = 0
                        if point == 0:
                            self.list['0']["Text"] = "Color men " + list[idColor]

                        elif point == 1:
                            self.list['1']["Text"] = "Background " + list[idColor]
                        elif point == 2:
                            self.list['2']["Text"] = "Music " + listMusic[idMusic]
                if e.type == p.MOUSEBUTTONDOWN and e.button == 1:
                    if point == 3:
                        done = False


            p.display.flip()

    def setPoint(self, start, point, window, point1):

        if self.point == 0:
            start = True
        elif self.point == 1:
            self.list = point
            self.Setting(window)
            if self.point == 3:
                self.list = point1
                self.menu(window)
                if self.point == 0:
                    start = True

        return start

    def ChangeMenu(self, window):
        self.menu(window)

        return self.point
