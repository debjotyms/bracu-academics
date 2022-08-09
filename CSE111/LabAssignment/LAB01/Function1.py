def BMI(height,weight):
    BMI = weight/(height**2)
    if BMI<18.5:
        print('Score is {:.1f}. Your are Underweight'.format(BMI))
    elif 18.5<=BMI<=24.9:
        print('Score is {:.1f}. You are Normal'.format(BMI))
    elif 25<=BMI<=30:
        print('Score is {:.1f}. You are Overweight'.format(BMI))
    else:
        print('Score is {:.1f}. You are Obese'.format(BMI))
height = float(input())*0.01
weight = float(input())
BMI(height,weight)