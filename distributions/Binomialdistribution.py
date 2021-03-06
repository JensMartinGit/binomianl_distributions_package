import math
import matplotlib.pyplot as plt
from .Generaldistribution import Distribution

class Binomial(Distribution):
    """ Binomial distribution class for calculating and 
    visualizing a Binomial distribution.
    
    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats to be extracted from the data file
        p (float) representing the probability of an event occurring
        n (int) the total number of trials
    
    
    TODO: Fill out all TODOs in the functions below
            
    """
    
    
    def __init__(self, prob=.5, size=20):
                    
        self.p = prob # store the probability of the distribution in an instance variable p
        self.n = size # store the size of the distribution in an instance variable n
        mu = self.calculate_mean()
        sigma = self.calculate_stdev()
        
        Distribution.__init__(self, mu, sigma)
                
                  
    
    def calculate_mean(self):
    
        """Function to calculate the mean from p and n
        
        Args: 
            None
        
        Returns: 
            float: mean of the data set
    
        """
                     
        self.mu = self.p * self.n
        return self.mu



    def calculate_stdev(self):

        """Function to calculate the standard deviation from p and n.
        
        Args: 
            None
        
        Returns: 
            float: standard deviation of the data set
    
        """
          
        self.stdev = math.sqrt(self.n * self.p * (1-self.p))
        return self.stdev
        
        
    def replace_stats_with_data(self):
    
        """Function to calculate p and n from the data set
        
        Args: 
            None
        
        Returns: 
            float: the p value
            float: the n value
    
        """        
                
        data_list = self.data
        self.n = len(data_list)
        self.p = sum(data_list)/len(data_list)
        self.calculate_stdev()
        self.calculate_mean()
        return self.p, self.n
    
    
        
    def plot_bar(self):
        """Function to output a histogram of the instance variable data using 
        matplotlib pyplot library.
        
        Args:
            None
            
        Returns:
            None
        """
                   
        data_list = self.data
        vals = [0,1]
        counts = [data_list.count(x) for x in vals] 
        
        plt.bar(vals, counts)
        plt.title('Data Distribution')
        plt.xlabel('Values')
        plt.ylabel('Value Counts')
        plt.xticks(vals)
        
        
        
    def pdf(self, k):
        """Probability density function calculator for the gaussian distribution.
        
        Args:
            k (float): point for calculating the probability density function
            
        
        Returns:
            float: probability density function output
        """
        
        n = self.n
        p = self.p
        return math.factorial(n)/(math.factorial(n-k) * math.factorial(k)) * p ** k * (1-p) ** (n-k)
        
             

    def plot_bar_pdf(self):

        """Function to plot the pdf of the binomial distribution
        
        Args:
            None
        
        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot
            
        """
            
        n = self.n
        x_list = list(range(n+1))
        y_list = [self.pdf(x) for x in x_list]
        
        plt.bar(x_list, y_list)
        plt.title('Probability Density Function')
        plt.x_label('Number of Successes')
        plt.ylabel('Probability')
        
        return x_list, y_list
    
    
                
    def __add__(self, other):
        
        """Function to add together two Binomial distributions with equal p
        
        Args:
            other (Binomial): Binomial instance
            
        Returns:
            Binomial: Binomial distribution
            
        """
        
        try:
            assert self.p == other.p, 'p values are not equal'
        except AssertionError as error:
            raise
        
        p = self.p
        n = self.n + other.n
                
        new_binomial = Binomial(p, n)
        return new_binomial
        
        
    def __repr__(self):
    
        """Function to output the characteristics of the Binomial instance
        
        Args:
            None
        
        Returns:
            string: characteristics of the Gaussian
        
        """
          
        return 'mean {}, standard deviation {}, p {}, n {}'.format(self.mean, self.stdev, self.p, self.n)
