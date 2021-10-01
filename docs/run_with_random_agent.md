#### ➡️ Index

- [라이브러리 불러오기]()
- [랜덤 에이전트가 이용한 환경 정보 ]()
- [환경 정의 및 설정]()
- [Behavior 이름 불러오기 및 timescale 설정]()
- [전체 진행을 위한 Loop]()
- [에피소드 진행을 위한 Loop]()
- [누적보상 출력 및 환경 종료]()
- [전체 코드]()
- [Reference]()
---

# Python API를 사용하여 랜덤 에이전트로 실행하기

더 자세한 내용은 ML-Agents 깃허브의  내용을 참고해주세요!

## 라이브러리 불러오기
### Code
```python
from mlagents_envs.environment import UnityEnvironment, ActionTuple
from mlagents_envs.side_channel.engine_configuration_channel import EngineConfigurationChannel

import numpy as np 
```
### Description
- `UnityEnvironment`: Unity 환경과 Python Code를 연결해주는 메인 인터페이스로, 이를 통해 Python 코드가 Unity 환경의 정보를 받으며 Agent의 Action 정보를 Unity 환경에게 전송 
- `ActionTuple`: numpy array를 Unity에 전송하기 위해 ActionTuple로 변환해서 사용 


## 랜덤 에이전트가 이용한 환경 정보 

