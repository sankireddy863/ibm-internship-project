# IBM PROJECT

##  Project Title

FAQ Chatbot using Python and Streamlit

##  Project Description

The FAQ Chatbot is designed to answer frequently asked questions based on a predefined set of questions and answers. When a user enters a question, the chatbot compares it with stored FAQ questions and returns the most suitable answer.

This project uses text preprocessing, TF-IDF vectorization, and cosine similarity to find the best matching FAQ.

##  Objectives

* Collect FAQs related to a topic.
* Store questions and answers in the program.
* Preprocess user input text.
* Match the user question with stored FAQs.
* Use cosine similarity to find the most similar question.
* Display the best matching answer as a chatbot response.
* Create a simple chat interface using Streamlit.

##  Technologies Used

* Python
* Streamlit
* Natural Language Processing
* Machine Learning
* TF-IDF
* Cosine Similarity

##  Libraries Used

```bash
streamlit
scikit-learn
```

##  Installation

###  Install Required Libraries

```bash
python -m pip install streamlit scikit-learn
```

##  How to Run

Run the project using:

```bash
python -m streamlit run faq_chatbot.py
```

After running the command, Streamlit will open the chatbot application in your browser.

##  Working Process

1. FAQs are collected and stored as questions and answers.
2. The user enters a question in the chatbot interface.
3. The question is preprocessed by converting it to lowercase and removing punctuation.
4. Stored FAQ questions are also preprocessed.
5. TF-IDF converts text into numerical vectors.
6. Cosine similarity compares the user question with FAQ questions.
7. The chatbot selects the most similar FAQ.
8. The best matching answer is displayed to the user.

##  Project Flow

```text
User Question
      ↓
Text Preprocessing
      ↓
TF-IDF Vectorization
      ↓
Cosine Similarity Matching
      ↓
Find Best Matching FAQ
      ↓
Display Chatbot Response
```

##  Features

* Simple chatbot interface.
* FAQ-based question answering.
* Text preprocessing.
* TF-IDF vectorization.
* Cosine similarity matching.
* Displays best matching answer.
* Beginner-friendly implementation.
* No complex API required.

##  Example Questions

The chatbot can answer questions like:

* What is artificial intelligence?
* What is machine learning?
* What is deep learning?
* What is natural language processing?
* What is a chatbot?
* What is Python?
* What is CodeAlpha internship?
* How many tasks should I complete?

## 📷 Output

The application displays:

* Chat input box
* Send button
* Chatbot response
* Matched FAQ question

##  Future Improvements

* Add more FAQs.
* Store FAQs in a CSV file.
* Add voice input.
* Add chat history.
* Improve UI design.
* Use advanced NLP models.
* Deploy the chatbot online.

##  Conclusion

This project successfully demonstrates an FAQ chatbot using Python, Streamlit, TF-IDF, and cosine similarity. It helps users get quick answers by matching their questions with stored FAQs.

 # Screenshot
 
 ```
Screenshot 2026-06-13 113453.png
```
##  Author

**SUDHA ANKIREDDY**
