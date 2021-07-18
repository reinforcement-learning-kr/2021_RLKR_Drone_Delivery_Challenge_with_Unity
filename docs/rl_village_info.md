#### ➡️ Index
- [State]()
    - [Vector Observation]()
    - [Visual Observation]()
    - [Raycast]()
- [Action]()
- [Reward]()
    - [Event Reward]()
    - [Distance Reward]()
- [Done]()

---

# RL Village Infomation
챌린지의 환경인 RL Village MDP에 대해 소개합니다. 

## State

## Vector Observation (size == 16)

- 배송할 집의 택배 배달 위치의 좌표 (x, y, z)
    - 배송 상황(짐을 상차한)이 아니면 0, 0, 0
- agent의 좌표 (x, y, z)
- agent의 velocity (x, y, z)
- agent의 angularVelocity (x, y, z)
- 창고의 좌표 (x, y, z)
    - 배송 상황(짐을 상차한)이면 0, 0, 0
- 진행률 (%)
    
## Visual Observation

![vis_obs_overview](../images/vis_obs_overview.png)

- 정면 카메라 (64, 36, 3)

    ![vis_obs_front](../images/vis_obs_front.png)

- 우측 카메라 (64, 36, 3)

    ![vis_obs_right](../images/vis_obs_right.png)

- 후면 카메라 (64, 36, 3)

    ![vis_obs_back](../images/vis_obs_back.png)

- 좌측 카메라 (64, 36, 3)

    ![vis_obs_left](../images/vis_obs_left.png)

## Raycast (size == 26)

- 30도씩 12 방향

    ![raycast](../images/raycast.png)

## Action

![action](../images/action.png)

- x 방향 이동 (앞, 뒤) : -1 ~ 1 사이의 연속적인 값
- z 방향 이동 (좌, 우) : -1 ~ 1 사이의 연속적인 값
- y 방향 이동 (위, 아래) : -1 ~ 1 사이의 연속적인 값

## Reward

### Event reward 
- + 100
    - 창고 위치에 도달했을때
    - 물품 배송이 완료 되었을때
- - 100
    - 건물 혹은 장애물(ex, 새, 자동차, 가로등, 지면등)에 부딪혔을 때
    - 맵 밖으로 멀리 이동 했을때

### Distance Reward

목표 지점과 거리에 따른 보상

![distance_reward](../images/distance_reward.png)

- 현재 Step에서 목표지점과 거리(curDistance) - 이전 Step에서 목표지점과 거리(preDistance)


## Done

- 건물 혹은 장애물(ex, 새, 자동차, 가로등, 지면등)에 부딪혔을 때
- 맵 밖으로 멀리 이동 했을때
- 배송 물품을 모두 배달 완료 되었을때