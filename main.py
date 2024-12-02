class ArithmaGenie:
    def __init__(self):
        self.supported_bases = [2, 10, 16]  # Supports binary, decimal, and hexadecimal operations

    def add(self, a, b):
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)
        result = []
        carry = 0
        for i in range(max_len - 1, -1, -1):
            digit_sum = int(a[i]) + int(b[i]) + carry
            result.append(str(digit_sum % 10))
            carry = digit_sum // 10
        if carry:
            result.append(str(carry))
        return ''.join(result[::-1])

    def subtract(self, a, b):
        if self.compare(a, b) < 0:
            return '-' + self.subtract(b, a)
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)
        result = []
        borrow = 0
        for i in range(max_len - 1, -1, -1):
            digit_diff = int(a[i]) - int(b[i]) - borrow
            if digit_diff < 0:
                digit_diff += 10
                borrow = 1
            else:
                borrow = 0
            result.append(str(digit_diff))
        return ''.join(result[::-1]).lstrip('0') or '0'

    def multiply(self, a, b):
        result = [0] * (len(a) + len(b))
        a = a[::-1]
        b = b[::-1]
        for i in range(len(a)):
            for j in range(len(b)):
                result[i + j] += int(a[i]) * int(b[j])
                if result[i + j] >= 10:
                    result[i + j + 1] += result[i + j] // 10
                    result[i + j] %= 10
        return ''.join(map(str, result[::-1])).lstrip('0') or '0'

    def divide(self, a, b):
        if b == '0':
            raise ValueError("Cannot divide by zero")
        quotient = '0'
        remainder = a
        while self.compare(remainder, b) >= 0:
            remainder = self.subtract(remainder, b)
            quotient = self.add(quotient, '1')
        return quotient, remainder

    def factorial(self, a):
        result = '1'
        while self.compare(a, '1') > 0:
            result = self.multiply(result, a)
            a = self.subtract(a, '1')
        return result

    def compare(self, a, b):
        a, b = a.lstrip('0'), b.lstrip('0')  # Strip leading zeros
        if len(a) > len(b):
            return 1
        if len(a) < len(b):
            return -1
        return (a > b) - (a < b)

    def parse_and_compute(self, expr):
        tokens = expr.split()
        if tokens[0] == 'add':
            return self.add(tokens[1], tokens[2])
        elif tokens[0] == 'subtract':
            return self.subtract(tokens[1], tokens[2])
        elif tokens[0] == 'multiply':
            return self.multiply(tokens[1], tokens[2])
        elif tokens[0] == 'divide':
            quotient, remainder = self.divide(tokens[1], tokens[2])
            return f"quotient: {quotient}, remainder: {remainder}"
        elif tokens[0] == 'factorial':
            return self.factorial(tokens[1])
        else:
            return "Unsupported operation"

    def repl(self):
        print("Welcome to ArithmaGenie Calculator")
        print("These are the supported operations: add, subtract, multiply, divide, factorial")
        print("To interact with ArithmaGenie, use commands such as : add 1 9")
        print("Type 'exit' to quit at the end of your operations. Enjoy calculating!")
        while True:
            user_input = input("ArithmaGenie> ").strip()
            if user_input.lower() == 'exit':
                print("Goodbye!")
                break
            try:
                result = self.parse_and_compute(user_input)
                print(result)
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    print("Starting ArithmaGenie...")
    calculator = ArithmaGenie()
    calculator.repl()
