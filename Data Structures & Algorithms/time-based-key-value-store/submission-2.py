from collections import defaultdict
import bisect

class TimeMap:

    def __init__(self):
        self.key_time_2_value = {}
        self.key_2_time_list = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_time_2_value[(key, timestamp)] = value
        self.key_2_time_list[key].append(timestamp)


    def get(self, key: str, timestamp: int) -> str:
        if (key, timestamp) in self.key_time_2_value:
            return self.key_time_2_value[(key, timestamp)]
        if self.key_2_time_list[key]:
            idx = bisect.bisect_left(self.key_2_time_list[key], timestamp)
            if idx > 0:
                prev = self.key_2_time_list[key][idx - 1]
                return self.key_time_2_value[(key, prev)]
        return ""
        
