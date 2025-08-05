def calculate_bmi(weight,height):
    height = height / 100                 # cm 
    bmi = weight / (height ** 2)
    return bmi

try:
    weight = float(input("Enter yout weight in kilograms :"))
    height = float(input("Enter yout height in centimeters :"))
    
    bmi = calculate_bmi(weight, height)
    print(f"Your BMI is: {bmi:.2f}")
    
    if bmi < 18.5:
        print("you are under weight")
    elif 18.5 <= bmi < 24.9:
        print("you are normal weight")
    elif 25 <= bmi < 30:
        print("you are overweight")
    else:
        print("you have more fat than overweight")
        
except ValueError:
    print("please enter the correct value ")                    