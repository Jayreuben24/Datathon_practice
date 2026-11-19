## inputs number of voltages (n) and voltages
## input validations

while True: ## input validation for the number of voltages
    try: 
        n = int(input("Please input the number of voltages:"))
    except ValueError:
        print("Please input valid number.")
        continue
    if n <= 0:
        print("Please input value greater than zero.")
    break

def get_values(text):## input validation for the voltage values
    while True:
        try:
            value = float(input(text))
        except ValueError:
            print("Please input valid voltage values.")
            continue
        return value 
 
samples = []
for i in range(n):
    value = get_values(f'Please input the value for voltage {i+1}:')
    samples.append(value)
    
print(samples)

voltages = {f"V{i+1}": value for i, value in enumerate(samples)}
print(voltages)
# {'V1': 4.8, 'V2': 12.1, 'V3': 3.3}
print(voltages["V2"])  # 12.1

def classify(v):
    if v < 11.5:        # example thresholds, change to yours
        return "Critical"
    elif v <= 12.20 and v >=11.50:
        return "Low"
    elif v <= 13.80 and v >=12.20:
        return "Normal"
    elif v > 13.80:
        return "Overvoltage"

classified = {}
for i, value in enumerate(samples, start=1):
    classified[f"V{i}"] = classify(value)
    print(f"Voltage {i}: {value:.2f} V -> {classified[f'V{i}']}")



    
        
    