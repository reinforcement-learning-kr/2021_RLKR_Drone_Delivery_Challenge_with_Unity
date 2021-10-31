# Python API를 사용하여 예제 알고리즘 (DQN, A2C)로 학습하기

> 기본적으로 제공하는 DQN, A2C Baseline Code 실행을 위한 가이드 페이지 입니다.
> python API로 제출할 경우 Baseline으로 제공하는 경로들을 따라 주시기 바랍니다.

## Baseline code 다운로드.
- 먼저, 대회 깃허브 페이지에서 Baseline Code들을 경로에 맞게 다운로드 해주시기 바랍니다.
  - [Baseline Code](https://github.com/reinforcement-learning-kr/2021_RLKR_Drone_Delivery_Challenge_with_Unity/tree/master/baseline)를 참고해주세요 !

## Directory 설명.
```bash
├─code
│  ├─best_model
│  └─__pycache__
└─RL_Drone
    ├─DroneDelivery_Data
    │  ├─Managed
    │  ├─ML-Agents
    │  │  └─Timers
    │  ├─Plugins
    │  │  └─x86_64
    │  ├─Resources
    │  └─StreamingAssets
    │      └─Inference_Data
    └─MonoBleedingEdge
        ├─EmbedRuntime
        └─etc
            └─mono
                ├─2.0
                │  └─Browsers
                ├─4.0
                │  └─Browsers
                ├─4.5
                │  └─Browsers
                └─mconfig
```
- 크게 2가지 폴더로 나누어져 있습니다.
  - code: python script와 model 관리를 위한 파일과 폴더가 있습니다.
  - RL_Drone: 환경과 관련된 유니티 파일과 폴더가 있습니다. 다운로드 받은 환경 zip파일을 RL_Drone 폴더에 압축해제 하시기 바랍니다.
### code 폴더.
```bash
└─code
  │  Agent_a2c.py
  │  Agent_dqn.py
  │  Agent_user.py
  │  Drone_gym.py
  │  inference.py
  │
  └─best_model
        best_model.pkl
```
- Agent_a2c.py: a2c 알고리즘 기반 python script 입니다.
- Agent_dqn.py: dqn 알고리즘 기반 python script 입니다.
- Agent_user.py: Agent Class의 기본 형태를 가지고 있는 python script 입니다.
- Drone_gym.py: 원활한 대회 진행을 위해 OpenAI gym 스타일로 변환된 Drone gym 입니다.
- inference.py: 서버에서 진행되는 evaluation 진행 예시 입니다.
- best_model: model이 저장되는 경로 입니다.

### RL_Drone 폴더.
```bash
─RL_Drone
    │  DroneDelivery.exe
    │  UnityCrashHandler64.exe
    │  UnityPlayer.dll
    │
    ├─DroneDelivery_Data
    │  ...
    │
    └─MonoBleedingEdge
        │ ...
        └─ ...
```

## Baseline Code 실행.
```bash
cd code
python Agent_a2c.py
python Agent_dqn.py
```
