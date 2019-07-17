import random

class Agent:
	def __init__(self):
		self.x = 0
		self.y = 2

		self.alpha = 0.4;
		self.gamma = 0.99;

		self.WIDTH = 4
		self.HEIGHT = 3
		self.depth = 4

		self.q_vals = [];

		for i in range(self.WIDTH):
			addVal = []
			for j in range(self.HEIGHT):
				addVal += [[]]
				for k in range(self.depth):
					addVal[j] += [0]
			self.q_vals += [addVal];

		self.q_vals[3][0] = [1, 1, 1, 1]
		# self.q_vals[1][1] = ['x', 'x', 'x', 'x']
		self.q_vals[1][1] = [0, 0, 0, 0]
		self.q_vals[3][1] = [-1, -1, -1, -1]


	def get_move(self):
		return self.q_vals[self.x][self.y].index(max(self.q_vals[self.x][self.y]))


	def move(self, num_in): # up = 0; right = 1; down = 2; left = 3
		# Implementing random chance of left/right
		num = num_in
		rand = random.random()
		if(rand > 0.9):
			num += 1
		elif(rand > 0.8):
			num -= 1

		if num < 0:
			num = 3
		if num > 3:
			num = 0

		nx = self.x
		ny = self.y

		if num == 0:
			ny -= 1
		elif num == 1:
			nx += 1
		elif num == 2:
			ny += 1
		elif num == 3:
			nx -=1

		if self.bounce_back(self.x, self.y, nx, ny):
			self.update_q_vals(self.x, self.y, self.x, self.y, num_in)
		else:
			self.update_q_vals(self.x, self.y, nx, ny, num_in);
			self.x = nx
			self.y = ny

		if self.check_end():
			self.x = 0
			self.y = 2

	def check_end(self):
		if self.x == 3 and self.y == 0:
			return True
		elif self.x == 3 and self.y == 1:
			return True

	def get_reward(self, x, y): # helper function
		ret_val = -0.04
		return ret_val;

	def get_max_q(self, x, y): # Helper function
		ret_val = max(self.q_vals[x][y])
		return ret_val

	def bounce_back(self, cx, cy, nx, ny):
		if nx < 0 or ny < 0 or nx >= self.WIDTH or ny >= self.HEIGHT:
			return True
		elif nx == 1 and ny == 1:
			return True
		return False

	# Function for updating q-values based on current position, new position, and direction.
	def update_q_vals(self, cx, cy, nx, ny, direction): # current x, current y
												  # new x, new y, direction (0-3)
		if(nx == cx and cy == ny):
			self.q_vals[cx][cy][direction] = self.q_vals[cx][cy][direction] + self.alpha*(-0.04 - self.q_vals[cx][cy][direction])
			return
		else:
			self.q_vals[cx][cy][direction] = self.q_vals[cx][cy][direction] + self.alpha*(self.get_reward(nx, ny) + self.gamma*self.get_max_q(nx, ny) - self.q_vals[cx][cy][direction])
			return
