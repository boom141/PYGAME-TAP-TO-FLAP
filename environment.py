import random
from setup import*
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


    def collision(self,player):
        if (player.hit_box.colliderect(self.upper_pipe_rect) or 
            player.hit_box.colliderect(self.lower_pipe_rect)):
                player.hit = True
                return True
       
    
    def points(self,player):
        if player.rect.left > self.upper_pipe_rect.right:
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
        
