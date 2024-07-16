import os
import subprocess
import filecmp
import sys
import pdb

def run_test(input, output):
    # 파일 경로 설정
    code_file = 'elice7.py'
    try:
        # code.py 실행하고 결과 받기 (1초 timeout 설정)
        result = subprocess.run(['python', code_file], input=input, text=True, capture_output=True, timeout=1)
        output_data = result.stdout.strip()

        # 출력이 예상 출력과 일치하는지 확인
        if output_data == output:
            print(f'Test case {input} -> {output} passed.')
        else:
            print(f'Test case {input} -> {output} failed. Expected {output} but got {output_data}.')
            pdb.set_trace()

    except subprocess.TimeoutExpired:
        print(f'Timeout occurred while running test case {input} -> {output}.')
    except Exception as e:
        print(f'Error occurred while running test case {input} -> {output}: {e}')

def main():
    with open("all_cases.txt", "r") as f:
        for line in f:
            input, output = line.split("->")
            run_test(input.strip(), output.strip())

if __name__ == '__main__':
    main()

