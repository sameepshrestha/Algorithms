
# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwis
def canPlaceFlowers(flowerbed, n):
    count = 0
    i = 0
    while i < len(flowerbed):
        if flowerbed[i] == 0:
            # Check if the current and adjacent positions are also empty
            if i == 0 or flowerbed[i - 1] == 0:
                if i == len(flowerbed) - 1 or flowerbed[i + 1] == 0:
                    flowerbed[i] = 1  # Plant a flower at the current position
                    count += 1
        i += 1

    return count >= n
