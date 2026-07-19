class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> lastPos = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int rem = target - nums[i];
            if (lastPos.containsKey(rem))
                return new int[]{lastPos.get(rem), i};
            lastPos.put(nums[i], i);
        }
        return new int[]{};
    }
}
