"""
In dumbClassifiers.py, we implement the world's simplest classifiers:
  1) Always predict +1
  2) Always predict the most frequent label from the training data
"""

from binary import *
from numpy  import *

import util

class AlwaysPredictOne(BinaryClassifier):
    """
    This defines the classifier that always predicts +1.
    """

    def __init__(self, opts):
        """
        do nothing
        """

    def online(self):
        return False

    def __repr__(self):
        return "AlwaysPredictOne"

    def predict(self, X):
        return 1       # return our constant prediction

    def train(self, X, Y):
        """
        do nothing
        """


class AlwaysPredictMostFrequent(BinaryClassifier):
    """
    This defines the classifier that always predicts the
    most frequent label from the training data.
    """

    def __init__(self, opts):
        """
        if we haven't been trained, assume most frequent class is +1
        """
        self.mostFrequentClass = 1

    def online(self):
        return False

    def __repr__(self):
        return "AlwaysPredictMostFrequent(%d)" % self.mostFrequentClass

    def predict(self, X):
        """
        X is an vector and we want to make a single prediction: Just
        return the most frequent class!
        """
        return self.mostFrequentClass
        util.raiseNotDefined()

    def train(self, X, Y):
        '''
        just figure out what the most frequent class is and store it in self.mostFrequentClass
        '''
        num1 = 0
        num2 = 0
        ln = len(Y)
        for i in range(0, ln):
            if Y[i] == 1: num1 += 1
            else: num2 += 1
        if num1 > num2:
            mostFrequentClass = 1
        else:
            mostFrequentClass = -1
        

        ### TODO: YOUR CODE HERE
       