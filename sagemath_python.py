# Import matplotlib for plotting
import matplotlib.pyplot as plt
import math

# Set up the number of years
years = 50
final_values = []  # Store the final value of money for each precision level
precisions = list(range(1, 105, 1))  # Precision levels (from 50 to 104 digits in steps of 1)

# Loop through different precision levels for e
for digits in precisions:
    e_value = e.n(digits=digits)  # Calculate 'e' with 'digits' number of precision
    money = e_value
    for i in range(1, years):
        money = (money - 1) * i  # Simulate the money evolution over 50 years
    final_values.append(money)

# Prepare the plot
plt.figure(figsize=(10, 6))

# Plotting with conditional log scale
for i in range(len(precisions)):
    if final_values[i] > 0:
        plt.scatter(precisions[i], math.log(final_values[i]), color='b')  # Plot positive values
    else:
        plt.scatter(precisions[i], -math.log(-final_values[i]), color='r')  # Plot negative values

# Set y-axis to log scale for positive values only
plt.yscale("linear")  # Start with linear scale

# Draw the plot
plt.title('Final Money Value After 50 Years vs Precision of e')
plt.xlabel('Number of Digits of Precision for e')
plt.ylabel('Final log of Money Value After 50 Years')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')  # Add a horizontal line at y=0 for reference
plt.grid(True)

# Show the plot
plt.show()
