import maze
import pygame


class GameLoop():
    # General settings
    screen_width = 800
    screen_height = 600

    # Running flag for main loop
    running = True
    font = None
    clock = pygame.time.Clock()

    m = maze.Maze((25, 25))
    
    # Handle events
    def events(self):
        # Check event queue
        for event in pygame.event.get():
            # Print the current event
            print(event)
            # Check if the event is a keydown event
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
            # Check if the event is a pygame quit event
            if event.type == pygame.QUIT:
                print("TRIED TO QUIT!")
                self.running = False

    # Update logic in the program.
    def update(self):
        self.fps = self.font.render(str(self.clock.get_fps()), 1, (255, 0, 0))

    def render(self):
        # Clear the display
        self.display.fill((0, 0, 0))
        # Blit the fps to the screen
        self.display.blit(self.fps, (0, 0))
        # Flip the buffers.
        pygame.display.flip()
        # Tick the clock for the fps counter
        self.clock.tick()

    # Called when the program requires cleanup
    def close(self):
        # Close the pygame instance and deload all modules
        pygame.quit()

    # Runs initialization for pygame and other required libraries
    def initialize(self):
        # Initialize PyGame
        pygame.init()
        # Setup a PyGame Screen for rendering.
        self.display = pygame.display.set_mode(
            (self.screen_width, self.screen_height)
        )

        self.font = pygame.font.Font(None, 24)

    # The constructor for the class
    def __init__(self):
        self.initialize()
        while self.running:
            self.events()
            self.update()
            self.render()
        self.close()


window = GameLoop()
