# calculator.py
class Calculator:
    """간단한 계산기 클래스"""
    
    def __init__(self):
        self.result = 0
    
    def add(self, x, y):
        """두 숫자를 더합니다"""
        return x + y
    
    def subtract(self, x, y):
        """두 숫자를 뺍니다"""
        return x - y
    
    def multiply(self, x, y):
        """두 숫자를 곱합니다"""
        return x * y
    
    def divide(self, x, y):
        """두 숫자를 나눕니다"""
        if y != 0:
            return x / y
        else:
            return "0으로 나눌 수 없습니다"

def calculate_area(length, width):
    """직사각형 넓이를 계산합니다"""
    return length * width

def calculate_volume(length, width, height):
    """직육면체 부피를 계산합니다"""
    return length * width * height

if __name__ == "__main__":
    calc = Calculator()
    print("5 + 3 =", calc.add(5, 3))
    print("직사각형 넓이:", calculate_area(5, 3))