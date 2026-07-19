class Solution {
    private static final Map<Character, Character> CLOSE_TO_OPEN =
        Map.of(')', '(', '}', '{', ']', '[');

    public boolean isValid(String s) {
        Deque<Character> stack = new ArrayDeque<>();
        for (char c : s.toCharArray()) {
            if (CLOSE_TO_OPEN.containsKey(c)) { // closing bracket
                if (stack.isEmpty() || !stack.pop().equals(CLOSE_TO_OPEN.get(c)))
                    return false;
            } else {
                stack.push(c); // opening bracket
            }
        }
        return stack.isEmpty();
    }
}
