- elice5.py -> 시간초과 88/100
  
- elice5_v2.py
  - list slice를 촘촘하게 해서 loop를 덜 돌게 설계
  - ss 루프에 check_list로 continue가 아닌 `ss_t=ss[idx:]` 로 slicing
  - 더 느려짐... ~~(역시 파이썬은)~~
  
- 심지어 gen으로 생성한 15개 짜리(심지어는 10개 짜리)가 죽는다
  - o_loc을 못 찾음 `ss[i:].index(s+a)`
  
- 더 줄일 방법은 모르겠고... 혹시나 해서 그냥 똑같이 제출 -> 100/100
  - ?? -> pass