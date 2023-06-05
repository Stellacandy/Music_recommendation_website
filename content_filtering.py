from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Define and initialize the preprocessed_data variable
preprocessed_data = [
    ("Rihanna", "Love on the Brain", "Pop"),
    ("Chris Brown", "Influential", "Pop"),
    ("Shakira", "Waka Waka", "Reggae"),
    ("Adele", "Hello", "Pop Soul"),
    ("Snoop Dogg", "Sexual Eruption", "Hip Hop")
]

# Extract textual features from preprocessed data
songs = [entry[1] for entry in preprocessed_data]  # Song titles

# Create a TF-IDF vectorizer
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(songs)

# Calculate pairwise cosine similarity scores
similarity_scores = cosine_similarity(tfidf_matrix)

# Function to recommend similar songs based on user input
def recommend_similar_songs(user_input, top_n=5):
    # Find the index of the user input song
    user_input_index = songs.index(user_input)

    # Get the similarity scores for the user input song
    similarity_scores_user_input = similarity_scores[user_input_index]

    # Sort the songs based on similarity scores
    sorted_indices = similarity_scores_user_input.argsort()[::-1]
    top_similar_indices = sorted_indices[1:top_n + 1]  # Exclude the input song itself

    # Get the top similar songs
    top_similar_songs = [preprocessed_data[index] for index in top_similar_indices]

    return top_similar_songs

# prompt the user for input
user_input_song = input("Enter a song title: ")

# get recommended song based on user input
recommended_songs = recommend_similar_songs(user_input_song)

# Print the recommended songs
for song in recommended_songs:
    print(song)

