def rangeSum(minimum,maximum,divisor):
    sum=0
    for number in range(minimum,maximum):
        if number%divisor==0:
            sum+=number
    return sum
print(rangeSum(3,16,3))