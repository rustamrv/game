import pygame as p

class Menu:

    def __init__(self, list):
        self.list = list
        self.point = 0 
        self.color = (255, 0, 0)
        self.background = (0, 0, 0)
        self.music = '1.mp3'
        self.font =  p.font.Font(p.font.get_default_font(), 50)

    def render(self, window): 
        for i in self.list:  
          
            if str(self.point) == i:  
                window.blit(self.font.render(self.list[i]["text"], 1, self.list[i]["background"]),
                            (self.list[i]["x"], self.list[i]["y"]))
            else:
                window.blit(self.font.render(self.list[i]["text"], 1, self.list[i]["color"]),
                            (self.list[i]["x"], self.list[i]["y"]))

    def ask(self, window, question):
        p.font.init()
        text = ""
        self.inputText(window, question + ": " + text)
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
            self.inputText(window, question + ": " + text)

        return text

    def position(self, connect, window, play, enemy, basic, set_menu):

        if self.point == 0:
            # start = connect.SearchName(play, enemy, basic)
            return True
        elif self.point == 1:
            name = self.ask(window, "What is your name?")
            print('n', name)
            # connect.SetName(name)
            return False
        elif self.point == 2:
            name = self.ask(window, "What is your name?")
            print(',', name)
            # connect.SetName(name)
            # connect.SearchName(play, enemy, basic)
        elif self.point == 3:
            self.setList(set_menu)
            self.Setting(window, play, enemy, basic)

    def setList(self, list):
        self.list = list

    def menu(self, window): 
        done = True
        while done: 
            window.fill((0, 100, 200))
            self.render(window)
            for e in p.event.get():   
                if e.type ==p.KEYDOWN:
                    if e.key == p.K_UP: 
                        if self.point > 0:
                            self.point -= 1   
                    elif e.key == p.K_DOWN: 
                        if self.point < 4:
                            self.point += 1  
                    if e.key == p.K_SPACE:
                       done = False
                       return True
                if e.type == p.QUIT:   
                    exit() 
                p.display.update()
                p.display.flip() 
                
        #     if self.point != 3:
        #         window.fill((0, 100, 200))
        #    

                # for e in p.event.get():
                #     if e.type == p.KEYDOWN:
                #         if e.key == p.K_UP:
                #             if point > 0:
                #                 point -= 1
                #         if e.key == p.K_DOWN:
                #             if point < len(self.list) - 1:
                #                 point += 1
                #         if e.key == p.K_SPACE and point == 0:
                #             done = False
                #             self.point = point
                #         if e.key == p.K_SPACE and point == 1:
                #             done = False
                #             self.point = point
                #             # save game sql

                #         if e.key == p.K_SPACE and point == 2:
                #             done = False
                #             self.point = point
                #         if e.key == p.K_SPACE and point == 3:
                #             done = False
                #             self.point = point
                #         if e.key == p.K_SPACE and point == 4:
                #             self.point = point
                #             exit()

                #     if e.type == p.MOUSEBUTTONDOWN and e.button == 1:
                #         if point == 0:
                #             done = False
                

    def inputText(self, window, message):

        window.fill((0, 100, 200))
        rect = p.Rect([50, 200, 180, 25])

        center = window.get_rect().left
        rect.left = center

        if len(message) != 0:
            window.blit(self.font.render(message, 1, (255, 255, 224)), rect.topleft)
        p.display.flip()

    def Setting(self, window, play, enemy, basic):
        done = True
        point = 0
        list = ["green", "red", "blue"]
        value = [(124, 252, 0), (255, 0, 0), (0, 0, 255)]
        list_music = ["First", "two", "three"]
        value_music = ['1.mp3', '2.mp3', '3.mp3']
        id_color = 0
        id_music = 0
        while done:
            window.fill((0, 100, 200))
            self.render(window, self.font, point)

            for e in p.event.get():
                if e.type == p.KEYDOWN:
                    if e.key == p.K_UP:
                        point -= 1
                    if e.key == p.K_DOWN:
                        point += 1
                    if e.key == p.K_SPACE:

                        if point == 0:
                            self.color = value[id_color]
                            play.getShape().setColor(value[id_color])
                            enemy.getShape().setColor(value[id_color])
                        elif point == 1:
                            self.background = value[id_color]
                            basic.setColor(value[id_color])
                        elif point == 2:
                            self.music = value_music[id_music]
                        self.point = point
                    if e.key == p.K_SPACE and point == 3:
                        self.point = point
                        done = False
                    elif e.key == p.K_LEFT:
                        id_color -= 1
                        id_music -= 1
                        if id_color < 0:
                            id_color = 2
                        if id_music < 0:
                            id_music = 2
                        if point == 0:
                            self.list['0']["Text"] = "Color men " + list[id_color]

                        elif point == 1:
                            self.list['1']["Text"] = "Background " + list[id_color]
                        elif point == 2:
                            self.list['2']["Text"] = "Music " + list_music[id_music]
                    elif e.key == p.K_RIGHT:
                        id_color += 1
                        id_music += 1
                        if id_color > len(list) - 1:
                            id_color = 0
                        if id_music > len(list_music) - 1:
                            id_music = 0
                        if point == 0:
                            self.list['0']["Text"] = "Color men " + list[id_color]

                        elif point == 1:
                            self.list['1']["Text"] = "Background " + list[id_color]
                        elif point == 2:
                            self.list['2']["Text"] = "Music " + list_music[id_music]
                if e.type == p.MOUSEBUTTONDOWN and e.button == 1:
                    if point == 3:
                        done = False

            p.display.flip()

