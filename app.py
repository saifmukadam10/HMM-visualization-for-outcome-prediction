import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("Libraries imported successfully.")

# Load CSV file
data = pd.read_csv("weather.csv")

print("Dataset Loaded Successfully")
print(data.head())

# -------------------------------
# Create Temperature State
# -------------------------------
# Adjust column name depending on dataset
# Usually Temp_C or Temperature

if 'Temp_C' in data.columns:
    temperature = data['Temp_C']
elif 'Temperature' in data.columns:
    temperature = data['Temperature']
else:
    raise Exception("Temperature column not found")

# Convert temperature to states
# 0 = Cold, 1 = Mild, 2 = Hot

temp_states = []

for temp in temperature:
    if temp < 15:
        temp_states.append(0)   # Cold
    elif temp < 30:
        temp_states.append(1)   # Mild
    else:
        temp_states.append(2)   # Hot

data['Temp State'] = temp_states

print("Temperature states created.")

# -------------------------------
# Predicted states (Example Model)
# -------------------------------
# Replace this later with HMM output
np.random.seed(42)
hidden_states = np.random.randint(0, 3, len(data))

# -------------------------------
# Mapping
# -------------------------------
temp_state_map = {0: 'Cold', 1: 'Mild', 2: 'Hot'}

hidden_states_actual = data['Temp State'].values

y_tick_labels = [temp_state_map[i] for i in sorted(temp_state_map.keys())]

# -------------------------------
# Plot
# -------------------------------
plt.figure(figsize=(12,6))

plt.plot(hidden_states_actual[:200],
         label='Actual Temperature State',
         marker='o')

plt.plot(hidden_states[:200],
         label='Predicted Temperature State',
         marker='x',
         linestyle='--')

plt.title('Comparison of Actual vs Predicted Temperature States')
plt.xlabel('Time')
plt.ylabel('Temperature State')

plt.yticks(sorted(temp_state_map.keys()), y_tick_labels)

plt.legend()
plt.grid(True)

plt.show()

print("Plot generated successfully.")