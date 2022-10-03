from setup import*

class Instruction(pygame.sprite.Sprite):
    def __init__(self,chracter):
        pygame.sprite.Sprite.__init__(self)
        self.chracter = chracter
        self.image_char = None
        self.image_spacebar = None
        self.font = pygame.font.Font(os.path.join('fonts','04B_19__.TTF'),80)
        self.font_outline = pygame.font.Font(os.path.join('fonts','04B_19__.TTF'),85)
        self.frame_count = 0
    
    def draw(self,surface,delta_time):

        self.frame_count += 0.09 * delta_time
        if self.frame_count > 2:
            self.frame_count = 0
        
        outline1 = self.font_outline.render('TAP IT',False,((33,33,35)))
        outline2 = self.font_outline.render('FLAP IT',False,((33,33,35)))
        text1 = self.font.render('TAP IT',False,'white')
        text2 = self.font.render('FLAP IT',False,'white')
        self.image_char = pygame.image.load(os.path.join(f'characters/{self.chracter}', f'{int(self.frame_count)}.png'))
        self.image_spacebar = pygame.image.load(os.path.join(f'ui/spacebar', f'{int(self.frame_count)}.png'))

        surface.blit(outline1,(133,45))
        surface.blit(outline2,(118,110))
        surface.blit(text1,(135,40))
        surface.blit(text2,(120,105))
        surface.blit(self.image_char,(175,210))
        surface.blit(self.image_spacebar,(140,320))
      