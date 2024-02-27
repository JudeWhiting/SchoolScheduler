import numpy as np
import tensorflow as tf

# Define parameters
POPULATION_SIZE = 100
TARGET_STRING = "Hello, World!"
MUTATION_RATE = 0.01
NUM_GENERATIONS = 1000

# Convert target string to binary representation
TARGET_BINARY = ''.join(format(ord(c), '08b') for c in TARGET_STRING)

# Create initial population randomly
population = np.random.choice([0, 1], size=(POPULATION_SIZE, len(TARGET_BINARY)))

# Convert population to TensorFlow tensor
population_tf = tf.constant(population, dtype=tf.float32)

# Convert target binary to TensorFlow tensor
target_tf = tf.constant(np.array(list(map(int, TARGET_BINARY))), dtype=tf.float32)

# Define the genetic algorithm operations
def fitness(population):
    # Calculate fitness as the number of matching bits with the target
    return -tf.reduce_sum(tf.abs(population - target_tf), axis=1)

def select_parents(population, num_parents):
    # Select parents based on their fitness
    return tf.gather(population, tf.nn.top_k(fitness(population), num_parents).indices)

def crossover(parents, num_offsprings):
    offsprings = []
    for _ in range(num_offsprings):
        parent1_index = np.random.randint(0, parents.shape[0])
        parent2_index = np.random.randint(0, parents.shape[0])
        crossover_point = np.random.randint(1, parents.shape[1])
        offspring = np.concatenate([parents[parent1_index, :crossover_point],
                                    parents[parent2_index, crossover_point:]])
        offsprings.append(offspring)
    return np.array(offsprings)

def mutate(offsprings):
    # Apply mutation to the offsprings
    for offspring in offsprings:
        for idx in range(len(offspring)):
            if np.random.uniform(0, 1) < MUTATION_RATE:
                offspring[idx] = 1 - offspring[idx]
    return offsprings

# Main genetic algorithm loop
for generation in range(NUM_GENERATIONS):
    # Select parents
    parents = select_parents(population_tf, 2)

    # Perform crossover to produce offsprings
    offsprings = crossover(parents, POPULATION_SIZE - 2)

    # Mutate the offsprings
    mutated_offsprings = mutate(offsprings)

    # Create new population with parents and mutated offsprings
    population = np.concatenate((parents.numpy(), mutated_offsprings), axis=0)

    # Print best individual and its fitness
    best_individual_index = tf.argmax(fitness(population))
    best_individual = population[best_individual_index]
    best_fitness = fitness(tf.expand_dims(best_individual, axis=0)).numpy()[0]

    # Convert binary to string
    best_individual_string = ''.join(map(str, best_individual.astype(int)))
    decoded_string = ''.join(chr(int(best_individual_string[i:i+8], 2)) for i in range(0, len(best_individual_string), 8))

    print(f"Generation {generation+1}: Best Fitness: {best_fitness}, Best Individual: {decoded_string}")

    # Check for convergence
    if best_fitness == len(TARGET_STRING) * 8:
        print("Target reached!")
        break
