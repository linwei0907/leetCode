class Solution:
    def parse(self, s):
        tokens = []
        index = 0
        while index < len(s):
            if s[index] <= '9' and s[index] >= '0':
                number = []
                while index < len(s) and s[index] <= '9' and s[index] >= '0':
                    number.append(s[index])
                    index += 1
                tokens.append(int(''.join(number)))
            else:
                tokens.append(s[index])
                index += 1
        return tokens


    def insert_zero(self, tokens):
        res = []
        for index in range(len(tokens)):
            if tokens[index] == '-' and tokens[index - 1] == '(':
                res.append(0)
            res.append(tokens[index])

        return res

    def to_postfix(self, tokens):
        res = []
        num = []
        ops = []

        for t in tokens:
            if t in set(['+', '-']):
                while ops[-1] != '(':
                    res.append(ops.pop())
                ops.append(t)

            elif t == ')':
                while ops[-1] != '(':

                    res.append(ops.pop())

                ops.pop()

            elif t == '(':
                ops.append(t)

            else:
                res.append(t)

        return res

    def solve_postfix(self, tokens):
        res = []

        for t in tokens:
            if t == '+':
                two = res.pop()
                one = res.pop()
                res.append(one + two)

            elif t == '-':
                two = res.pop()
                one = res.pop()
                res.append(one - two)

            else:
                res.append(t)

        return res[-1]


    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        s = '(' + s + ')'

        tokens = self.parse(s)
        print(tokens)
        tokens = self.insert_zero(tokens)
        print(tokens)
        tokens = self.to_postfix(tokens)
        print(tokens)
        res = self.solve_postfix(tokens)

        return res      
