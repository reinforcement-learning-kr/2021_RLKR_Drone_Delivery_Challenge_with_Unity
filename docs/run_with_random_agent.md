# 랜덤 에이전트 코드

#### ➡️ Index

- []()
- []()

더 자세한 내용은 ML-Agents 깃허브의 [Python-API](https://github.com/Unity-Technologies/ml-agents/blob/main/docs/Python-API.md) 내용을 참고해주세요!

### 라이브러리 불러오기

```python
from mlagents_envs.environment import UnityEnvironment, ActionTuple
from mlagents_envs.side_channel.engine_configuration_channel import EngineConfigurationChannel

import numpy as np 
```

- UnityEnvironment: 유니티 환경과 코드 사이를 연결해주는 메인 인터페이스로 이를 통해 코드가 환경의 정보를 받으며 행동 정보를 환경에게 전송 
- ActionTuple: numpy array를 유니티에 전송하기 위한  ActionTuple로 변환하기 위해 사용 



### 환경 정보 

드론 환경에 대한 더 자세한 정보를 본 깃허브의 [문서](https://github.com/reinforcement-learning-kr/2021_RLKR_Drone_Delivery_Challenge_with_Unity/blob/master/docs/rl_village_info.md)를 참고해주세요!

- 관측 (Observation): 7개의 관측 데이터 
  - 벡터 관측, 정면 이미지, 오른쪽 이미지, 뒤쪽 이미지, 왼쪽 이미지, 측면 raycast, 아래쪽 raycast
- 행동 (Action): 3개의 연속적인 행동 벡터 (범위: -1 ~ 1)



### 환경 정의 및 설정

```python
if __name__ == '__main__':
    # 환경 정의 및 설정 
    engine_configuration_channel = EngineConfigurationChannel()
    env = UnityEnvironment(file_name='환경의 경로', 
                           worker_id=np.random.randint(65535),
                           side_channels=[engine_configuration_channel])
    env.reset()
```

- EngineConfigurationChannel: 환경에 대한 타임 스케일, 해상도, 그래픽 품질 등에 대한 변경 가능 

- UnityEnvironment를 통해 환경 정의 
  - file_name: 환경의 경로 입력
  - worker_id: 환경과 통신하기 위한 포트 -> 여러 환경을 사용하는 경우 값을 다르게 설정해야함 
  - side_channels: 강화학습 루프와 상관없는 데이터를 환경과 주고받기 위한 방법을 제공 
- env.reset(): 환경을 초기화  



### Behavior 이름 불러오기 및 timescale 설정 

```python
    # behavior 이름 불러오기 및 timescale 설정
    behavior_name = list(env.behavior_specs)[0]
    engine_configuration_channel.set_configuration_parameters(time_scale=10)
```

- engine_configuration_channel의  set_configuration_parameters를 통해 time_scale을 10으로 설정 (10프레임 마다 한번씩 화면 업데이트)



### 전체 진행을 위한 반복문

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

- get_steps: decision step과 terminal step을 tuple로 반환
  - decision step: 환경을 에피소드가 진행중인 경우 에이전트에 대한 정보를 포함
  - terminal step: 환경의 에피소드가 종료된 경우 에이전트에 대한 정보를 포함 



### 에피소드 진행을 위한 while문

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

- Random 행동 설정: 행동의 수 = 3
  - ActionTuple을 이용하여 random action을 변환 -> action_tuple.add_continuous(random_action)
- 행동 수행 -> env.step() 
- 에피소드가 종료되는 경우 (done=True)인 경우 terminal step의 정보를, 에피소드를 진행중인 경우 (done=False) decision_step의 정보를 취득



### 누적보상 출력 및 환경 종료

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

