# BIRTHDAY CAKE CANDLES HACKER-RANK SOLUTION:

# function receiving an argument as the candles array.
def birthdayCakeCandles(candles):

    # declaring a variable to store the length of the candle array.
    x = len(candles)

    # declaring variables for the count and the maximum number.
    maximum_number = 0
    counter = 0

    # for-loop to iterate for the length of the candle array.
    for i in range (x):

        # nested if-statement to determine if the count should be increased.
        if candles[i] > maximum_number:

            maximum_number = candles[i]
            counter = 1

        elif candles[i] == maximum_number:

            counter+= 1
    
    # returning count for the most common index.
    return candles.count(max(candles))

candles_count = int(input().strip())
candles = list(map(int, input().rstrip().split()))

print(birthdayCakeCandles(candles))