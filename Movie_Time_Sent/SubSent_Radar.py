import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Function to create radar chart for a specified line range
def create_radar_chart(start_line, end_line, file_path='Shrek1_subLines_and_emotions.csv'):
    # Read the CSV file
    df = pd.read_csv(file_path)

    # Filter the DataFrame for the specified line range
    df = df.iloc[start_line:end_line]

    # Emotion labels to be plotted
    # emotions_to_check = ['sadness', 'anger', 'joy', 'fear', 'surprise']
    # Shrek
    emotions_to_check = ['neutral', 'disappointment', 'curiosity', 'approval', 'disapproval', 'excitement']

    # emotions_to_check = ['neutral', 'disapproval','anger']
    #Incredibles Scene
    # emotions_to_check = ['neutral', 'curiosity', 'anger','approval']

    # Calculate the average score for each emotion
    average_scores = {}
    for emotion in emotions_to_check:
        emotion_data = df[df.iloc[:, 1] == emotion]
        average_scores[emotion] = emotion_data.iloc[:, 2].mean() if not emotion_data.empty else 0

    # Prepare data for the radar chart
    labels = list(average_scores.keys())
    stats = list(average_scores.values())

    # Create radar chart
    angles=np.linspace(0, 2*np.pi, len(labels), endpoint=False).tolist()
    stats=np.concatenate((stats,[stats[0]]))
    angles+=angles[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.fill(angles, stats, alpha=0.25)
    ax.plot(angles, stats)

    # Label the plot
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)

    # Show the plot
    plt.title('Average Sentiment Scores for the Movie Shrek (Lines {} to {})'.format(start_line, end_line))
    plt.show()

# Example usage
create_radar_chart(200, 278)  # Change start_line and end_line as needed
