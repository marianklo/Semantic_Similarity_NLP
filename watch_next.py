# Let us build a system that will tell you what to watch next based on the word
# vector similarity of the description of movies.

# Create a file called watch_next.py.
# Read in the movies.txt file. Each separate line is a description of a different movie.
# The task is to create a function to return which movies a user would watch
# next if they have watched Planet Hulk with the description “Will he save
# their world or destroy it? When the Hulk becomes too dangerous for the
# Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
# planet where the Hulk can live in peace. Unfortunately, Hulk lands on the
# planet Sakaar where he is sold into slavery and trained as a gladiator.”

# The function should take in the description as a parameter and return the title of the most similar movie.


import spacy
import numpy as np

# Create a function.
def get_next_movie(description):

# Load the model language.
    nlp = spacy.load("en_core_web_md")
# Read the file
    with open("movies.txt", "r") as file:
        movies = file.readlines()
# Create a empty list to store the similarity score.
    similarity_score = []
# Calculate similarity between the descriptio and each movie.
    for movie in movies:
        movie1 = nlp(description)
        movie2 = nlp(movie)
        similarity = movie1.similarity(movie2)
    # Ensures that each similarity score is added to the "similarity_scores" list
        similarity_score.append(similarity)
# Get index for most similar movie.
    most_similar_index = np.argmax(similarity_score)
# Get the title of the most similar movie
    most_similar_movie = movies[most_similar_index]

    return most_similar_movie.strip()

# Add the description of the movie watched. 
description = """Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth,
the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace.
Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."""

# Use the fuction and print the results.
next_movie = get_next_movie(description)
print("Next movie to watch:", next_movie)