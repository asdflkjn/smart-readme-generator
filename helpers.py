# helpers.py
from datetime import datetime
import random

def get_current_time():
    """현재 시간을 문자열로 반환합니다"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def generate_random_id():
    """랜덤 ID를 생성합니다"""
    return f"ID_{random.randint(1000, 9999)}"

def format_file_size(bytes_size):
    """바이트 크기를 사람이 읽기 쉬운 형태로 변환"""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes_size < 1024.0:
            return f"{bytes_size:.2f} {unit}"
        bytes_size /= 1024.0
    return f"{bytes_size:.2f} PB"

class ColorHelper:
    """색상 관련 유틸리티 클래스"""
    
    COLORS = {
        'red': '#FF0000',
        'green': '#00FF00', 
        'blue': '#0000FF',
        'yellow': '#FFFF00'
    }
    
    @classmethod
    def get_color_code(cls, color_name):
        """색상 이름으로 헥스 코드를 반환합니다"""
        return cls.COLORS.get(color_name.lower(), '#000000')
    
    @classmethod
    def add_color(cls, name, hex_code):
        """새로운 색상을 추가합니다"""
        cls.COLORS[name.lower()] = hex_code

if __name__ == "__main__":
    print(f"현재 시간: {get_current_time()}")
    print(f"랜덤 ID: {generate_random_id()}")
    print(f"파일 크기 예시: {format_file_size(1048576)}")
    
    color_helper = ColorHelper()
    print(f"빨간색 코드: {color_helper.get_color_code('red')}")