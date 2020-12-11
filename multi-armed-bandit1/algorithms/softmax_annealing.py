import random
import math


class SoftmaxAnnealing():
    def __init__(self, n_arms, annealing_factor=.0000001):
        self.annealing_factor = annealing_factor
        self.n_arms = n_arms
        self.counts = [0] * n_arms
        self.values = [0.0] * n_arms
        self.alpha = [1] * n_arms
        self.beta = [1] * n_arms

    def reset(self):
        self.counts = [0] * self.n_arms
        self.values = [0.0] * self.n_arms
        self.alpha = [1] * self.n_arms
        self.beta = [1] * self.n_arms

    def select_arm(self):
        t = sum(self.counts) + 1
        temperature = 1 / math.log(t + self.annealing_factor)
        total = sum([math.exp(value / temperature) for value in self.values])
        probs = [math.exp(value / temperature) / total for value in self.values]
        threshold = random.random()
        cum_prob = 0.0
        for idx in range(len(probs)):
            prob = probs[idx]
            cum_prob += prob
            if cum_prob > threshold:
                return idx
        return len(probs) - 1

    def update(self, chosen_arm, reward):
        self.counts[chosen_arm] += 1
        self.alpha[chosen_arm] += reward
        self.beta[chosen_arm] += 1 - reward
        n = float(self.counts[chosen_arm])
        value = self.values[chosen_arm]
        new_value = ((n - 1) / n) * value + (1 / n) * reward
        self.values[chosen_arm] = new_value
