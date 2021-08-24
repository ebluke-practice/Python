while True:
	line = input('> ')
	if "deez" in line:
		print('deez nuts')
	
	if line[0] == '#':
		continue
	if line == 'done':
		break
print('Done')
