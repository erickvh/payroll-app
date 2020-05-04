import os
files = os.listdir('fixtures')

files.sort()
for file in files:
	print(file)
	os.system("python manage.py loaddata fixtures/%s" % file)


