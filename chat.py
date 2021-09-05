import random
import os

def chk_file(filename):
	if os.path.isfile(filename):
		print('file', filename, 'exists')	
		return True
	else:
		print('file product.csv not exists \n')	
		return False

def read_file_chat_2_people(filename, name_a, name_b):
	chat_list = []
	chat_list_conversation = []	
	with open(filename, 'r', encoding='UTF-8-sig') as f:
		cnt = 0
		for p in f:
			if name_a in p:
				if cnt != 0:
					chat_list.append(cnt)	
					cnt = 0
				chat_list.append(p.strip())
			elif name_b in p:
				if cnt != 0:
					chat_list.append(cnt)	
					cnt = 0
				chat_list.append(p.strip())
			else:
				chat_list_conversation.append(p.strip())
				cnt += 1
		chat_list.append(cnt)
	return chat_list, chat_list_conversation 				


def write_file(filename, chat_list, chat_list_conversation):			
	with open(filename, 'w', encoding='UTF-8-sig')	as f:
		name = ''
		cnt = 0
		for p in chat_list:
			if isinstance(p, int):
				for i in range(p):
					f.write(name + ':' + chat_list_conversation[cnt] + '\n')
					cnt += 1
			else:
				name = p;

def main():
	if_file = chk_file('input.txt')
	if if_file:
		chat_list, chat_list_conversation = read_file_chat_2_people('input.txt', 'Allen', 'Tom')
		print(chat_list)
		print(chat_list_conversation)		
		write_file('output.txt', chat_list, chat_list_conversation)
	

#refactor
main()	