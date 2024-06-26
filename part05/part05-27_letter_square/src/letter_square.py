# Write your solution here
alphabet=" ABCDEFGHIJKLMNOPQRSTUVWXYZ"
layers = int(input("Layers: "))
multiplier=2*layers-1
square_matrix=[]
first_row = alphabet[layers]*multiplier
square_matrix.append(first_row)
for i in range (layers-1):
    first = square_matrix[i][0:i+1]
    
    last = square_matrix[i][len(first_row)-i-1:len(first_row)]
    next_row= f'{first}{alphabet[layers-(i+1)]*(multiplier-((i+1)*2))}{last}'
    square_matrix.append(next_row)


for i in range (layers-2, -1, -1):
    square_matrix.append(square_matrix[i])

for i in square_matrix:
    print (i)
#for i in range (multiplier, 0, -1):
 #   file_maker=[]
  #  for j in range (multiplier):
   #     if i == multiplier or i == 1:
    #        file_maker.append(alphabet[layers])
     #   else:
      #      if multiplier-i-1 <= j:
       #         file_maker.append(alphabet[layers-(multiplier-i)])
        #        minus = i
         #   else:
          #      file_maker.append(alphabet[layers-minus])
        #if i != 1 and i != multiplier and j != 0 and j != multiplier-1:
         #   file_maker.append(alphabet[layers-1])
        #else:
         #   file_maker.append(alphabet[layers])

    #square_matrix.append(file_maker)
#print(square_matrix)


#for i in (square_matrix):
 #   row=""
  #  for j in i:
   #     row += j
    #print (row)
