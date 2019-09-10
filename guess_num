import random
import os
import time
import sys

cout=1
print('This game need you to guess a number in range 1-500')
while True:
	num=random.randint(1,500)
	for cout in range(1,8):
		user=int(input('input num:'))
		cout+=1
		if user<num:
			print('num too small')
		elif user>num:
			print('num too big')
		else:
			print('ohhhhhhhhhhhhh!!!you win')
	os.system('clear')
	if cout<3:
		print('You are genius')
	elif cout>2 and cout <8:
		print('You are normal')
	else:
		i=1
		bad_word='Idiot,you must thinking what just happend,how can you guess a num used over 8 times,what a fool little puppy!'
		max_i=len(bad_word)
		for i in range(1,max_i):
		#	print(bad_word[i],end='!')
			sys.stdout.write(bad_word[i])
			sys.stdout.flush()
			time.sleep(0.1)
			i+=1
	print('bye')
