class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        cleaned_triplets = []
        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue
            cleaned_triplets.append(triplet)
        
        if not cleaned_triplets:
            return False

        res = cleaned_triplets[0]
        for triplet in cleaned_triplets:
            res = [max(res[0], triplet[0]), max(res[1], triplet[1]), max(res[2], triplet[2])]
        
        return tuple(res) == tuple(target)
