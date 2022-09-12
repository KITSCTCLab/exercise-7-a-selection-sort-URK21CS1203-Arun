from typing import List

def selectionSort(array, size) -> List[int]:
  # Write your code here
  for i in range(len(data)):
    min = i
    for j in range(i+1,len(data)):
      if data[i]<data[j]:
        data[i],data[j] = data[j],data[i]
        
        
# Do not change the following code
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(selectionSort(data, len(data)))
