import sys
raw_data_file = open("raw_data", "r")
clear_data_file = open("clear_data", "w")


'''
  num: store all number from a line of raw data
  pair: store number pair which sum is equal to stop_amount
  final: store clean data from pair (pick a valid pair of number from 'pair')
'''
num, pair, final = [], [], []

stop_amount = int(input("Please enter total amount of bike stop: "))

print(">>> Read raw data, and amount of bike stop is : %d"%(stop_amount))

while True:
  line = raw_data_file.readline()
  if line == "": break
  #print(line, end="")
  csv = line.split(",")

  '''
    Get time info from a line of raw data.
  '''
  for x in csv:
    if x.split("-")[0] == "2018":
      #print(x)
      time = x.split(".")[0]
  
  '''
    Try to get all number from a line of raw data.
    Because the order of raw data is wrong, we should clean it.
  '''
  for x in csv:
    try:
      num.append(int(x))  
    except ValueError:
      continue;

  '''
    Get a valid (occupied space, empty space) from all of lines of raw data
  '''
  found = 0
  for index in range(len(num)):
    for nex in range(index+1, len(num)):
      if(num[index]+num[nex] == stop_amount):
        #pair.append((num[index], num[nex]))
        final.append(time+","+str(num[index])+","+str(num[nex])+"\n")
        found = 1
        break
    if found == 1:
      break

  num = []
  #pair = []

raw_data_file.close()

'''
  Sort all of clean data based on time
'''
sorted_data = sorted(final, key=lambda x: x.split(",")[0])

clear_data_file.write(sorted_data[0])

'''
  Get a correct order of  (occupied space, empty space) from all of lines of sorted data
'''
for i in range(1, len(sorted_data)):
  left = int(sorted_data[i].split(",")[1])
  right = int(sorted_data[i].split(",")[2].split("\n")[0])
  try:
    up = int(sorted_data[i-1].split(",")[1])
  except IndexError:
    print(sorted_data[i-1])
    sys.exit(0)

  if abs(left-up) <= abs(right-up):
    clear_data_file.write(sorted_data[i])
  else:
    ne = sorted_data[i].split(",")[0] + "," + str(right) + "," + str(left) + "\n"
    clear_data_file.write(ne)
    sorted_data[i] = ne
  
clear_data_file.close()

print(">>> Create clear data file success!")
print(">>> Now please execute 'probability.py'")