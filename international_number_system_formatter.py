

def take_input():
	num = input("Enter the number you want to convert : ")
	return num

def validate_input(num):
		try:
			int(num)
			return True
		except:
			return False
	
def special_case(num):
	if len(num) <=3:
		return num
	else:
		return 

	
														
def slicing(num):
						
		raw_num = num
		list_of_num= [ ]
		cursor=-3
		while  raw_num !="": 
			group = raw_num[cursor:]
			remaining = raw_num[:cursor]
	
			list_of_num.append(group)
			raw_num=remaining
		
		
		unformatted_num= list_of_num		

		return unformatted_num
		
def formatting_num(unformatted_list_of_num):
		rev_list = [ ]
		a = -1
		for i in range(len(unformatted_list_of_num)):
			element = unformatted_list_of_num[a]
			rev_list.append(element)
			a +=-1
		
		return rev_list	

def final_num(rev_list):
	international_formatted_number = "," .join(rev_list)
	return international_formatted_number
	
def print_number(international_formatted_number):
	print(f"{international_formatted_number}")

def taking_printing(num):
	unformatted_list_of_num=slicing(num)
	rev_list=formatting_num(unformatted_list_of_num)
	international_formatted_number =final_num(rev_list)
	print_number(international_formatted_number)
																	
num = take_input()
validation= validate_input(num)
if validation is True:
	result = special_case(num)
	if result == num:
		print(num)
	else:
		taking_printing(num)
else:
	print(f"You wrote ({num}) Write integers only! ")		


user_choice = input("Type 'go' to convert another number or 'exit' to quit:")

while user_choice.lower() =="go":
	num = take_input()
	validation= validate_input(num)
	if validation is True:
		result = special_case(num)
		if result == num:
			print(num)
		else:
			taking_printing(num)
	else:
		print(f"You wrote ({num}) Write integers only! ")	
	
	
	user_choice = input("Type 'go' to convert another number or 'exit' to quit:")

	