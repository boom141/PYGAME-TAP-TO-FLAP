import random
from setup import*
from sprite_groups import*
from environment import*
from player import*
from instruction_ui import*

def game():
	last_time = time.time()
	running = True
	instruction = True

	player = Player('brian')
	pipe = Pipes(1,[550, int(130 + random.randint(1,12) * 10)],1)
	pipes.add(pipe)
	ground = Ground(1,0)
	grounds.add(ground)
	instruction = Instruction('brian')
	
	slide_value = 1.5
	
	while running:
		delta_time = time.time() - last_time
		delta_time *= 60
		last_time = time.time()
		
		display.fill((25,25,25))
		
# slide ------------------------------  --------------------------------------------#
		horizontal_scroll = 0
		horizontal_scroll -= slide_value * delta_time 

		if instruction == False:
			for pipe in pipes:
				pipe.update(horizontal_scroll)
				if pipe.collision(player):
					slide_value = 0
				pipe.points(player)
				pipe.draw(display)

			player.update(delta_time)
			player.draw(display)

			grounds.update(horizontal_scroll)
			grounds.draw(display)
		else:
			instruction.draw(display,delta_time)
			grounds.update(horizontal_scroll)
			grounds.draw(display)
		
		if pygame.key.get_pressed()[K_SPACE]:
			instruction = False
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pygame.quit()
					sys.exit()

		window.blit(pygame.transform.scale(display,RESOLUTION),(0,0))
		pygame.display.update()
		clock.tick(FPS)

game()