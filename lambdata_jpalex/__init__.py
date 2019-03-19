import numpy as np
import pandas as pd

class Statistic:
  """
  Contains statistic functions helper
  """
  def __init__(self, numbers = [1,2], confidence=0.95):
    """
    numbers = array of numbers
    confidence = 0 to 1
    """
    self.numbers = numbers
    self.confidence = confidence
    
  def mean(self):
    """
    Calculate the mean of dataset
    """
    mean = sum(self.numbers)/len(self.numbers)
    return mean
  
  def variance(self):
    """
    Calculate the variances of sample dataset (n - 1)
    """
    differences = [(x-mean(self.numbers))**2 for x in self.numbers]
    variance = sum(differences)/(len(differences)-1)
    return variance
  
  def stdev(self):
    """
    Calculate the standard deviation of sample dataset (n - 1)
    """
    stdev = np.sqrt(mean_variance(numbers))
    return stdev
