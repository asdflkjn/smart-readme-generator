def hello_world():
    """간단한 테스트 함수"""
    return "Hello, World!"

class TestClass:
    def __init__(self):
        self.name = "테스트"
    
    def greet(self):
        return f"안녕하세요, {self.name}입니다!"

if __name__ == "__main__":
    print(hello_world())
    test = TestClass()
    print(test.greet())