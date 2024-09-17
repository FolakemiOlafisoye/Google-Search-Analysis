import streamlit as st
from googlesearch import search
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter

st.title("Google Search Analysis")
st.markdown("### A simple map for analyzing Google search results")

#Get the search query from the user
query = st.text_input("Enter your search query:",
placeholder="e.g. machine learning")

#Get the number of results from the user
num_results = st.slider("Number of results:", 1,10,5)

#Run the Google search
if st.button("Search"):
    results = []
    for i, result in enumerate(search(query)):
        if i >= num_results:
            break
        results.append(result)

    #Display the results
    st.write("### Search Results:")
    for i, result in enumerate(results):
        st.write(f"{i+1}.{result}")

    #Display the word count
    st.write("### Word Count:")
    words = ''.join(results).split()
    st.write(f"Total words: {len(words)}")

    #Display the top 5 most common words
    st.write("### Top 5 Most Common Words:")
    word_counts = Counter(words)
    for word, count in word_counts.most_common(5):
        st.write(f"{word}:{count}")

    #Display a word cloud
    st.write("### Word Cloud:")
    wordcloud = WordCloud(width=800, height=400).generate(''.join(words))
    plt.figure(figsize=(10,5))                                                                      
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    st.pyplot(plt)

    #Display a bar chart of the top 10 most common words
    st.write("### Top 10 Most Common Words (Bar Chart):")
    top_10_words = word_counts.most_common(10)
    words, counts = zip(*top_10_words)
    plt.figure(figsize=(10,5))
    plt.bar(words, counts)
    plt.xlabel('Word')
    plt.ylabel('Count')
    plt.xticks(rotation=90, ha='right', wrap=True)
    st.pyplot(plt)

st.write("")