import numpy as np
import random
import matplotlib.pyplot as plt

sample_sizes = [10, 100, 1000, 10000]

for size in sample_sizes:
    # Generate random samples from a normal distribution
    uniform_sample = np.random.uniform(0, 1, size)
    #exponential_sample = np.random.exponential(1, size)
    # Generate random samples from an exponential distribution
    #poisson_sample = np.random.poisson(500 ,size)
    
    # Plot histograms for the normal and exponential samples
    plt.hist(uniform_sample, bins=50, density=True, alpha=0.5, label=f'Uniform - Sample Size {size}')
    #plt.hist(exponential_sample, bins=50, density=True, alpha=0.5, label=f'Exponential - Sample Size {size}')
    #plt.hist(poisson_sample, bins=50, density=True, alpha=0.5, label=f'Poisson - Sample Size {size}')

plt.title('Histograms of Different Distributions')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend()
plt.show()