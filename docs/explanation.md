#### ➡️ Index


---

# Challenge Explanation

본 챌린지는 강화학습 알고리즘으로 드론이 물류창고의 물품들을 배송지인 집으로 빠르고 안전하게 배송하도록 학습시키는 것이 목표입니다.

## How to play

1. 에피소드가 시작되면 Drone이 Warehouse에서 해당 Episode에서 배송할 3개 Package들을 모두 싣게 됩니다.

![](../images/play1.png)

2. 각 Package는 배달 될 미션지인 House가 있고 이는 10개 집들 중 랜덤으로 3개가 선정된다. 따라서 총 3개의 집으로 Drone Agent가 도착해야 한다. 

![](../images/play2.png)

3. RL Village에 있는 장애물(새, 건물 등)을 파악하며 선회하여 주행할 수 있어야 한다.

![](../images/play3.png)

4. 모든 3개의 집들에 배달을 완료하면 에피소드 Completed!

![](../images/play4.png)

## Metric