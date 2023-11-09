import matplotlib.pyplot as plt
import numpy as np
from IPython import display

class GameVisualizer:
    def __init__(self):
        plt.ion() 
        self.scores = []
        self.mean_scores = []

    def update_scores(self, scores, mean_scores):
        self.scores = scores
        self.mean_scores = mean_scores

    def plot_scores(self):
        plt.clf()
        plt.title('Évolution en temps réel de l\'IA')
        plt.xlabel('Partie')
        plt.ylabel('Score')
        plt.plot(self.scores, label='Score', color='#FF0000')  # Rouge
        plt.plot(self.mean_scores, label='Score moyen', color='#0000FF')  # Bleu
        plt.ylim(ymin=0)
        plt.legend()
        plt.show()
        plt.pause(0.1)

