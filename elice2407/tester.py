import os
import subprocess
import filecmp
import sys

code=sys.argv[1]

def count_input_files():
    input_files = [filename for filename in os.listdir() if filename.startswith('input') and filename.endswith('.txt')]
    return len(input_files)

def run_test(input_file, output_file):
    # 파일 경로 설정
    global code
    # code_file = 'code.py'
    code_file = code
    input_path = os.path.join(input_file)
    output_path = os.path.join(output_file)

    # code.py 실행하여 출력 받기
    with open(input_path, 'r') as f:
        input_data = f.read().strip()

    try:
        # code.py 실행하고 결과 받기 (1초 timeout 설정)
        result = subprocess.run(['python', code_file], input=input_data, text=True, capture_output=True, timeout=1)
        output_data = result.stdout.strip()

        # 예상 출력 파일 읽기
        with open(output_path, 'r') as f:
            expected_output = f.read().strip()

        # 출력이 예상 출력과 일치하는지 확인
        if output_data == expected_output:
            print(f'Test case {input_file} passed.')
        else:
            print(f'Test case {input_file} failed.')

    except subprocess.TimeoutExpired:
        print(f'Timeout occurred while running test case {input_file}.')
    except Exception as e:
        print(f'Error occurred while running test case {input_file}: {e}')

def main():
    num_test_cases = count_input_files()

    for i in range(1, num_test_cases + 1):
        input_file = f'input{i}.txt'
        output_file = f'output{i}.txt'
        run_test(input_file, output_file)

if __name__ == '__main__':
    main()

