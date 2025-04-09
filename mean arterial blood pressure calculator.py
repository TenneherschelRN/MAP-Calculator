print("Hello World!")
print("I'm Pearl and i am learning how to code")

# Demo pulse pressure calculator

num1 = float(input("Enter the Systolic Blood Pressure: "))
num2 = float(input("Enter the Diastolic Blood Pressure: "))

pulse_pressure = num1 - num2
mean_arterial_blood_pressure = 1/3 * (num1) + 2/3 * (pulse_pressure)


print(f"Results of your 2 numbers: ")
print(f"pulse_pressure: {pulse_pressure}")
print(f"mean_arterial_blood_pressure: {mean_arterial_blood_pressure}")

