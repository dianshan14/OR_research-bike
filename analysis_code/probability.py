import sys
import numpy as np

stop_amount = int(input("Please enter total amount of bike stop: "))
print(">>> Read clear data, and amount of bike stop is : %d"%(stop_amount))

clear_data_file = open("clear_data", "r")

prob = {}
count = 0
data = []

'''
  data: store clear data
  count: amount of data
'''
while True:
  i = clear_data_file.readline()
  if i=="": break
  count = count + 1
  data.append(i)

clear_data_file.close()
#print(count)

#print(len(data))

'''
  Count variation of current time and previous time
'''
for x in range(1, len(data)):
  first = int(data[x-1].split(",")[1])
  second = int(data[x].split(",")[1])

  if str(second-first) in prob:
    prob[str(second-first)] = prob[str(second-first)] + 1
  else:
    prob[str(second-first)] = 1 

#print(prob)


'''
  Doing statistics according to the above data of variation
'''
dire = {"-5":0, "-4":0, "-3":0, "-2":0, "-1":0, "0":0, "1":0, "2":0, "3":0, "4":0, "5":0}

for key, value in prob.items():
  if 5 >= int(key) >= -5:
    dire[key] = dire[key] + int(value)
  elif int(key) > 5:
    dire["5"] = dire["5"] + int(value)
    #print("5", value)
  elif int(key) < -5:
    dire["-5"] = dire["-5"] + int(value)
    #print("-5", value)

#print("")
#print(dire)

'''
  Count probability of variation 
'''
bi = []
for key, value in dire.items():
  dire[key] = dire[key]/count
  bi.append(dire[key])

'''
  Create transition matrix
'''
prob = bi
array = [[0 for x in range(stop_amount+1)]for y in range(stop_amount+1)]

matrix_file = open("./matrix.csv", "w")

for j in range(stop_amount+1):
  for k in range(-5, 6, 1):
    try:
      if j+k < 0:
        array[j][0] = array[j][0] + prob[k+5]
      elif j+k > 40:
        array[j][40] = array[j][40] + prob[k+5]
      else:
        array[j][j+k] = array[j][j+k] + prob[k+5]
    except IndexError:
      #print(j,k+5)
      continue
  for x in array[j]:
    matrix_file.write(str(round(x,5)) + ",")
  matrix_file.write("\n")

matrix_file.close()
print(">>> Create transition matrix file success! (matrix.csv)")
#print(sum(prob))

'''
  Solve the simultaneous equations.
'''
constant = [-1 for i in range(stop_amount)]

s, ts = "", ""
for i in range(1, stop_amount+1):
  for j in range(1, stop_amount+1):
    if i==j:
      s = s + str(round(array[i][j]-1,4)) + ","
    else:
      s = s + str(round(array[i][j],4)) + ","
  #print(s)
  ts = ts + s[0:-1] + ";"
  #print(s)
  s = ""

ts = ts[0:-2]

A = np.mat(ts)    
b = np.mat(constant).T       
r = np.linalg.solve(A,b)  
#print(r)

new_str = str(r)
new_list = new_str.split("[")[2:]

tt = open("to_zero.csv", "w")
for x in new_list:
  a = x.split("]")[0]
  tt.write(str(float(a)) + "\n")

tt.close()
print(">>> Create 'all state to zero' file success! (to_zero.csv)")

#print("-"*100)

#print("full")
constant = [-1 for i in range(stop_amount)]

s, ts = "", ""
for i in range(0, stop_amount):
  for j in range(0, stop_amount):
    if i==j:
      s = s + str(round(array[i][j]-1,4)) + ","
    else:
      s = s + str(round(array[i][j],4)) + ","
  #print(s)
  ts = ts + s[0:-1] + ";"
  #print(s)
  s = ""

ts = ts[0:-2]

A = np.mat(ts)    
b = np.mat(constant).T       
r = np.linalg.solve(A,b)  
#print(r)

new_str = str(r)
new_list = new_str.split("[")[2:]
#print(new_list)

tt = open("to_full.csv", "w")
for x in new_list:
  a = x.split("]")[0]
  tt.write(str(float(a)) + "\n")

tt.close()
print(">>> Create 'all state to full' file success! (to_full.csv)")