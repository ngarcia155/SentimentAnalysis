from transformers import pipeline
text = "Just watched the latest Marvel movie, and the special effects were mind-blowing! I love how they bring comic book characters to life."

pipe = pipeline('text-classification', model="cardiffnlp/twitter-roberta-large-topic-latest", return_all_scores=True)
predictions = pipe(text)[0]
predictions = [x for x in predictions if x['score'] > 0.5]
# predictions = [{'label': 'gaming', 'score': 0.899931013584137},{'label': 'sports', 'score': 0.5215537548065186}]
