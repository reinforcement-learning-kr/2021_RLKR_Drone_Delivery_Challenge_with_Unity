#### ➡️ Index
- Goal
- Senario
- Evaluation
    - 평가 항목 우선순위
    - Test Environment
    - Leaderboard
---

# Challenge Explanation

## Goal

본 챌린지에서는 강화학습 알고리즘으로 드론이 물류창고의 물품들을 집으로 빠르고 안전하게 배송하도록 학습시키는 것이 목표입니다.

---

## Senario

1. 에피소드가 시작되면 Drone이 Warehouse에서 해당 Episode에서 배송할 3개 Package들을 모두 싣게 됩니다.

![](../images/play1.png)

2. 각 Package는 배달 될 House가 있고 이는 [10개 집들](https://github.com/curieuxjy/2021_RLKR_Drone_Delivery_Challenge_with_Unity/blob/master/docs/rl_village_info.md#-rl-village-%EC%86%8C%EA%B0%9C-%EB%B0%8F-%EA%B5%AC%EC%84%B1) 중 랜덤으로 3개가 선정된다. 따라서 총 3개의 집으로 Drone Agent가 도착해야 합니다. 

![](../images/play2.png)

3. RL Village에 있는 모든 장애물(새, 건물 등)을 State 정보를 활용하여 파악하며 선회하여 주행할 수 있어야 합니다.

![](../images/play3.png)

4. 모든 3개의 집들에 배달을 완료하면 에피소드 Mission Completed! 입니다.

![](../images/play4.png)

---

## Evaluation

Submission된 모델들을 평가하는 방식에 대해서 설명합니다. 평가방식은 평가항목별 우선순위가 존재하며 우선순위부터 비교하며 순위가 정해집니다.

### 평가 항목 우선순위
1. 배달 완료 수
2. 소요 시간

### Test Environment

배달할 집들이 서로 다른 에피소드 10개가 Test Environment가 되며, 예시 Test Environment의 예시는 다음과 같습니다.

```
- test no.1 : 1,3,4 집 배달
- test no.2 : 3,7,8 집 배달
- ...
- test no.10 : 3,6,9 집 배달
```

### Leaderboard

리더보드는 Submission된 모델들을 평가한 후 순위가 매겨지고 리더보는 구성은 다음과 같습니다.

- `순위`
- `팀명`
- `배달 완료수`: Test Envionment에서 배달 완료한 수
- `소요 시간`: Test Envionment개에서  
- `Raw Score`: Test Envionment 10개에서 
- `상세정보`: `보기`를 누르면 Test Envrionment 10개 각각에서의 제출된 모델의 퍼포먼스를 볼 수 있음

```
상세정보의 세부 항목
```

#### 리더보드의 각 항목 순위 산출 방식
- `배달 완료수`: Test Envionment 10개에서 배달 완료한 수의 총합
- `소요 시간`: