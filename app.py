import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
from datasets import load_dataset

# Load the dataset
# df = pd.read_csv('./data.csv')
dataset = load_dataset("mmhshayer/books_data", data_files="data.csv")
df = pd.DataFrame( dataset["train"] )
# df = pd.read_csv(dataset)

# Function to get recommendations based on author, genre, and publisher
def get_recommendations(user_input_title):
    # Find the book in the dataset
    input_book = df[df['title'].str.contains(user_input_title, case=False, na=False)]
    
    if input_book.empty:
        return []
    
    # Extract features of the input book
    input_authors = input_book.iloc[0]['authors']
    input_genres = input_book.iloc[0]['genres']
    input_publisher = input_book.iloc[0]['publisher']
    
    # Filter books by author, genre, and publisher
    author_matches = df[df['authors'].str.contains(input_authors, case=False, na=False)]
    genre_matches = df[df['genres'].str.contains(input_genres, case=False, na=False)]
    publisher_matches = df[df['publisher'].str.contains(input_publisher, case=False, na=False)]
    
    # Combine the matches and remove the input book
    combined_matches = pd.concat([author_matches, genre_matches, publisher_matches]).drop_duplicates()
    combined_matches = combined_matches[combined_matches['title'] != input_book.iloc[0]['title']]
    
    # Sort the recommendations by the number of matches and ratings count
    combined_matches['match_score'] = combined_matches.apply(
        lambda x: (x['authors'] == input_authors) + (x['genres'] == input_genres) + (x['publisher'] == input_publisher), axis=1)
    combined_matches = combined_matches.sort_values(by=['match_score', 'ratingsCount'], ascending=False)
    
    # Return the top 5 recommended books with their authors, publishers, and genres
    recommended_books = combined_matches.head(5)[['title', 'authors', 'publisher', 'genres']]
    
    return recommended_books

# Streamlit App to host the Book Recommender System
def main():
    # Create a sidebar with tabs
    with st.sidebar:
        selected_tab = option_menu(
            "Menu", 
            ["Home", "Dataset Features", "Recommendation System"],
            icons=['house', 'bar-chart', 'book'],
            default_index=0,
        )

    # Home Tab
    if selected_tab == "Home":
        st.title("Machine Learning Book Recommender System")
        st.write("""
        This application provides a comprehensive analysis and recommendation system for a large dataset of books sourced from Amazon.

        ### About the Project
        The purpose of this project is to explore the rich dataset of books available on Amazon, provide insightful data exploration features, and offer personalized book recommendations based on various attributes.

        #### How the Data Was Cleaned
        The dataset underwent thorough cleaning to ensure data quality:
        - Columns such as image links, preview links, and info links were removed to focus on essential book attributes.
        - Rows lacking critical information (e.g., title, authors, and at least two of publisher, genres, or description) were filtered out.

        #### Features:
        - **Data Overview**: Get an overview of the dataset, including its structure and basic statistics.
        - **Book Recommendations**: Receive personalized recommendations based on specific attributes such as author, genre, and publisher.

        ### Dataset Information:
        The dataset includes various features of books, such as:
        - **Title**: The title of the book.
        - **Description**: A brief description of the book.
        - **Authors**: The names of the authors.
        - **Publisher**: The name of the publisher.
        - **Published Date**: The date when the book was published.
        - **Genres**: The genres of the book.
        - **Ratings Count**: The number of ratings the book has received.

        Explore the tabs to dive deeper into the dataset and discover new books!
        """)

    # Features Tab
    elif selected_tab == "Dataset Features":
        st.title("Dataset Features")
        st.subheader("Shape:")
        st.write(df.shape)
        st.subheader("Columns:")
        st.write(df.columns.tolist())
        st.subheader("Empty rows:")
        st.write(df.isnull().sum())
        st.subheader("Summary")
        st.write(df.head())
        st.subheader("Description:")
        st.write(df.describe(include='all'))

    # Recommendation System
    elif selected_tab == "Recommendation System":
        st.title("Recommendation System")

        user_input_title = st.text_input("Enter the book title to get recommendations:")

        if st.button("Recommend"):
            if user_input_title:
                recommended_books = get_recommendations(user_input_title)
                st.subheader("Recommended Books:")
                st.markdown("---")
                if not recommended_books.empty:
                    for i, row in recommended_books.iterrows():
                        st.markdown(f"**Index:** {i+1}")
                        st.markdown(f"**Title:** {row['title']}")
                        st.markdown(f"**Author:** {row['authors']}")
                        st.markdown(f"**Publisher:** {row['publisher']}")
                        st.markdown(f"**Genres:** {row['genres']}")
                        st.markdown("---")
                else:
                    st.write("No recommendations found. Please check the book title.")
            else:
                st.write("Please enter a valid book title.")

if __name__ == '__main__':
    main()

