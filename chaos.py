from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.graphics import Color, Ellipse
import random
import math

class Sphere(Widget):

    def __init__(self):
        # Let's describe some things about the sphere

        # What color is it?
        self.color = (random.random(), 1, 1)

        # How fast is it moving and in what direction?
        delta = [-1, 1]
        self.x_velocity = random.randint(2,5) * random.choice(delta)
        self.y_velocity = random.randint(2,5) * random.choice(delta)

        # How big is it?
        self.diameter = 30

        # Where is it?
        self.x_position = 0
        self.y_position = 0

        # Has it been destroyed?
        self.destroy = False

        # Is this sphere fixed, or moving around?
        self.fixed = False

    def updateSphere(self, canvas, game):
        # What kind of sphere is this? A moving one or an expanding one?
        if self.fixed:
            if self.destroy:
                self.contractSphere()
            else:
                self.expandSphere()
        else:
            self.moveSphere(game)

        # Sphere has been updated, redraw it
        with canvas:
            Color(*self.color, mode='hsv')
            self.e = Ellipse(pos=(self.x_position, self.y_position), size=(self.diameter, self.diameter))

    def moveSphere(self, game):
        self.x_position = self.x_position + self.x_velocity
        self.y_position = self.y_position + self.y_velocity
        if (self.y_position < 0) or (self.y_position + self.diameter > game.top):
            self.y_velocity *= -1
        if (self.x_position < 0) or (self.x_position + self.diameter > game.right):
            self.x_velocity *= -1

    def expandSphere(self):
        if self.diameter > 0 and self.diameter < 300:
            self.diameter = self.diameter + 1
            self.x_position = self.x_position - 1 + math.pow(1/math.sqrt(2), 2)
            self.y_position = self.y_position - 1 + math.pow(1/math.sqrt(2), 2)
        else:
            self.destroy = True

    def contractSphere(self):
        if self.diameter > 0:
            self.diameter = self.diameter - 4
            self.x_position = self.x_position + 2 + math.pow(1/2*math.sqrt(32), 2)
            self.y_position = self.y_position + 2 + math.pow(1/2*math.sqrt(32), 2)

    def collidingWith(self, otherSphere):
        deltax = (otherSphere.x_position+otherSphere.diameter/2) - (self.x_position + self.diameter/2)
        deltay = (otherSphere.y_position+otherSphere.diameter/2) - (self.y_position+self.diameter/2)
        distance = math.sqrt(math.pow(deltax, 2) + math.pow(deltay, 2))
        if distance < (otherSphere.diameter/2 + self.diameter/2):
            return True


class Chaos(Widget):
    spheres = []
    hasClicked = False

    def initialize(self):
        for i in range(50):
            s = Sphere()
            s.x_position = random.random() * 1000
            s.y_position = random.random() * 1000
            self.spheres.append(s)

    def updateSphereGraphics(self):
        for s in self.spheres:
            s.updateSphere(self.canvas, self)

    def checkForSphereCollisions(self):
        for s in self.spheres:
            if s.diameter > 5:
                for other in self.spheres:
                    if other.diameter > 5:
                        if s != other and s.fixed == True and s.collidingWith(other):
                            other.fixed = True

    def update(self, dt):
        # Clear out our drawing space
        self.canvas.clear()

        # Update the sphere graphics
        self.updateSphereGraphics()

        # Check for sphere collisions
        self.checkForSphereCollisions()


    def on_touch_down(self, mouseClickPosition):
        if not self.hasClicked:
            # Create a new sphere
            s = Sphere()

            # Place it on the location we clicked
            s.x_position = mouseClickPosition.x - 15
            s.y_position = mouseClickPosition.y - 15

            # Is this sphere fixed in position? Yes it is.
            s.fixed = True

            # Add this sphere to our list of spheres
            self.spheres.append(s);

            # Note that we used our one click so that we can't click again
            self.hasClicked = True

class ChaosApp(App):
    def build(self):
        game = Chaos()
        game.initialize()
        Clock.schedule_interval(game.update, (1/60))
        return game

if __name__ == '__main__':
    ChaosApp().run()
