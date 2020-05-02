import os
files = os.listdir('fixtures')

for file in files:
	print(file)
	os.system("python manage.py loaddata fixtures/%s" % file)