> 챌린지 환경인 RL Village에 대한 더 자세한 정보는 본 Github repository에 있는 [RL Village Infomation](https://github.com/reinforcement-learning-kr/2021_RLKR_Drone_Delivery_Challenge_with_Unity/blob/master/docs/rl_village_info.md)를 참고해주세요!

- Observation: 7개의 관측 데이터 
  1. 벡터 관측
  2. 정면 이미지
  3. 오른쪽 이미지
  4. 뒤쪽 이미지
  5. 왼쪽 이미지
  6. 측면 raycast
  7. 아래쪽 raycast
- Action: 3개의 continuous 벡터 (range: -1 ~ 1 float)

## 환경 정의 및 설정
### Code
```python
if __name__ == '__main__':
    # 환경 정의 및 설정 
    engine_configuration_channel = EngineConfigurationChannel()
    env = UnityEnvironment(file_name='환경의 경로', 
                           worker_id=np.random.randint(65535),
                           side_channels=[engine_configuration_channel])
    env.reset()
```
### Description
- `EngineConfigurationChannel`: 환경에 대한 타임 스케일, 해상도, 그래픽 품질 등에 대한 변경 가능 
- UnityEnvironment를 통해 환경 정의 
  - `file_name`: 환경의 경로 입력
  - `worker_id`: 환경과 통신하기 위한 포트 -> 여러 환경을 사용하는 경우 값을 다르게 설정해야함 
  - `side_channels`: 강화학습 루프와 상관없는 데이터를 환경과 주고받기 위한 방법을 제공 
- `env.reset()`: 환경을 초기화  

## Behavior 이름 불러오기 및 timescale 설정 
### Code
```python
    # behavior 이름 불러오기 및 timescale 설정
    behavior_name = list(env.behavior_specs)[0]
    engine_configuration_channel.set_configuration_parameters(time_scale=10)
```
### Description
- `engine_configuration_channel`의  `set_configuration_parameters`를 통해 `time_scale`을 10으로 설정 (10프레임 마다 한 번씩 화면 업데이트)


## 전체 진행을 위한 Loop
### Code
```python
    # 전체 진행을 위한 반복문 (10 에피소드 반복)
    for ep in range(10):
        # 환경 초기화 
        env.reset()

        # decision_steps와 terminal_steps 정의
        decision_steps, terminal_steps = env.get_steps(behavior_name)

        # 파라미터 초기화 
        done = False
        ep_rewards = 0
```
### Description
- `get_steps`: `decision_step`과 `terminal_step`을 tuple로 반환
  - `decision_step`: 환경을 에피소드가 진행중인 경우 에이전트에 대한 정보를 포함
  - `terminal_step`: 환경의 에피소드가 종료된 경우 에이전트에 대한 정보를 포함 


### 에피소드 진행을 위한 Loop
### Code
```python
        # 에피소드 진행을 위한 while문 
        while not done:
            # 랜덤 행동 설정
            random_action = np.random.randn(len(decision_steps),3)

            action_tuple = ActionTuple()
            action_tuple.add_continuous(random_action)

            env.set_actions(behavior_name, action_tuple)

            # 행동 수행 
            env.step()

            # 행동 수행 후 에이전트의 정보 (상태, 보상, 종료 여부) 취득
            decision_steps, terminal_steps = env.get_steps(behavior_name)
            
            done = len(terminal_steps.agent_id)>0
            reward = terminal_steps.reward[0] if done else decision_steps.reward[0]

            if done:
                next_state = [terminal_steps.obs[i][0] for i in range(7)]
            else:
                next_state = [decision_steps.obs[i][0] for i in range(7)]

            # 매 스텝 보상을 에피소드에 대한 누적보상에 더해줌 
            ep_rewards += reward 
```
### Description
- Random Action 설정: Action 수 = 3
  - `action_tuple.add_continuous(random_action)`: `ActionTupl`e을 이용하여 `random_action`을 변환
- `env.step()`: 1번의 Action 실행
- 에피소드가 종료된 (`done=True`)인 경우 `terminal_steps`의 정보를, 에피소드를 진행중인 경우 (`done=False`) `decision_step`의 정보를 취득


### 누적보상 출력 및 환경 종료
### Code
```python
        # 누적 보상 출력
        print('total reward for ep {} is {}'.format(ep, ep_rewards))

    # 환경 종료 
    env.close() 
```


### 전체 코드 

```python
from mlagents_envs.environment import UnityEnvironment, ActionTuple
from mlagents_envs.side_channel.engine_configuration_channel import EngineConfigurationChannel

import numpy as np 

if __name__ == '__main__':
    # 환경 정의 및 설정 
    engine_configuration_channel = EngineConfigurationChannel()
    env = UnityEnvironment(file_name='환경의 경로', 
                           worker_id=np.random.randint(65535),
                           side_channels=[engine_configuration_channel])
    env.reset()

    # behavior 이름 불러오기 및 timescale 설정
    behavior_name = list(env.behavior_specs)[0]
    engine_configuration_channel.set_configuration_parameters(time_scale=10)

    # 전체 진행을 위한 반복문 (10 에피소드 반복)
    for ep in range(10):
        # 환경 초기화 
        env.reset()

        # decision_steps와 terminal_steps 정의
        decision_steps, terminal_steps = env.get_steps(behavior_name)

        # 파라미터 초기화 
        done = False
        ep_rewards = 0

        # 에피소드 진행을 위한 while문 
        while not done:
            # 랜덤 행동 설정
            random_action = np.random.randn(len(decision_steps),3)

            action_tuple = ActionTuple()
            action_tuple.add_continuous(random_action)

            env.set_actions(behavior_name, action_tuple)

            # 행동 수행 
            env.step()

            # 행동 수행 후 에이전트의 정보 (상태, 보상, 종료 여부) 취득
            decision_steps, terminal_steps = env.get_steps(behavior_name)
            
            done = len(terminal_steps.agent_id)>0
            reward = terminal_steps.reward[0] if done else decision_steps.reward[0]

            if done:
                next_state = [terminal_steps.obs[i][0] for i in range(7)]
            else:
                next_state = [decision_steps.obs[i][0] for i in range(7)]

            # 매 스텝 보상을 에피소드에 대한 누적보상에 더해줌 
            ep_rewards += reward 
        
        # 누적 보상 출력
        print('total reward for ep {} is {}'.format(ep, ep_rewards))

    # 환경 종료 
    env.close() 
```

### Reference
- [ml-agents Python-API](https://github.com/Unity-Technologies/ml-agents/blob/main/docs/Python-API.md)
- [RL Village Infomation](https://github.com/reinforcement-learning-kr/2021_RLKR_Drone_Delivery_Challenge_with_Unity/blob/master/docs/rl_village_info.md)
