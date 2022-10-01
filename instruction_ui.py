from setup import*

class Instruction(pygame.sprite.Sprite):
    def __init__(self,chracter):
        pygame.sprite.Sprite.__init__(self)
        self.chracter = chracter
        self.image_char = None
        self.image_spacebar = None
        self.font = pygame.font.Font(os.path.join('fonts','Minecraft.ttf'),20)
        self.frame_count = 0
    
    def draw(self,surface,delta_time):

        self.frame_count += 0.09 * delta_time
        if self.frame_count > 2:
            self.frame_count = 0
        
        text = self.font.render('Pressed Space key To Flap',False,'white')
        self.image_char = pygame.image.load(os.path.join(f'characters/{self.chracter}', f'{int(self.frame_count)}.png'))
        self.image_spacebar = pygame.image.load(os.path.join(f'ui/spacebar', f'{int(self.frame_count)}.png'))

        surface.blit(self.image_char,(175,150))
        surface.blit(self.image_spacebar,(140,300))
      