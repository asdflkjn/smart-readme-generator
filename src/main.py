# src/main.py (최종 통합 버전)
import os
import ast
from pathlib import Path
from smart_generator import SmartReadmeGenerator

def analyze_python_file(file_path):
    """Python 파일 내용 분석"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        tree = ast.parse(content)
        
        functions = []
        classes = []
        
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                functions.append(node.name)
            elif isinstance(node, ast.ClassDef):
                classes.append(node.name)
        
        return {
            'functions': functions,
            'classes': classes,
            'lines': len(content.splitlines())
        }
    except Exception as e:
        return {'error': str(e), 'functions': [], 'classes': []}

def analyze_project(project_path):
    """프로젝트 전체 분석"""
    path = Path(project_path)
    
    # 다양한 파일 타입 지원
    python_files = list(path.glob('*.py'))
    js_files = list(path.glob('*.js'))
    
    print(f"=== 🔍 프로젝트 분석 중... ===")
    print(f"📁 Python 파일: {len(python_files)}개")
    print(f"📁 JavaScript 파일: {len(js_files)}개")
    
    # 모든 함수와 클래스 수집
    all_functions = []
    all_classes = []
    
    for py_file in python_files:
        if py_file.name == 'main.py':  # 자기 자신 제외
            continue
            
        print(f"\n📄 {py_file.name} 분석 중...")
        analysis = analyze_python_file(py_file)
        
        if 'error' not in analysis:
            print(f"  ✅ 함수: {len(analysis['functions'])}개")
            print(f"  ✅ 클래스: {len(analysis['classes'])}개")
            print(f"  ✅ 줄 수: {analysis['lines']}줄")
            
            all_functions.extend(analysis['functions'])
            all_classes.extend(analysis['classes'])
        else:
            print(f"  ❌ 에러: {analysis['error']}")
    
    return {
        'python_files': len(python_files),
        'js_files': len(js_files),
        'all_functions': all_functions,
        'all_classes': all_classes
    }

def generate_readme_for_project(project_path):
    """🎯 메인 함수: 프로젝트 분석 + README 자동 생성"""
    print("🚀 Smart README Generator 시작!")
    print("="*50)
    
    # 1단계: 프로젝트 분석
    analysis = analyze_project(project_path)
    
    print(f"\n📊 분석 결과:")
    print(f"  - 전체 함수: {len(analysis['all_functions'])}개")
    print(f"  - 전체 클래스: {len(analysis['all_classes'])}개")
    
    # 2단계: README 생성
    print(f"\n🎨 README 생성 중...")
    generator = SmartReadmeGenerator()
    readme_content = generator.generate_readme(analysis)
    
    # 3단계: 파일 저장
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    print("✅ README.md 파일이 생성되었습니다!")
    print("="*50)
    
    return readme_content

if __name__ == "__main__":
    # 현재 폴더의 프로젝트를 분석하고 README 자동 생성
    generate_readme_for_project(".")
    print("\n🎉 완료! README.md 파일을 확인하세요!")