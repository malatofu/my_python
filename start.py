import getpass
import time
from sys import exit
import os
from random import randint

def user_loading_window():
	while 1:
		username=str(input('please input you name:'))
		password=str(getpass.getpass('you password:'))
		if username=='root' and password=='root':
			print('welcome back:',username)
			time.sleep(1)
			os.system('clear')
			input()
			break		
		else:
			print('no user please sign up')

def row_dice(num):
	while num==1:
		dice=randint(1,6)
		input('press space to start')
		print('',dice)
		play_num=str(input('play again,y/n'))
		if play_num=='y':
			os.system('clear')
		else:
			break
	while num==2:
		dice_1=randint(1,6)
		dice_2=randint(1,6)
		input('1P-time')
		print('1P:',dice_1)
		input('2P-time')
		print('2P:',dice_2)
		if dice_1>dice_2:
			print('Player1 win')
		elif dice_1<dice_2:
			print('Player2 win')
		else:	
			print('peace')
		play_num=str(input('play again,y/n'))
		if play_num=='y':
			os.system('clear')
		else:
			break
def game_choose():
	while 1:
		print('1.row dice')
		print('2.more games coming soon...')
		print('3.quit')
		choose=str(input())
		if choose=='1':
			os.system('clear')
			while 1:
				dice_num=str(input('1.1P	2.2P'))
				if dice_num=='1':
					row_dice(1)
				elif dice_num=='2':
					row_dice(2)
				else:
					print('????')
		elif choose=='3':
			exit()

while 1:
	user_loading_window()
	game_choose()
