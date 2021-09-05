import random
import os

def chk_file(filename):
	if os.path.isfile(filename):
		print('file', filename, 'exists')	
		return True
	else:
		print('file product.csv not exists \n')	
		return False

def read_file(filename):
	chat_list = []
	with open(filename, 'r', encoding='UTF-8-sig') as f:
		for p in f:
			chat_list.append(p.strip())
	return chat_list 				

def convert(chat_list, name_a, name_b):
	new_chat_list = []
	#name = ''
	name = None
	for p in chat_list:
		if p == name_a:
			name = name_a
		elif p == name_b:
			name = name_b		
		else:
			new_chat_list.append(name + ':' + p)
	return new_chat_list


def write_file(filename, chat_list):			
	with open(filename, 'w', encoding='UTF-8-sig')	as f:
		for p in chat_list:
				f.write(p + '\n')


def main():
	if_file = chk_file('input.txt')
	if if_file:
		chat_list = read_file('input.txt')
		new_chat_list = convert(chat_list, 'Allen', 'Tom')
		print(new_chat_list)		
		write_file('output.txt', new_chat_list)
	

#refactor
main()	