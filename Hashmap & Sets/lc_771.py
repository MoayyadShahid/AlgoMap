class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # create a dict / hash map to store the different stones we have
        types = {}
        # go through all stones and add them to the dict
        for stone in stones:
            types[stone] = types.get(stone, 0) + 1

        # now we will check how many jewels are in the stones
        count = 0
        # going through each jewel, we will see if it exists, if so we add them
        for jewel in jewels:
            # if the jewel exists, then add all its occurrences to count
            if types.get(jewel, 0) > 0:
                count += types.get(jewel, 0)
        # return count
        return count
