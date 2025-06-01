class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''
        Not too bad:
        maintain a stack and add tokens
        If we add an operand, evaluate it and that's the new top
        '''
        stack = []
        for t in tokens:
            if t in '+-*/':
                val1 = stack.pop()
                val2 = stack.pop()
                if t == '+':
                    stack.append(val2 + val1)
                if t == '*':
                    stack.append(val2 * val1)
                if t == '-':
                    stack.append(val2 - val1)
                if t == '/':
                    res = val2/val1
                    if res > 0:
                        res = int(res)
                    else:
                        res = -1 * int(abs(res))
                    stack.append(res)
            else:
                stack.append(int(t))
            #print(t, stack)
        return stack[0] # stack len should be 1