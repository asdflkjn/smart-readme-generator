# data_processor.py
import json
from datetime import datetime

class DataProcessor:
    """데이터 처리 전용 클래스"""
    
    def __init__(self):
        self.data = []
        self.processed_count = 0
    
    def load_json_data(self, file_path):
        """JSON 파일에서 데이터를 로드합니다"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                self.data = json.load(f)
            return True
        except Exception as e:
            print(f"데이터 로드 실패: {e}")
            return False
    
    def filter_data(self, condition):
        """조건에 맞는 데이터를 필터링합니다"""
        filtered = [item for item in self.data if condition(item)]
        return filtered
    
    def save_processed_data(self, output_path, processed_data):
        """처리된 데이터를 파일로 저장합니다"""
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(processed_data, f, ensure_ascii=False, indent=2)
            self.processed_count += 1
            return True
        except Exception as e:
            print(f"데이터 저장 실패: {e}")
            return False

def clean_text_data(text):
    """텍스트 데이터를 정리합니다"""
    if not text:
        return ""
    return text.strip().lower().replace("  ", " ")

def validate_email(email):
    """이메일 주소 유효성을 검사합니다"""
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def generate_report(data_list):
    """데이터 리스트로부터 요약 리포트를 생성합니다"""
    report = {
        "total_items": len(data_list),
        "generated_at": datetime.now().isoformat(),
        "summary": "데이터 처리 완료"
    }
    return report

if __name__ == "__main__":
    processor = DataProcessor()
    print("DataProcessor 초기화 완료!")
    
    # 샘플 테스트
    sample_data = [
        {"name": "홍길동", "email": "hong@example.com"},
        {"name": "김철수", "email": "kim@example.com"}
    ]
    
    processor.data = sample_data
    report = generate_report(processor.data)
    print("리포트:", report)