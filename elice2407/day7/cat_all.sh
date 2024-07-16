
#!/bin/bash

# 파일 목록에서 input 파일과 output 파일을 찾기
input_files=$(ls input*.txt | sort -V)
output_files=$(ls output*.txt | sort -V)

# input 파일 개수 확인
num_files=$(echo "$input_files" | wc -l)

# 각 input 파일과 그에 해당하는 output 파일을 순서대로 출력
for (( i=1; i<=$num_files; i++ )); do
    input_file=$(echo "$input_files" | sed -n "${i}p")
    output_file=$(echo "$output_files" | sed -n "${i}p")

    # input 파일 이름 출력
    echo "===${input_file}==="
    # input 파일 내용 출력
    cat "${input_file}"
    cat "${output_file}"
done
