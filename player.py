import pygame
#pickle is necessary to load our pickled frame values
import pickle
 
#Player extends the pygame.sprite.Sprite class
class Player(pygame.sprite.Sprite):
    #In the main program, we will pass a spritesheet and x-y position values to the constructor
    def __init__(self, position, spritesheet):
        pygame.sprite.Sprite.__init__(self)
       
        #Load our pickled frame values and assign them to dicts
        self.left_states = pickle.load(open("ls.dat", "rb"))
        self.right_states = pickle.load(open("rs.dat", "rb"))
        self.up_states = pickle.load(open("us.dat", "rb"))
        self.down_states = pickle.load(open("ds.dat", "rb"))
       
        #Assign the spritesheet to self.sheet
        self.sheet = pygame.image.load(spritesheet)
        #'Clip' the sheet so that only one frame is displayed (the first frame of down_states)
        self.sheet.set_clip(pygame.Rect(self.down_states[0]))
       
        #Create a rect to animate around the screen
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
       
        #Assign the position parameter value to the topleft x-y values of the rect
        self.rect.topleft = position
       
        #We'll use this later to cycle through frames
        self.frame = 0
        
        #We'll use these values to move our character
        self.change_x = 0
        self.change_y = 0

    '''The event handler handles keypresses for our class. If a key is pressed down
    or released, the appropriate 'state' is passed to the update
    method below.'''
    def handle_event(self, event):
      
        #Handles key presses
        if event.type == pygame.KEYDOWN:
        
            if event.key == pygame.K_LEFT:
                self.update('walk_left')
            if event.key == pygame.K_RIGHT:
                self.update('walk_right')
            if event.key == pygame.K_UP:
                self.update('walk_up')
            if event.key == pygame.K_DOWN:
                self.update('walk_down')
        
        #Handles key releases
        if event.type == pygame.KEYUP:  

            if event.key == pygame.K_LEFT:
                self.update('stand_left')            
            if event.key == pygame.K_RIGHT:
                self.update('stand_right')
            if event.key == pygame.K_UP:
                self.update('stand_up')
            if event.key == pygame.K_DOWN:
                self.update('stand_down')
                
    '''This method updates our character by passing the appropriate dict to the clip
    method below and moves our rect object. If the direction is left, for example, 
    the character moves -5 pixels on the x-plane.'''
    def update(self, direction):
        if direction == 'walk_left':
            self.clip(self.left_states)
            self.rect.x -= 5
        if direction == 'walk_right':
            self.clip(self.right_states)
            self.rect.x += 5
        if direction == 'walk_up':
            self.clip(self.up_states)
            self.rect.y -= 5
        if direction == 'walk_down':
            self.clip(self.down_states)
            self.rect.y +=5
        
        '''These checks are necessary in order to return our character to a standing
        position if no key is being pressed.'''
        if direction == 'stand_left':
            self.clip(self.left_states[0])
        if direction == 'stand_right':
            self.clip(self.right_states[0])
        if direction == 'stand_up':
            self.clip(self.up_states[0])
        if direction == 'stand_down':
            self.clip(self.down_states[0])

        #Update the image for earch pass
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        
    '''This method checks to see if it has been passed a dict or a single frame. If it is
    a dict (animated), it clips the rect via the get_frame method. If it is a single frame 
    (standing), it directly clips the frame.'''
    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect

    '''This method is used to cycle through frames. Since the 0th element of each frame set
    is a an image of the character standing (we don't want to use this), we will instead
    start at the 1st element.'''
    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 1
        return frame_set[self.frame]