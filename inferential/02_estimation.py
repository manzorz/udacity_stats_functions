import sys
import os
sys.path.append("C:/Users/Laptop/Documents/Repos/udacity_stats_functions/descriptive")
import normal_distribution_06
#import sampling_distributions_07

def lower_upper_confidence_intervals(avg, SD):
    #avg is x bar. The mean value at the "would be" point. ie Bieber Tweeter
    #SD is standard error (standard deviation of population dataset dvided by sqrt(number_in_sample)
    lower = avg-2*SD
    upper = avg+2*SD
    return((lower, upper))
    
#7. Quiz: Confidence Interval Bounds
print(lower_upper_confidence_intervals(40, 2.71))

#8. Quiz: Exact Z-Scores
print(get_z_from_p(0.975))