class Sphere(Widget):

    def __init__(self):
        # Let's describe some things about the sphere
        # What color is it?
        # How fast is it moving and in what direction?
        # How big is it?
        # Where is it?
        # Has it been destroyed?
        # Is this sphere fixed, or moving around?

    def updateSphere(self, canvas, game):
        # What kind of sphere is this? A moving one or an expanding one?
        # If it's a fixed sphere, is it expanding or contracting?
        # Otherwise, move the sphere

        # Since we updated the sphere Sphere we need to redraw it

    def moveSphere(self, game):
        # How does the sphere move?
        # Change the x position of the sphere based on the x velocity
        # Change the y position of the sphere based on the y velocity
        # If the sphere touches the top edge of the screen or the bottom edge, flip the y velocity from positive to negative or negative to positive
        # If the sphere touches the left edge of the screen or the right edge, flip the x velocity from positive to negative or negative to positive

    def expandSphere(self):
        # How does the sphere expand?
        # As long as the sphere has a diameter greater than zero, but less than the maximum size of the sphere
        # increase its diameter.
        # If the sphere has reached its maximum diameter, set the destroy flag to true.

    def contractSphere(self):
        # How does the sphere contract?
        # As long as the diameter is greater than zero, reduce the diameter of the sphere.

    def collidingWith(self, otherSphere):
        # Is this sphere colliding with another sphere?
        # If the distance between the two spheres is less than their combined radii, we have a collision


class Chaos(Widget):
    # Set up some parameters for our game
    # We need a list of spheres
    # We need a flag recording whether or not we clicked the board. We only get one click
    # so once we click, we can't click again.

    def initialize(self):
        # Initilize the game
        # Create some number of spheres
        # Place them randomly across the board
        # Add the newly created sphere to the list

    def updateSphereGraphics(self):
        # For every sphere in our list, run the code to update the sphere's graphics.

    def checkForSphereCollisions(self):
        # For every sphere in our list, compare it to every other sphere in the list
        # Run the colliding with code from the sphere object

    def update(self, dt):
        # Clear out our drawing space

        # Update the sphere graphics

        # Check for sphere collisions


    def on_touch_down(self, mouseClickPosition):
        # If we haven't already used our click
        # Create a new sphere
        # Place it on the location we clicked

        # Is this sphere fixed in position? Yes it is.
        # Add this sphere to our list of spheres
        # Note that we used our one click so that we can't click again

class ChaosApp(App):
    def build(self):
        # Create a new instance of our game
        game = Chaos()

        # Run the initialization code
        game.initialize()

        # The clock runs our game. This code tells us that the clock is going to tick 60 times per second.
        Clock.schedule_interval(game.update, (1/60))
        return game

if __name__ == '__main__':
    ChaosApp().run()
