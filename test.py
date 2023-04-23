import numpy as np

# Generate random example word embeddings
def generate_random_embedding(dim):
    return np.random.rand(dim)

embedding_dim = 3
animal_embedding = generate_random_embedding(embedding_dim)
food_embedding = generate_random_embedding(embedding_dim)

# Define a non-commutative product operation
def non_comm_product(embedding_a, embedding_b):
    return np.outer(embedding_a, embedding_b)

# Non-commutative relationship between animal and food
animal_food_algebra = non_comm_product(animal_embedding, food_embedding)

# Non-commutative relationship between food and animal
food_animal_algebra = non_comm_product(food_embedding, animal_embedding)

# Cosine similarity
def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

# Calculate cosine similarity between animal and food embeddings
cosine_sim = cosine_similarity(animal_embedding, food_embedding)

print("Cosine Similarity:", cosine_sim)

# Calculate the simplified Connes' metric distance
dirac_animal = np.linalg.norm(animal_embedding)
dirac_food = np.linalg.norm(food_embedding)
connes_metric = abs(dirac_animal - dirac_food)

print("Connes' Metric Distance:", connes_metric)

print("Non-commutative relationship (Animal->Food):")
print(animal_food_algebra)
print("Non-commutative relationship (Food->Animal):")
print(food_animal_algebra)
print("Is non-commutative?", not np.array_equal(animal_food_algebra, food_animal_algebra))
