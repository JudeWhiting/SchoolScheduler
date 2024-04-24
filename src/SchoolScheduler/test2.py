import random
import math

def objective_function(x):
    # Define your objective function here
    return x ** 2  # Example: minimizing x^2

def simulated_annealing(initial_solution, initial_temperature, cooling_rate, num_iterations):
    current_solution = initial_solution
    best_solution = initial_solution

    current_temperature = initial_temperature

    for i in range(num_iterations):
        # Generate a new candidate solution
        new_solution = current_solution + random.uniform(-1, 1)

        # Calculate the change in objective function value
        delta = objective_function(new_solution) - objective_function(current_solution)

        # If the new solution is better, accept it
        if delta < 0:
            current_solution = new_solution
            best_solution = new_solution
        else:
            # If the new solution is worse, accept it with a certain probability
            if random.random() < math.exp(-delta / current_temperature):
                current_solution = new_solution

        # Update the temperature
        current_temperature *= cooling_rate

    return best_solution

# Example usage
initial_solution = 10
initial_temperature = 1000
cooling_rate = 0.95
num_iterations = 1000

best_solution = simulated_annealing(initial_solution, initial_temperature, cooling_rate, num_iterations)
print("Best solution found:", best_solution)
print("Objective function value:", objective_function(best_solution))
