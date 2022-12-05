# Гачи Version 3 
 
from datetime import datetime 
 
name = input("\nEnter name \n\n>>> ") 
password = input("\nEnter password \n\n>>> ") 
worldcs = input("\nWcs ? \n\n>>> ") 
 
def gachi(): 
	if password == "world cum shot": 
		if worldcs == "YES" or worldcs == "Yes" or worldcs == "yes": 
			time = datetime.now().hour 
			if 7 <= time <= 23: 
				print(f"\nNow {time} hours, mef day") 
				return "\n♂️ Thanks for using, " + name + " ♂️" 
			else: 
				print(f"\nNow {time} hours, wesleep ZzZz...") 
				return "\n♂️ Thanks for using, " + name + " ♂️"  
		elif worldcs != "YES" or worldcs != "Yes" or worldcs != "yes":
			print("\nFUCK YOU LEATHER MAN!!!") 
			exit()	 
	elif password != "world cum shot":
		print(password + " - Not a valid password") 
		exit() 
	return "\n♂️ Thanks for using, " + name + " ♂️" 
 
result = gachi() 
print(result) 