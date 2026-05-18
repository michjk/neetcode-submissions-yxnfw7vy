class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse=True)
        
        fleets = 1
        prev_time = (target - cars[0][0]) / cars[0][1]
        for i in range(1, len(cars)):
            cur_pos, cur_speed = cars[i]
            cur_time = (target - cur_pos) / cur_speed
            if cur_time > prev_time:
                fleets += 1
                prev_time = cur_time
        
        return fleets

