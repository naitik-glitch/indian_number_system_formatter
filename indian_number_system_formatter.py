

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

def part_1(num):
	last_part = (num[-3:])
	return last_part
	
														
def part_2(num):
		starting_part = (num[:-3])
				
		raw_num = starting_part
		list_of_num= [ ]
		cursor=-2
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
		#print(f"{rev_list},{last_part}")
		return rev_list	

def final_num(rev_list):
	indian_formatted_number = "," .join(rev_list)
	return indian_formatted_number
	
def print_number(indian_formatted_number,last_part):
								print(f"{indian_formatted_number},{last_part}")

def taking_printing(num):
	last_part = part_1(num)
	unformatted_list_of_num=part_2(num)
	rev_list =formatting_num(unformatted_list_of_num)
	indian_formatted_number =final_num(rev_list)
	print_number(indian_formatted_number,last_part)																
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

	