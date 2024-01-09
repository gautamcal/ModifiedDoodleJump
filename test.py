import unittest
import math
class DoodleJump:
	def __init__(self):
		self.player_x = 80
		self.player_y = 90 
		self.platform_x = 100
		self.platform_y = 110

	def collision(self): 
		#for i in range(self.num_platforms): [needed to be removed for test to work]
			distance = math.sqrt((math.pow(self.player_x - self.platform_x, 2) + math.pow(self.player_y - self.platform_y, 2)))
			if distance < 90: 
				return True
			else:
				return False # indented, unlike original code, to make up for removing the for loop

class Testcollision(unittest.TestCase):

	def test_collision1(self):
		result = DoodleJump().collision()
		self.assertTrue(result)
	
	def test_collision2(self):
		value = DoodleJump()
		value.player_x = 11
		value.player_y = 28
		value.platform_x = 20
		value.platform_y = 27
		result = value.collision()
		self.assertTrue(result)
	

if __name__ == '__main__':
	unittest.main()
