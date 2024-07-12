# import pdb

a = list(map(int,input().split()))

all_case = []
for i in range(len(a)):
  if i == 0:
    all_case.append('0')
    all_case.append('1')
  else:
    next_case = []
    for c in all_case:
      next_case.append(c+'0')
      next_case.append(c+'1')
    all_case = next_case

sums = []
for case in all_case:
  isum = 0
  for i, c in enumerate(case):
    if c == '1':
      isum += a[i]
  sums.append(isum)

sums.sort()
print(sums, f"-> {len(sums)}")
