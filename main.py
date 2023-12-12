#The total number of combinations when rolling two six-sided dice is calculated as 6 * 6 = 36.
total_combinations = 6 * 6
print("Total Combinations:", total_combinations)
#This section generates a 6x6 matrix (distribution) to represent all possible sums resulting from the two dice rolls.
# For example, distribution[0][0] represents the sum when both dice roll a 1, distribution[0][1]
distribution = [[0] * 6 for _ in range(6)]
#probability to store the probabilities of getting each possible sum (from 2 to 12) when rolling two dice.
for i in range(1, 7):
    for j in range(1, 7):
        distribution[i-1][j-1] = i + j

print("Distribution of Combinations:")
for row in distribution:
    print(row)
probability = [0] * 11

for i in range(1, 7):
    for j in range(1, 7):
        probability[i+j-2] += 1

total_combinations = 6 * 6
'''Probability of Sum = 2:
The sum 2 can only be obtained when both dice roll a 1. There's only one combination (1, 1) that results in a sum of 2.
Therefore, the probability of getting a sum of 2 is 1/36.

Probability of Sum = 3:
The sum 3 can be obtained in two ways: (1, 2) or (2, 1).
Therefore, the probability of getting a sum of 3 is 2/36 or 1/18.

Probability of Sum = 4:
Similarly, the sum 4 can be obtained in three ways: (1, 3), (2, 2), or (3, 1).
Therefore, the probability of getting a sum of 4 is 3/36 or 1/12.'''
print("Probability of Sums:")
for i in range(2, 13):
    print("P(Sum =", i, ") =", probability[i-2] / total_combinations)

