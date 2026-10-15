import streamlit as st
import string

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(
    page_title="FAQ Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 FAQ Chatbot")
st.write("Ask a question and get the best matching FAQ answer.")

# FAQ dataset
faqs = {
    "What is artificial intelligence?":
    "Artificial Intelligence is a branch of computer science that makes machines think and act like humans.",

    "What is machine learning?":
    "Machine Learning is a part of AI where machines learn from data and improve automatically.",

    "What is deep learning?":
    "Deep Learning uses neural networks to solve complex problems.",

    "What is natural language processing?":
    "Natural Language Processing helps computers understand human language.",

    "What is computer vision?":
    "Computer Vision helps computers understand images and videos.",

    "What is a chatbot?":
    "A chatbot is a software application that can communicate with users and answer questions.",

    "What is Python?":
    "Python is a simple and powerful programming language used in AI and machine learning.",

    "What is CodeAlpha internship?":
    "CodeAlpha internship provides hands-on project experience in different technology domains.",

    "How many tasks should I complete?":
    "You should complete at least two or three tasks from the given internship task list.",

    "What technique is used in this chatbot?":
    "This chatbot uses TF-IDF vectorization and cosine similarity to find the best matching FAQ.",

    "What is cosine similarity?":
    "Cosine similarity is used to measure how similar two text sentences are."
}

# Text preprocessing
def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text

questions = list(faqs.keys())
answers = list(faqs.values())

processed_questions = [preprocess_text(q) for q in questions]

st.subheader("Chat with FAQ Bot")

user_question = st.text_input("You:")

if st.button("Send"):
    if user_question.strip() == "":
        st.warning("Please enter a question.")
    else:
        processed_user_question = preprocess_text(user_question)

        all_questions = processed_questions + [processed_user_question]

        vectorizer = TfidfVectorizer(stop_words="english")
        vectors = vectorizer.fit_transform(all_questions)

        similarity_scores = cosine_similarity(vectors[-1], vectors[:-1])

        best_match_index = similarity_scores.argmax()
        best_score = similarity_scores[0][best_match_index]

        st.write("### 🤖 Bot:")

        if best_score > 0.2:
            st.success(answers[best_match_index])
            st.write("Matched FAQ:", questions[best_match_index])
        else:
            st.error("Sorry, I could not find a suitable answer.")