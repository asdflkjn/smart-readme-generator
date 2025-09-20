# src/smart_generator.py (완전 새 버전)
import ast
import os
from pathlib import Path
from datetime import datetime

class SmartReadmeGenerator:
    def __init__(self):
        self.templates = {
            'web': ['flask', 'django', 'fastapi', 'app', 'server'],
            'data': ['pandas', 'numpy', 'analysis', 'data', 'ml'],
            'automation': ['script', 'tool', 'auto', 'bot'],
            'game': ['game', 'pygame', 'play'],
        }
    
    def detect_project_type(self, project_analysis):
        all_code = ' '.join(project_analysis.get('all_functions', [])).lower()
        all_code += ' '.join(project_analysis.get('all_classes', [])).lower()
        
        for proj_type, keywords in self.templates.items():
            if any(keyword in all_code for keyword in keywords):
                return proj_type
        return 'general'
    
    def generate_smart_description(self, project_analysis):
        functions = project_analysis.get('all_functions', [])
        classes = project_analysis.get('all_classes', [])
        
        features = []
        if any('hello' in f.lower() for f in functions):
            features.append("인사 기능")
        if any('test' in f.lower() for f in functions):
            features.append("테스트 도구")
        if any('get' in f.lower() for f in functions):
            features.append("데이터 조회")
        if any('set' in f.lower() or 'save' in f.lower() for f in functions):
            features.append("데이터 저장")
        if classes:
            features.append("객체 지향 설계")
            
        return features
    
    def generate_usage_examples(self, project_analysis):
        functions = project_analysis.get('all_functions', [])
        classes = project_analysis.get('all_classes', [])
        
        examples = []
        
        for func in functions[:3]:
            if not func.startswith('_'):
                examples.append("result = " + func + "()")
        
        for cls in classes[:2]:
            examples.append(cls.lower() + " = " + cls + "()")
            examples.append("print(" + cls.lower() + ".greet())")
        
        return examples
    
    def generate_readme(self, project_analysis):
        project_type = self.detect_project_type(project_analysis)
        features = self.generate_smart_description(project_analysis)
        examples = self.generate_usage_examples(project_analysis)
        
        titles = {
            'web': '🌐 웹 애플리케이션',
            'data': '📊 데이터 분석 도구', 
            'automation': '🤖 자동화 스크립트',
            'game': '🎮 게임 프로젝트',
            'general': '🐍 Python 프로젝트'
        }
        
        title = titles.get(project_type, '🐍 Python 프로젝트')
        current_date = datetime.now().strftime('%Y년 %m월 %d일')
        
        # 문자열 연결 방식으로 변경
        readme = "# " + title + "\n\n"
        readme += "> ⚡ **자동 생성된 README** - " + current_date + "\n\n"
        readme += "## 📋 프로젝트 개요\n\n"
        readme += "이 프로젝트는 **" + str(project_analysis['python_files']) + "개의 Python 파일**로 구성된 프로그램입니다.\n\n"
        
        readme += "### 🎯 주요 특징\n"
        readme += self._format_features(features) + "\n\n"
        
        readme += "### 📊 코드 통계\n"
        readme += "- **Python 파일**: " + str(project_analysis['python_files']) + "개\n"
        readme += "- **JavaScript 파일**: " + str(project_analysis['js_files']) + "개\n"
        readme += "- **함수**: " + str(len(project_analysis.get('all_functions', []))) + "개\n"
        readme += "- **클래스**: " + str(len(project_analysis.get('all_classes', []))) + "개\n\n"
        
        readme += "## 🚀 빠른 시작\n\n"
        readme += "### 설치\n"
        readme += "```bash\n"
        readme += "git clone <repository-url>\n"
        readme += "cd <project-name>\n"
        readme += "pip install -r requirements.txt\n"
        readme += "```\n\n"
        
        readme += "### 사용법\n"
        readme += "```python\n"
        for example in examples[:5]:
            readme += example + "\n"
        readme += "```\n\n"
        
        readme += "## 📚 API 문서\n\n"
        readme += "### 📋 함수 목록\n"
        readme += self._format_functions(project_analysis.get('all_functions', [])) + "\n\n"
        
        readme += "### 🏗️ 클래스 목록\n"
        readme += self._format_classes(project_analysis.get('all_classes', [])) + "\n\n"
        
        readme += "## 🛠️ 개발 환경\n\n"
        readme += "- **Python**: 3.7+\n"
        readme += "- **플랫폼**: Windows, macOS, Linux\n"
        readme += "- **IDE**: VS Code 권장\n\n"
        
        readme += "## 🤝 기여하기\n\n"
        readme += "1. 🍴 Fork the Project\n"
        readme += "2. 🌿 Create your Feature Branch\n"
        readme += "3. 💾 Commit your Changes\n"
        readme += "4. 📤 Push to the Branch\n"
        readme += "5. 🔄 Open a Pull Request\n\n"
        
        readme += "## 📄 라이선스\n\n"
        readme += "MIT License - 자유롭게 사용하세요!\n\n"
        readme += "---\n"
        readme += "*📝 이 README는 Smart README Generator로 자동 생성되었습니다.*\n"
        
        return readme
    
    def _format_features(self, features):
        if not features:
            return "- 🔧 다양한 유틸리티 기능"
        return '\n'.join(["- ✨ " + feature for feature in features])
    
    def _format_functions(self, functions):
        if not functions:
            return "- 함수가 없습니다"
        
        formatted = []
        for func in functions:
            if not func.startswith('_'):
                formatted.append("- `" + func + "()` - " + func + " 기능을 수행합니다")
        
        return '\n'.join(formatted) if formatted else "- 공개 함수가 없습니다"
    
    def _format_classes(self, classes):
        if not classes:
            return "- 클래스가 없습니다"
        
        return '\n'.join(["- `" + cls + "` - " + cls + " 객체를 정의합니다" for cls in classes])

# 테스트
if __name__ == "__main__":
    generator = SmartReadmeGenerator()
    
    test_analysis = {
        'python_files': 1,
        'js_files': 0,
        'all_functions': ['hello_world', 'greet', 'get_data', 'save_file'],
        'all_classes': ['TestClass', 'DataProcessor']
    }
    
    print("🎯 스마트 README 생성 중...")
    readme = generator.generate_readme(test_analysis)
    
    print("✅ 생성 완료!")
    print("\n" + "="*60)
    print(readme)
    print("="*60)
    
    with open('README_smart.md', 'w', encoding='utf-8') as f:
        f.write(readme)
    
    print("\n💾 README_smart.md 파일로 저장됨!")