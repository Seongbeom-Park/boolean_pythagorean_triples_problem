# Boolean Pythagorean Triples Problem
[![엄청 신기함.. ㄷㄷ 딱 7824까지 되고, 7825부터 안된다.](https://img.youtube.com/vi/X3dItaE1N3g/0.jpg)](https://www.youtube.com/watch?v=X3dItaE1N3g)

## Simple Dynamic Programming
정수 `n-1`까지 사용하여 성립하는 모든 정수 집합의 조합을 `notes`에 저장
정수 `n`을 추가할 수 있는 집합이 있는지 확인

```bash
time python3 src/simple_dp.py 30
number: 2 len(notes): 1
number: 3 len(notes): 2
number: 4 len(notes): 4
number: 5 len(notes): 8
number: 6 len(notes): 12
number: 7 len(notes): 24
number: 8 len(notes): 48
number: 9 len(notes): 96
number: 10 len(notes): 192
number: 11 len(notes): 288
number: 12 len(notes): 576
number: 13 len(notes): 1152
number: 14 len(notes): 1728
number: 15 len(notes): 3456
number: 16 len(notes): 5184
number: 17 len(notes): 10368
number: 18 len(notes): 15552
number: 19 len(notes): 31104
number: 20 len(notes): 62208
number: 21 len(notes): 93312
number: 22 len(notes): 186624
number: 23 len(notes): 373248
number: 24 len(notes): 746496
number: 25 len(notes): 1492992
number: 26 len(notes): 1617408
number: 27 len(notes): 2437632
number: 28 len(notes): 4875264
number: 29 len(notes): 9750528
number: 30 len(notes): 14625792

real    4m13.128s
user    3m59.145s
sys     0m13.959s
```

## Graph
TODO: `notes`에서 `n`을 추가할 수 없는 트리를 모두 삭제
