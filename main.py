import pygame
import maze

class Main():
    # General settings
    screen_width = 800
    screen_height = 600

    maze = maze.Maze((50, 50))
    print(maze)

    # Running flag for main loop
    running = True

    ## Handle events 
    def events(self):
        for event in pygame.event.get():
            if event == pygame.QUIT:
                break

    ## Update logic in the program.
    def update(self):
        pass

    def postupdate(self):
        pass
    
    def render(self):
        pass
        
    ## Called when the program requires cleanup
    def close(self):
        pygame.quit()

    ## Runs initialization for pygame and other required libraries
    def initialize(self):
        # Initialize PyGame
        pygame.init()
        # Setup a PyGame Screen for rendering.
        screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height))
    
    ## The constructor for the class
    def __init__(self):
        self.initialize()
        while self.running:
            self.update()
            self.render()
            self.postupdate()
        self.close()

main = Main()
