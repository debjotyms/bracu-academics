def is_five(n):
    if n == 1:
        return True
    if n % 5 == 0:
        return is_five(n/5)
    return False

def iterate_array(arr, i, sum):
    if i < len(arr):
        if (arr[i]>=5 and is_five(arr[i]) or arr[i]==1):
            sum+=arr[i]
        iterate_array(arr, i+1,sum)
        if(i==len(arr)-1):
            print(sum)
    
arr = [625, 15,25,225,1,0,125]
iterate_array(arr, 0, 0)