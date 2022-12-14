import random
from setup import*
from sprite_groups import*
from environment import*
from player import*
from instruction_ui import*
from game_over_ui import*

def game():
	last_time = time.time()
	running = True
	instruction = True

	player = Player('brian')
	pipe = Pipes(1,[550, int(130 + random.randint(1,12) * 10)],1)
	pipes.add(pipe)
	ground = Ground(1,0)
	grounds.add(ground)
	
	main_bg = pygame.image.load(os.path.join('bg','main.png'))

	layer3 = Layer3(1,[0,70])
	layers[0].add(layer3)

	layer2 = Layer2(1,[0,190])
	layers[1].add(layer2)

	layer1 = Layer1(1,[0,230])
	layers[2].add(layer1)

	instruction = Instruction('brian')
	game_over = Game_Over()

	slide_value = 2
	action = None

	while running:
		delta_time = time.time() - last_time
		delta_time *= 60
		last_time = time.time()
		
		display.fill((25,25,25))

		if action:
			for pipe in pipes:
				pipe.kill()
			for ground in grounds:
				ground.kill()
			game()
# slide ----------------------------------------------------------------------------#
		horizontal_scroll = 0
		horizontal_scroll -= slide_value * delta_time 

		display.blit(main_bg,(0,0))
		
		for layer in layers:
			for list in layer:
				list.update(horizontal_scroll)
				list.draw(display)
		
		if instruction == False:
			for pipe in pipes:
				pipe.update(horizontal_scroll)
				if pipe.collision(player):
					slide_value = 0
				pipe.points(player)
				pipe.draw(display)

			if player.fly(delta_time):
				slide_value = 0
			player.update(delta_time)
			player.draw(display)

			grounds.update(horizontal_scroll)
			grounds.draw(display)
			
		else:
			instruction.draw(display,delta_time)
			grounds.update(horizontal_scroll)
			grounds.draw(display)

		if slide_value == 0:
			action = game_over.draw(display,player,delta_time)
			
		
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
			
			if action == False:
				pygame.quit()
				sys.exit()

		window.blit(pygame.transform.scale(display,RESOLUTION),(0,0))
		pygame.display.update()
		clock.tick(FPS)

game()