class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []

        for token in tokens:
            if token not in "+/*-":
                nums.append(int(token))
            else:
                second = nums.pop()
                first = nums.pop()

                if token == "/":
                    nums.append(int(first / second))
                elif token == "*":
                    nums.append(first * second)
                elif token == "+":
                    nums.append(first + second)
                elif token == "-":
                    nums.append(first - second)
        return nums[0]