"""Main program for calculating the ratio of escalators in repair. """
from parviainen.session2 import calculate_ratio

print "Currently, " + str(round(100*calculate_ratio())) + "% of not working escalators are doing so due to being in repair."