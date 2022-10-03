import random
from setup import*
from sound_music import Sfx_Sound
from sprite_groups import*

class Ground(pygame.sprite.Sprite):
    def __init__(self,theme,initial_x):
        pygame.sprite.Sprite.__init__(self)
        self.theme = theme
        self.image = pygame.image.load(os.path.join('environment','ground.png'))
        self.rect = self.image.get_rect(x=initial_x,y=400)

    def update(self,horizontal_scroll):
        self.rect.right += horizontal_scroll
        if self.rect.left < 0:
            ground = Ground(self.theme,self.rect.right)
            if len(grounds) < 2 :
                grounds.add(ground)
        if self.rect.right < 0:
            self.kill()
        

class Pipes(pygame.sprite.Sprite):
    def __init__(self,theme,position,pipe_num):
        pygame.sprite.Sprite.__init__(self)
        self.pipe_num = pipe_num
        self.theme = theme
        self.upper_pipe = pygame.image.load(os.path.join('environment','large_upper_pipe.png'))
        self.upper_pipe_rect = self.upper_pipe.get_rect(x=position[0],y=-position[1])
        self.lower_pipe = pygame.image.load(os.path.join('environment','large_lower_pipe.png'))
        self.lower_pipe_rect = self.upper_pipe.get_rect(x=position[0],y=self.upper_pipe_rect.bottom + 110)
        self.spawn = -1
        self.score = 0
        self.font = pygame.font.Font(os.path.join('fonts','digitalix.ttf'),30)
        self.sounds = -1


    def collision(self,player):
        if (player.hit_box.colliderect(self.upper_pipe_rect) or 
            player.hit_box.colliderect(self.lower_pipe_rect)):
                player.hit = True
                return True
       
    
    def points(self,player):
        if player.rect.left > self.upper_pipe_rect.right and self.sounds == -1:
            self.sounds = 0
            Sfx_Sound('sounds/points1.wav').play_sound(0)
            player.score = self.pipe_num

    def update(self,horizontal_scroll):
        self.upper_pipe_rect.right += horizontal_scroll
        self.lower_pipe_rect.right += horizontal_scroll

        if self.upper_pipe_rect.right < 500 and self.spawn == -1:
            self.spawn = 0
            pipe = Pipes(1,[self.upper_pipe_rect.right + 120, int(130 + random.randint(1,12) * 10)],self.pipe_num + 1)
            pipes.add(pipe)

        if self.upper_pipe_rect.right < 0:
            self.kill()
        
    def draw(self,surface):
        # pygame.draw.rect(surface, 'green', self.upper_pipe_rect, 1)
        # pygame.draw.rect(surface, 'green', self.lower_pipe_rect, 1)
        surface.blit(self.upper_pipe,(self.upper_pipe_rect.x,self.upper_pipe_rect.y))
        surface.blit(self.lower_pipe,(self.lower_pipe_rect.x,self.lower_pipe_rect.y))




class Layer3(pygame.sprite.Sprite):
    def __init__(self,theme,position):
        pygame.sprite.Sprite.__init__(self)
        self.theme = theme
        self.layer3 = pygame.image.load(os.path.join('bg','layer3.png'))
        self.layer3_rect = self.layer3.get_rect(x=position[0],y=position[1])
        self.spawn = -1
        
    def update(self,horizontal_scroll):
        self.layer3_rect.right += horizontal_scroll / 3
        if self.layer3_rect.left < 0 and self.spawn == -1:
            self.spawn = 0
            layer3 = Layer3(self.theme,[self.layer3_rect.right,self.layer3_rect.y])
            layers[0].add(layer3)

        if self.layer3_rect.right < 0:
            self.kill()

    def draw(self,surface):
        surface.blit(self.layer3, self.layer3_rect)



class Layer2(pygame.sprite.Sprite):
    def __init__(self,theme,position):
        pygame.sprite.Sprite.__init__(self)
        self.theme = theme
        self.position = position
        self.layer2 = pygame.image.load(os.path.join('bg','layer2.png'))
        self.layer2_rect = self.layer2.get_rect(x=position[0],y=position[1])
        self.spawn = -1
        
    def update(self,horizontal_scroll):
        self.layer2_rect.right += horizontal_scroll / 2
        if self.layer2_rect.left < 0 and self.spawn == -1:
            self.spawn = 0
            layer2 = Layer2(self.theme,[self.layer2_rect.right,self.layer2_rect.y])
            layers[1].add(layer2)

        if self.layer2_rect.right < 0:
            self.kill()

    def draw(self,surface):
        surface.blit(self.layer2, self.layer2_rect)


class Layer1(pygame.sprite.Sprite):
    def __init__(self,theme,position):
        pygame.sprite.Sprite.__init__(self)
        self.theme = theme
        self.layer1 = pygame.image.load(os.path.join('bg','layer1.png'))
        self.layer1_rect = self.layer1.get_rect(x=position[0],y=position[1])
        self.spawn = -1
        
    def update(self,horizontal_scroll):
        self.layer1_rect.right += horizontal_scroll
        if self.layer1_rect.left < 0 and self.spawn == -1:
            self.spawn = 0
            layer1 = Layer1(self.theme,[self.layer1_rect.right,self.layer1_rect.y])
            layers[2].add(layer1)

        if self.layer1_rect.right < 0:
            self.kill()

    def draw(self,surface):
        surface.blit(self.layer1, self.layer1_rect)