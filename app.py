#!/usr/bin/env python3
from flask import Flask, request, render_template, jsonify
import mysql.connector
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# MySQL connection configuration
mysql_host = 'localhost'
mysql_user = 'root'
mysql_password = 'Nomoya123##'
mysql_database = 'music_app'

connection = mysql.connector.connect(
    host=mysql_host,
    user=mysql_user,
    password=mysql_password,
    database=mysql_database
)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/search", methods=["POST"])
def search():
    query = request.form.get("query")  # Get the query from the form

    # Perform recommendation based on the query
    results = perform_recommendation(query)    
    return render_template("results.html", results=results)


@app.route("/recommend", methods=["GET"])
def recommend():
    query = request.args.get("query")  # Get the query parameter from the request

    # Perform recommendation based on the query and get the results
    results = perform_recommendation(query)

    return jsonify(results)
 

    # Perform content-based filtering using TF-IDF vectorization
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([entry[1] for entry in preprocessed_data])

    # Get the user input's TF-IDF vector
    user_input_tfidf = vectorizer.transform([query])

    # Calculate the cosine similarity between user input and preprocessed data
    similarity_scores = cosine_similarity(user_input_tfidf, tfidf_matrix)

    # Get the indices of top similar songs
    top_similar_indices = similarity_scores.argsort()[0][-5:][::-1]

    # Get the recommended songs based on the indices
    recommended_songs = [preprocessed_data[index] for index in top_similar_indices]

    return recommended_songs


if __name__ == "__main__":
    app.run()