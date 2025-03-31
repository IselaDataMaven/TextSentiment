# 😄😢 Text Sentiment Recognition Challenge 😠😲

Category   ➡️   Data Science

Subcategory   ➡️   Machine Learning Engineer (NLP)

Difficulty   ➡️   Easy

## 🌐 Background

In the realm of natural language processing (NLP), understanding the emotions behind texts is crucial for enhancing human-computer interaction. SentimentTech invites AI researchers and developers to engage in the Text Sentiment Recognition Challenge. The objective is to utilize natural language processing models to identify and classify sentiments expressed in text messages. This challenge aims to improve sentiment analysis technologies, which are vital for customer service, social media monitoring, and various applications in AI-driven analytics, using the Sentiment140 Dataset.

![Image]()

### 🗂️ Dataset

Participants will be granted access to the "Sentiment140 Dataset," comprising:

- `idx`: Identifier of the text messages.
- `date`: Timestamp of the text messages.
- `text`: Content of the text messages.
- `target`: Sentiment labels (Positive, Negative). This is the target variable to be predicted.

This dataset plays a crucial role in training your models to accurately identify and classify the sentiments expressed in text messages.


### 📊 Data Processing:

Implement the appropriate data preprocessing techniques to effectively manage and prepare the text data for sentiment analysis.


### 🤖 Model

Choose and train an NLP model that fits the challenge. While the choice of model is yours, consider exploring model architectures like recurrent neural networks (RNNs), long short-term memory (LSTM) networks or transformer-based models such as BERT for sentiment classification.


## 📂 Respository Structure

The repository structure is provided and must be adhered to strictly:

```
|__README.md
|__requirements.txt
|
|__data
|  |__train
|  |  |__train.csv
|  |
|  |__test
|     |__test.csv
|
|__src
|  |__data_processing.py
|  |__model_training.py 
|  |__model_prediction.py
|  |__utils.py
|
|__models
|  |__model.pkl
|
|__predictions
   |__example_predictions.json
   |__predictions.json

```
The `predictions` folder should contain the `predictions.json` file with your model's predicted sentiment labels.


## 🎯 Tasks:

Develop a system using natural language processing models to accurately identify and classify sentiments in text messages. The system should be able to discern positive and negative sentiments to align with user experiences and applications in AI analytics.


## 📤 Submission

Submit a `predictions.json` file containing your system's sentiment classifications for text messages. Ensure the file is formatted correctly, with message ids as keys and the predicted sentiment labels as values.
predictions.json:
```json
{
     "target": {
        "2200003313": "positive",
        "1467998601": "positive",
        "2300049112": "negative",
        "1993474319": "positive",
        "2256551006": "negative",
        ...
    }
}

```

## 📊 Evaluation

The effectiveness of your sentiment recognition system will be assessed based on its accuracy in classifying the sentiment of text messages. Metrics such as precision, recall, and the F1 score may be employed to evaluate the relevance and accuracy of your classifications.

**⚠️ Please note:**  
All submissions might undergo a manual code review process to ensure that the work has been conducted honestly and adheres to the highest standards of academic integrity. Any form of dishonesty or misconduct will be addressed seriously, and may lead to disqualification from the challenge.

Ensure that all data manipulation and model training strictly utilize the libraries mentioned in requirements.txt.


## ❓ FAQs

### Q1: What is the goal of the Text Sentiment Recognition Challenge?
A1: To develop a system capable of accurately identifying and classifying sentiments expressed in text messages.

### Q2: What type of data will I be working with?
A2: You will work with a dataset that includes text messages and their sentiment labels.

### Q3: Are there any recommended models or algorithms?
A3: Exploring RNNs, LSTMs or transformer-based models like BERT is encouraged, ensuring you utilize the libraries from requirements.txt.

### Q4: How will the system's effectiveness be evaluated?
A4: Effectiveness will be assessed using precision, recall, and the F1 score, focusing on the accuracy of sentiment classifications.