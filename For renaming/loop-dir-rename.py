import os 


# print(os.getcwd())
# print(os.listdir('.'))
# print(os.rename("New Text Document.txt", "the New Text Document.txt"))
extension = '.' + 'py' # input('whats the extension?')



for file in os.listdir():
	f_name, f_ext = os.path.splitext(file)
	if f_ext == extension:
		print(f_ext, f_name)
		name = ' '.join([ x for x in f_name.split(' ') if x != 'def'])
		new_name = f'{name}{f_ext}'
		os.rename(file, new_name)
		

