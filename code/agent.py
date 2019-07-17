class Agent:
	def __init__(self):
		self.x = 0
		self.y = 0

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
		self.q_vals[1][1] = ['x', 'x', 'x', 'x']
		self.q_vals[3][1] = [-1, -1, -1, -1]




	def move(self, num): # up = 0; right = 1; down = 2; left = 3
		if num == 0:
			self.y -= 1
		elif num == 1:
			self.x += 1
		elif num == 2:
			self.y += 1
		elif num == 3:
			self.x -= 1

