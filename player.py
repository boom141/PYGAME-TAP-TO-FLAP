from setup import*
from sound_music import*

class Player(pygame.sprite.Sprite):
    def __init__(self,current_character):
        pygame.sprite.Sprite.__init__(self)
        self.current_character = current_character
        self.frames = []
        self.frame_count = 0
        self.image = pygame.image.load(os.path.join(f'characters/{current_character}', '0.png'))
        self.image_copy = self.image.copy()
        self.rect = self.image_copy.get_rect(center = (130,200))
        self.vertical_momentum = 0
        self.jump_value = -2
        self.y_value = 0.2
        self.jump_cooldown = 0
        self.frame_speed = 0.2
        self.free_fall = 0
        self.hit_box = self.rect.copy()
        self.hit = False
        self.state = 'flying'
        self.score = 0
        self.font = pygame.font.Font(os.path.join('fonts','04B_19__.TTF'),45)
        self.sounds = -1

    def fly(self,delta_time):
        if self.jump_cooldown > 0:
            self.jump_cooldown -= 1
        
        if pygame.key.get_pressed()[K_SPACE] and self.hit == False:
            if self.jump_cooldown == 0:
                # Sfx_Sound('sounds/fly1.wav').play_sound(0)
                self.free_fall = 0
                self.vertical_momentum = self.jump_value
                self.frame_count = 0

        self.rect.centery += self.vertical_momentum * delta_time
        self.vertical_momentum += self.y_value
        self.free_fall += self.y_value

        if self.rect.bottom >= 425:
            self.rect.bottom = 425
            self.jump_value = 0
            self.frame_speed = 0
            self.hit = True

        if self.hit and self.sounds == -1:
            self.sounds = 0
            Sfx_Sound('sounds/hit.wav').play_sound(0)

    def update(self,delta_time):
        self.fly(delta_time)

        self.frames = os.listdir(f'characters/{self.current_character}')
        self.frame_count += self.frame_speed * delta_time
        if self.frame_count >= (len(self.frames) - 2):
            self.frame_count = (len(self.frames) - 2)


        self.image = pygame.image.load(os.path.join(f'characters/{self.current_character}',self.frames[int(self.frame_count)]))
        self.image_copy = self.image.copy()
        self.image_copy = pygame.transform.scale(self.image,(100,70))
    
        self.hit_box = self.rect.copy()
        self.hit_box.width = 30
        self.hit_box.height = 55
        self.hit_box.x = self.rect.x + 35
        self.hit_box.y = self.rect.y + 10

    def draw(self,surface):
        #pygame.draw.rect(surface, 'green', self.hit_box, 1)
        text = self.font.render(f'{self.score}',False,'white')
        surface.blit(text,(230,15))   
        surface.blit(self.image_copy,self.rect)