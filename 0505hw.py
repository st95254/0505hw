class Scoreinfo:
	def __init__(self, m ,e):
		self.math = m
		self.english = e

	def bigger(self):
			if self.math > self.english:
				print('數學比較高分')
			elif self.math < self.english:
				print('英文比較高分')
			else:
				print('兩個分數一樣')

	def add(self):
		print('總分為:%d' %(self.math + self.english))

	def present(self):
		print(self.math, self.english)
score = Scoreinfo(70,95)
score.bigger()
score.add()
score.present()