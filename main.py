items = [-2, 0, -10, -1]
for item in items:  # loop to find the first positive number
  if item > 0:
    break # exit the loop if a positive number is found
  else: 
    # else is executed if the loop has not been interrupted with break (if there is no positive number)
    item = None

print(item)



"""
Strings with the # symbol do not need to be processed
"""
lines_of_code = [
  '# In God we trust',
  'echo 123',
  'cd foo',
  '# end']
for line in lines_of_code:
  if line[:1] == '#':
    continue  # if # is found, go to the next iteration

  print(line)



tries = 3
while tries:
  print('>>> ', end='') # there will be no jump to another line
  command = input()
  if not command:
    continue
  if command in ('echo', 'cd', 'help'):
    break
  print('Unknown command!')
  tries -= 1
else:
  print('Too many bad tries!')
  command = None