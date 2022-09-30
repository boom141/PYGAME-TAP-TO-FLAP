import random
from setup import*
from sprite_groups import*
from environment import*
from player import*


def game():
	last_time = time.time()
	running = True

	player = Player('brian')
	pipe = Pipes(1,[510, int(130 + random.randint(1,12) * 10)])
	pipes.add(pipe)
	ground = Ground(1,0)
	grounds.add(ground)

	while running:
		delta_time = time.time() - last_time
		delta_time *= 60
		last_time = time.time()
		
		display.fill((25,25,25))
		
# slide --------------------------------------------------------------------------#
		horizontal_scroll = 0
		horizontal_scroll -= 1.5 * delta_time 


		for pipe in pipes:
			pipe.update(horizontal_scroll)
			pipe.collision(player)
			pipe.draw(display)

		grounds.update(1,horizontal_scroll)
		grounds.draw(display)

		player.update(delta_time)
		player.draw(display)
		
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