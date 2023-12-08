import RoBERTA_Go as RBG
import matplotlib.pyplot as plt
import numpy as np

# text = "That's enough. He's ready to talk. Run, run, run, as fast as you can. You can't catch me. I'm the gingerbread man! You're a monster. I'm not the monster here. You are. You, and the rest of that fairy tale trash, poisoning my perfect world. Now, tell me! Where are the others? Eat me! I've tried to be fair to you creatures. Now my patience has reached its end! Tell me or I'll... No, no, not the buttons. Not my gumdrop buttons. All right, then. Who's hiding them? Okay, I'll tell you. Do you know the muffin man? The muffin man? The muffin man. Yes, I know the muffin man, who lives on Drury Lane? Well, she's married to the muffin man. The muffin man? The muffin man! She's married to the muffin man."
# text = "Mom. You're making weird faces again. No, I'm not. You make weird faces, honey. Do you have to read at the table? Uh-huh. Yeah. Smaller bites, Dash. Yikes! Bob, could you help the carnivore cut his meat? Dash, you have something you wanna tell your father about school? Well, we dissected a frog. Dash got sent to the office again. Good. Good. No, Bob, that's bad. What? Dash got sent to the office again. What? What for? Nothing. He put a tack on the teacher's chair, during class. Nobody saw me. You could barely see it on the tape. They caught you on tape and you still got away with it? Whoa! You must have been booking. How fast were you going? We are not encouraging this. I'm not, I'm just asking how fast... Honey! Great. First the car, now I gotta pay to fix the table... What happened to the car? Here. I'm getting a new plate. So, how about you, Vi? How was school? Nothing to report. You've hardly touched your food. I'm not hungry for meatloaf. Well, it is leftover night. We have steak, pasta... What are you hungry for? Tony Rydinger. Shut up. Well, you are. I said, shut up, you little insect. Well, she is. Do not shout at the table. Honey! Kids! Listen to your mother. She'd eat if we were having Tony loaf. That's it! Stop it! You're gonna be toast! Stop running in the house. Sit down! Hey, no force fields! You started it. You sit down! You sit down! Violet! Simon J. Paladino, longtime advocate of superhero rights, is missing? Gazerbeam. Bob! It's time to engage. Do something! Don't just stand there! I need you to intervene! You want me to intervene? Okay. I'm intervening! Violet, let go of your brother. Hello? Get the door."

sentiment = RBG.emotion_analysis(text)

# Define the number of top emotions to display
num_top_emotions = 10

# Extract labels and scores from the sentiment analysis result
sentiments = sentiment[0]
sentiments.sort(key=lambda x: x['score'], reverse=True)
top_emotions = [entry['label'] for entry in sentiments[:num_top_emotions]]
top_scores = [entry['score'] for entry in sentiments[:num_top_emotions]]

# Create a radar chart
fig, ax = plt.subplots(figsize=(10, 8), subplot_kw={'projection': 'polar'})

# Add data to the radar chart
angles = np.linspace(0, 2 * np.pi, num_top_emotions, endpoint=False).tolist()
angles += angles[:1]  # Close the plot
top_scores += top_scores[:1]  # Close the plot
ax.fill(angles, top_scores, 'b', alpha=0.5)

# Set labels for each data point
ax.set_xticks(angles[:-1])
ax.set_xticklabels(top_emotions, rotation=45, ha="right")

# Display the radar chart
plt.title('Top 5 Emotions Radar Chart for Incredibles Scene')
plt.show()
