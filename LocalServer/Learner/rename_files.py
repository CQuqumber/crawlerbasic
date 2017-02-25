import os

def rename_files():
	file_list = os.listdir(r"/Users/Joel/Documents/LocalServer/G'Day")
	#print(file_list)
	saved_path = os.getcwd()
	print("Current Working Directory is" + saved_path)
	os.chdir(r"/Users/Joel/Documents/LocalServer/G'day")

	for file_name in file_list:
		print("Old Name - " + file_name)
		print("New Name - " + file_name.translate(None,"0987654321"))
		os.rename(file_name, file_name.translate(None,"1234567890"))
	os.chdir(saved_path)

rename_files()