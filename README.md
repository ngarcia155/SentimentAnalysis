# SentimentAnalysis

This repository contains Python scripts that demonstrate how to perform sentiment analysis on text data. Sentiment analysis is the process of determining the sentiment or emotion expressed in a piece of text, whether it's positive, negative, or neutral. We provide three different examples of sentiment analysis using various libraries and approaches.

## Table of Contents

- [Prerequisites](#prerequisites)
- [IMDb Movie Review Sentiment Analysis](#imdb-movie-review-sentiment-analysis)
- [Twitter RoBERTa-Based Sentiment Analysis](#twitter-roberta-based-sentiment-analysis)
- [Web Scraping IMDb Movie Reviews](#web-scraping-imdb-movie-reviews)

## Prerequisites

Before running the provided Python scripts, make sure you have the following installed:

- Python
- Necessary Python libraries for each script (mentioned in respective sections)
- A machine with compatible GPU for improved performance (optional)

You need to install the required libraries, here is the install command for PyTorch  using `pip`. Example:

```bash
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

## IMDb Movie Review Sentiment Analysis

The first script demonstrates sentiment analysis of movie reviews from IMDb using the Natural Language Toolkit (NLTK) and the VADER sentiment analysis tool. It covers the following steps:

- Tokenization
- Part-of-speech tagging
- Named entity chunking
- Sentiment analysis using VADER

## Twitter RoBERTa-Based Sentiment Analysis

Documentation:

https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment

The second script showcases sentiment analysis of movie reviews using the Hugging Face Transformers library and a pre-trained Twitter RoBERTa-based model. It involves:

- Utilizing a pre-trained model from Hugging Face Transformers
- Tokenizing the text
- Calculating sentiment scores
- Assigning a sentiment label

Refer to the [Twitter RoBERTa-Based Sentiment Analysis README](./Instructions/Read_RobertaModel.md) for detailed instructions and explanations.

## Web Scraping IMDb Movie Reviews

The third script demonstrates web scraping of movie reviews from IMDb and storing them in a pandas DataFrame. It covers the following steps:

- Sending HTTP requests to the IMDb review page
- Parsing HTML content using BeautifulSoup
- Retrieving reviews and star ratings
- Storing data in a DataFrame

Refer to the [Web Scraping IMDb Movie Reviews README](./Instructions/Read_ReviewToCSV.md) for detailed instructions and explanations.

---

## References

- https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment
- https://github.com/samlowe/go_emotions-dataset/blob/main/eval-roberta-base-go_emotions.ipynb
- https://huggingface.co/SamLowe/roberta-base-go_emotions?text=Today+is+going+to+be+a+wonderful+day.
- https://huggingface.co/roberta-base
- 
