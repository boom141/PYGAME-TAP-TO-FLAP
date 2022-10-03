from setup import*


class Game_Over():
    def __init__(self):
        self.font1_outline = pygame.font.Font(os.path.join('fonts','04B_19__.TTF'),158)
        self.font1 = pygame.font.Font(os.path.join('fonts','04B_19__.TTF'),150)
        self.font2_outline = pygame.font.Font(os.path.join('fonts','04B_19__.TTF'),31)
        self.font2 = pygame.font.Font(os.path.join('fonts','04B_19__.TTF'),30)
        self.click = -1
        self.animate1 = 0
        self.animate2 = 0
        self.current_score = 0
        self.high_score = 85
        self.offset = 0
        self.action = -1
    
    def draw(self,surface,player,delta_time):
        self.play_btn = pygame.image.load(os.path.join(f'ui/playbtn', f'{self.animate1}.png'))
        self.play_btn = pygame.transform.scale(self.play_btn,(150,50))
        self.quit_btn = pygame.image.load(os.path.join(f'ui/quitbtn', f'{self.animate2}.png'))
        self.quit_btn = pygame.transform.scale(self.quit_btn,(150,50))


        if self.action == 0:
           return True
        if self.action == 1:
            return False


        self.current_score += 0.2 * delta_time
        if self.current_score >= player.score:
            self.current_score = player.score

        outline1 = self.font1_outline.render(f'{int(self.current_score)}', False, ((33,33,35)))
        score = self.font1.render(f'{int(self.current_score)}', False, 'white')
        outline2 = self.font2_outline.render(f'HIGH SCORE:{self.high_score}', False, ((33,33,35)))
        highscore = self.font2.render(f'HIGH SCORE:{self.high_score}', False, 'white')


        if self.current_score > 9:
            self.offset = 30
        else:
            self.offset = 0

        surface.blit(outline1,(217 - self.offset, 170))
        surface.blit(score,(217 - self.offset, 170))
        surface.blit(outline2,(148, 317))
        surface.blit(highscore,(150, 315))
        btn1 = surface.blit(self.play_btn,(90,390))
        btn2 = surface.blit(self.quit_btn,(270,390))

        buttons = [btn1,btn2]

        for button in buttons:
            if button.collidepoint(pygame.mouse.get_pos()):
                if pygame.mouse.get_pressed()[0]:
                    self.action = buttons.index(button)
        
    