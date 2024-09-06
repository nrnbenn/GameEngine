import pygame

class game():
    def __init__(self,size):
        #setup
        pygame.init()
        self.running = True
        self.screensize = size
        self.screen = pygame.display.set_mode(size)
        self.registeredgameobjects = []

    def registerobject(self,gameobject):
        self.registeredsprites.append(gameobject)

    def renderscreen(self):
        self.screen.fill((0,0,0))
        for object in self.registeredgameobjects:
            object.render()

    def update(self):
        self.renderscreen()
        pygame.display.flip()

class gameobject():
    def __init__(self):
        self.appearence = None
        self.position = position()
        self.updatebehaviours = []

    def render(self):
        pass

    def update(self):
        for behaviour in self.updatebehaviours:
            behaviour.run()

    def applyupdatebehaviour(self,behaviour):
        self.updatebehaviours.append(behaviour)


class appearance():
    def __init__(self):
        self.image = None

    def getimage(self):
        if self.image:
            return(self.image)
        
    def setimage(self):
        pass

class position():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.rotation = 0

class behaviour():
    def __init__(self,func):
        self.function = func

    def run():
        pass