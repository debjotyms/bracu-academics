# You must run this cell to install dependency
import fhm_unittest as unittest

# Complete the functions defined in this cell

# Test 01: Shift Left k cell
def shift_left(source, k):
  # TO DO
  # Hint, You can write a function for left shift once and then use it
  for i in range(len(source)-k):
    source[i]=source[i+k]
    source[i+k]=0
  return source


# Test 02: Rotate Left k cell
def rotate_left(source, k):
  # TO DO
  # Hint, You can write a function for left rotate once and then use it
  for i in range(len(source)-k):
    temp=source[i]
    source[i]=source[i+k]
    source[i+k]=temp
  return source


# Test 03: Shift Right k cell
def shift_right(source, k):
  # TO DO
  # Hint, You can write a function for right shift once and then use it
  for i in range(len(source)-1,k-1,-1):
    source[i]=source[i-k]
    source[i-k]=0
  return source



# Test 04: Rotate Right k cell
def rotate_right(source, k):
  # TO DO
  # Hint, You can write a function for right rotate once and then use it
  for i in range(len(source)-1,k-1,-1):
    temp=source[i]
    source[i]=source[i-k]
    source[i-k]=temp
  return source



# Test 05: Remove an element from an array
def remove(source, idx):
  # TO DO
  if idx not in range(len(source)):
    print("Index not valid")
  else:
    for i in range(idx,len(source)-1):
      source[i]=source[i+1]
      source[i+1]=0
  return source



# Test 06: Remove all occurrences of a particular element from an array
def remove_all(source, element):
  # TO DO
  for i in range(len(source)):
    if source[i]==element:
      source[i]=0
  for i in range(len(source)-1):
    for j in range(len(source)-1):
      if source[j]==0:
        source[j]=source[j+1]
        source[j+1]=0
  return source



# Test 07: Splitting an Array
def split_array(a):
  # TO DO
  sum=0
  sum2=a[0]
  for i in range(len(a)):
    sum+=a[i]
  sum=sum-sum2
  for i in range(1,len(a)):
    if(sum==sum2):
      return True
    sum2+=a[i]
    sum-=a[i]
  return False


# Test 08: Max Bunch Count
def max_bunch(a):
  # TO DO
  ans=1
  for i in range(len(a)-1):
    c=1
    for j in range(i+1,len(a)):
      if a[i]!=a[j]:
        break
      c+=1
      if(c > ans):
        ans=c
  return ans


# This cell is the driver code
# Run this cell after completion of above function.
# You will see the status Accepted after completion if your code is correct.
# If your function is wrong you will see wrong[correction percentage]
# This is call unit testing if you are wondering the checking approach
# No need to write or change any code here

print("///  Test 01: Shift Left k cell  ///")
source = [10,20,30,40,50,60]
returned_value = shift_left(source, 3) # This should return [40, 50, 60, 0, 0, 0]
unittest.output_test(returned_value, [40, 50, 60, 0, 0, 0])


print("///  Test 02: Rotate Left k cell  ///")
source = [10,20,30,40,50,60]
returned_value = rotate_left(source, 3) # This should return [40, 50, 60, 10, 20, 30]
unittest.output_test(returned_value, [40, 50, 60, 10, 20, 30])


print("///  Test 03: Shift Right k cell  ///")
source = [10,20,30,40,50,60]
returned_value = shift_right(source, 3) # This should return [0, 0, 0, 10, 20, 30]
unittest.output_test(returned_value, [0, 0, 0, 10, 20, 30])


print("///  Test 04: Rotate Right k cell  ///")
source = [10,20,30,40,50,60]
returned_value = rotate_right(source, 3) # This should return [40, 50, 60, 10, 20, 30]
unittest.output_test(returned_value, [40, 50, 60, 10, 20, 30])


print("///  Test 05: Remove an element from an array  ///")
source = [10,20,30,40,50,0,0]
returned_value = remove(source, 2) # This should return [10, 20, 40, 50, 0, 0, 0]
unittest.output_test(returned_value, [10, 20, 40, 50, 0, 0, 0])


print("///  Test 06: Remove all occurrences of a particular element from an array  ///")
source = [10,2,30,2,50,2,2,0,0]
returned_value = remove_all(source, 2) # This should return [10, 30, 50, 0, 0, 0, 0, 0, 0]
unittest.output_test(returned_value, [10, 30, 50, 0, 0, 0, 0, 0, 0])


print("///  Test 07: Splitting an Array  ///")
test_1 = [1, 1, 1, 2, 1] # Here splitting is possible as summation of [1, 1, 1] = summation of [2,1]
returned_value = split_array(test_1) # This should return True
test_2 = [2, 1, 1, 2, 1] # Here splitting is not possible
returned_value = split_array(test_2) # This should return False
test_3 = [10, 3, 1, 2, 10] # Here splitting is possible as summation of [10, 3] = summation of [1,2,10]
returned_value = split_array(test_3) # This should return True
unittest.output_test(split_array(test_1), True)
unittest.output_test(split_array(test_2), False)
unittest.output_test(split_array(test_3), True)


print("///  Test 08: Max Bunch Count  ///")
returned_value = max_bunch([1, 2, 2, 3, 4, 4, 4]) # This should return 3
unittest.output_test(returned_value, 3)
returned_value = max_bunch([1, 1, 2, 2, 1, 1, 1, 1]) # This should return 4
unittest.output_test(returned_value, 4)