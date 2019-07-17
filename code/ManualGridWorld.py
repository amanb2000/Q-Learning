import pygame, sys
import agent

agnt = agent.Agent()

pygame.init()

DISP = pygame.display.set_mode((800, 800)) # each grid box is 200x200px
pygame.display.set_caption('Grid World!')


run = True

WIDTH = 4
HEIGHT = 3
BLOCK_SIZE = 200

font = pygame.font.Font('freesansbold.ttf', 10)

def draw_agent(_agent):
	pygame.draw.rect(DISP, (255, 255, 255), ( (_agent.x*BLOCK_SIZE+BLOCK_SIZE*0.4), 
		(_agent.y*BLOCK_SIZE+BLOCK_SIZE*0.4), (BLOCK_SIZE*0.2), (BLOCK_SIZE*0.2) ))

def draw_grid(_agent):
	for i in range(WIDTH):
		for j in range(HEIGHT):

			pygame.draw.rect(DISP, (10, 10, 20), (i*BLOCK_SIZE+1, j*BLOCK_SIZE+1, BLOCK_SIZE-2, BLOCK_SIZE-2))

			for k in range(4):
				text = font.render(str(round(_agent.q_vals[i][j][k], 3)), True, (100, 100, 100), (10, 10, 20));
				textRect = text.get_rect()

				if(k == 0):
					textRect.center = ((i+0.5)*BLOCK_SIZE, (j+0.5)*BLOCK_SIZE - BLOCK_SIZE*0.4)

				elif(k == 1):
					textRect.center = ((i+0.5)*BLOCK_SIZE + BLOCK_SIZE*0.4, (j+0.5)*BLOCK_SIZE)

				elif(k == 2):
					textRect.center = ((i+0.5)*BLOCK_SIZE, (j+0.5)*BLOCK_SIZE + BLOCK_SIZE*0.4)

				elif(k == 3):
					textRect.center = ((i+0.5)*BLOCK_SIZE - BLOCK_SIZE*0.4, (j+0.5)*BLOCK_SIZE)

				DISP.blit(text, textRect)

	pygame.draw.rect(DISP, (10, 255, 10), (3*BLOCK_SIZE+1, 0, BLOCK_SIZE-2, BLOCK_SIZE-2))
	pygame.draw.rect(DISP, (255, 10, 10), (3*BLOCK_SIZE+1, 1*BLOCK_SIZE+1, BLOCK_SIZE-2, BLOCK_SIZE-2))
	pygame.draw.rect(DISP, (100, 100, 100), (1*BLOCK_SIZE+1, 1*BLOCK_SIZE+1, BLOCK_SIZE-2, BLOCK_SIZE-2))
			

while run: # Main world loop
	# pygame.time.delay(10)
	DISP.fill((200, 255, 255))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False;
		# if event.type == pygame.KEYDOWN:
		# 		if event.key == pygame.K_LEFT:
		# 			agnt.move(3)

		# 		if event.key == pygame.K_RIGHT:
		# 			agnt.move(1)

		# 		if event.key == pygame.K_UP:
		# 			agnt.move(0)

		# 		if event.key == pygame.K_DOWN:
		# 			agnt.move(2)

	agnt.move(agnt.get_move())

	draw_grid(agnt)
	draw_agent(agnt)
	pygame.display.update()


pygame.quit()
sys.exit()
