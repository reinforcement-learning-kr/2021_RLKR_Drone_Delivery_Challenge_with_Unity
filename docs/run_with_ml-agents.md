#### ➡️ Index
- [Config 파일 작성하기](https://github.com/reinforcement-learning-kr/rlkorea_drone_challenge/blob/master/docs/run_with_ml-agents.md#config-%ED%8C%8C%EC%9D%BC-%EC%9E%91%EC%84%B1%ED%95%98%EA%B8%B0)
    - [Behavior Config](https://github.com/reinforcement-learning-kr/rlkorea_drone_challenge/blob/master/docs/run_with_ml-agents.md#behavior-config)
    - [Reward Signals](https://github.com/reinforcement-learning-kr/rlkorea_drone_challenge/blob/master/docs/run_with_ml-agents.md#reward-signals)
- [Training](https://github.com/reinforcement-learning-kr/rlkorea_drone_challenge/blob/master/docs/run_with_ml-agents.md#training)
    - [기본 Command](https://github.com/reinforcement-learning-kr/rlkorea_drone_challenge/blob/master/docs/run_with_ml-agents.md#%EA%B8%B0%EB%B3%B8-commmand)
    - [기본 Command 예시](https://github.com/reinforcement-learning-kr/rlkorea_drone_challenge/blob/master/docs/run_with_ml-agents.md#%EA%B8%B0%EB%B3%B8-command-%EC%98%88%EC%8B%9C)
    - [주요 Command option table](https://github.com/reinforcement-learning-kr/rlkorea_drone_challenge/blob/master/docs/run_with_ml-agents.md#%EC%A3%BC%EC%9A%94-command-option-table)
- [Tensorboard로 학습과정 확인하기](https://github.com/reinforcement-learning-kr/rlkorea_drone_challenge/blob/master/docs/run_with_ml-agents.md#tensorboard%EB%A1%9C-%ED%95%99%EC%8A%B5%EA%B3%BC%EC%A0%95-%ED%99%95%EC%9D%B8%ED%95%98%EA%B8%B0)
- [학습된 onnx file로 inference하기](https://github.com/reinforcement-learning-kr/rlkorea_drone_challenge/blob/master/docs/run_with_ml-agents.md#%ED%95%99%EC%8A%B5%EB%90%9C-onnx-file%EB%A1%9C-inference%ED%95%98%EA%B8%B0)
- [Reference](https://github.com/reinforcement-learning-kr/rlkorea_drone_challenge/blob/master/docs/run_with_ml-agents.md#reference)

---
RL Village 빌드파일을 다운로드한 후 ml-agents 2.0에서 제공하는 알고리즘으로 학습하기

# Config 파일 작성하기

ml-agents에서 제공하는 기본 알고리즘에는 `ppo`, `sac`, `poca`가 있습니다. 이중 `poca` 옵션은 multi-agent를 위한 알고리즘이므로 본 대회에서는 `ppo` 혹은 `sac` 옵션을 사용하실 수 있습니다. ml-agents에서 제공하는 알고리즘을 사용하기 위해 original RL paper를 읽어보시는 것을 권장합니다. 알고리즘들의 파라미터를 수정할 수 있는 Config를 작성하기 위해 어느정도의 이해가 필요합니다.
- ppo: https://arxiv.org/abs/1707.06347
- sac: https://arxiv.org/abs/1812.05905

## Behavior Config
[Official Behavior Config](https://github.com/Unity-Technologies/ml-agents/blob/main/docs/Training-ML-Agents.md#behavior-configurations)에 자신의 Agent가 실행하는 RL 알고리즘의 파라미터들을 지정할 수 있는 yaml 파일 작성법이 나와있습니다. 앞서 이번 챌린지에서 사용할 수 있는 알고리즘은 ppo, sac가 있음을 알 수 있는데 두 가지 알고리즘 중에 선택한 알고리즘을 `trainer_type`에 작성합니다. config 파일의 `behaviors`의 이름은 **반드시** `My Behavior`라고 적어야 합니다.

```
behaviors:
  My Behavior: 
    trainer_type: ppo
    hyperparameters:
      batch_size: 64
      ...
```

2개의 알고리즘 모두에 해당하는 Config element는 [Common Trainer Configurations](https://github.com/Unity-Technologies/ml-agents/blob/main/docs/Training-Configuration-File.md#common-trainer-configurations)에서 확인하실 수 있습니다.

하지만 ppo인지, sac인지에 따라 각 알고리즘에 해당하는 Config element도 있습니다. ppo에만 있는 configuration은 [PPO-specific Configurations](https://github.com/Unity-Technologies/ml-agents/blob/main/docs/Training-Configuration-File.md#ppo-specific-configurations)을, sac에만 있는 configuration은 [SAC-specific Configurations](https://github.com/Unity-Technologies/ml-agents/blob/main/docs/Training-Configuration-File.md#sac-specific-configurations)을 참고해주세요.

config 파일을 작성하지 않고 실행할 경우 default config(ppo)가 들어가게 됩니다.

## Reward Signals
강화학습에 중요한 Reward 설정 또한 config 파일을 통해 다양하게 시도해볼 수 있습니다. [Reward Signals](https://github.com/Unity-Technologies/ml-agents/blob/main/docs/Training-Configuration-File.md#reward-signals)에 있는 Extrinsic Rewards, Curiosity Intrinsic Reward, GAIL Intrinsic Reward등 다양한 reward design을 해보세요.

> Behavior, Reward 외에도 [Training Configuration File](https://github.com/Unity-Technologies/ml-agents/blob/main/docs/Training-Configuration-File.md#reward-signals)에서 다양한 config element들을 확인하실 수 있습니다.

---
# Training 
`mlagents-learn`을 통해 conda prompt에서 다양한 옵션을 설정하여 Agent를 training할 수 있습니다. 다양한 command option들을 확인하기 위해서 `mlagents-learn --help`를 입력해보세요. 

그러면 다음과 같은 사용할 수 있는 옵션들이 나옵니다.

```
usage: mlagents-learn [-h] [--env ENV_PATH] [--resume] [--force] [--run-id RUN_ID] [--initialize-from RUN_ID]
                          [--seed SEED] [--inference] [--base-port BASE_PORT] [--num-envs NUM_ENVS] [--debug]
                          [--env-args ...] [--torch] [--tensorflow] [--results-dir RESULTS_DIR] [--width WIDTH]
                          [--height HEIGHT] [--quality-level QUALITY_LEVEL] [--time-scale TIME_SCALE]
                          [--target-frame-rate TARGET_FRAME_RATE] [--capture-frame-rate CAPTURE_FRAME_RATE]
                          [--no-graphics] [--torch-device DEVICE]
                          [trainer_config_path]
```

## 기본 Commmand

```
mlagents-learn [Trainer_Config_Path] --env=[Env_Path] --run_id=[run_id]
```

- Trainer_Config_Path: 학습 알고리즘 설정 YAML 파일이 위치한 경로 (default: ml-agent/config/)
- Env_Path: 학습을 실행시킬 환경의 빌드 파일이 위치한 경로. 이번 챌린지에서 배포된 RL Village 파일이 있는 경로.
- Run_Id: 학습된 모델이 저장될 폴더의 이름

## 기본 Command 예시

위의 기본 Command를 바탕으로 예시로 작성된 command는 다음과 같습니다. 이때 command를 실행하는 경로는 챌린지의 github 페이지에서 받은 RL village 환경 파일을 받아 압축을 풀어 놓은 경로라고 가정한 예시입니다. 즉, 아래의 폴더 `~/YourDirectory`가 현재 prompt의 경로 입니다.

```
(Windows build 파일 기준)
YourDirectory
├── RLVillage
│   ├── DroneDelivery.exe
│   ├── DroneDelivery_Data  
│   ├── MonoBleedingEdge  
│   ├── UnityCrashHandle64.exe             
│   └── UnityPlayer.dll
└── drone_config
    └── ppo.yaml
```

위의 상황을 가정했을때 기본 Command 예시는 다음과 같습니다.

```
mlagents-learn ./drone_config/ppo.yaml --env=./RLVillage --run-id=drone1
```

## 주요 Command option table
기본 Command에서 소개한 option들을 제외하고 자주 사용하게 될 몇가지 옵션들은 다음과 같습니다. 이외에 더 자세한 설명은 앞서 설명해드린 `mlagents-learn --help`을 통해 확인하거나 공식 문서 [Starting Training](https://github.com/Unity-Technologies/ml-agents/blob/main/docs/Training-ML-Agents.md#starting-training)을 확인하시는 것을 권장해드립니다.

|option|description|
|-|-|
|`--resume`|Whether to resume training from a checkpoint. Specify a --run-id to use this option. If set, the training code loads an already trained model to initialize the neural network before resuming training. This option is only valid when the models exist, and have the same behavior names as the current agents in your scene. (default: False)|
|`--force`|Whether to force-overwrite this run-id's existing summary and model data. (Without this flag, attempting to train a model with a run-id that has been used before will throw an error.) (default: False)|
|`--inference`|Whether to run in Python inference mode (i.e. no training). Use with --resume to load a model trained with an existing run ID. (default: False)|
|`--num-envs NUM_ENVS`|The number of concurrent Unity environment instances to collect experiences from when training (default: 1)|
|`--width WIDTH`|The width of the executable window of the environment(s) in pixels (ignored for editor training). (default: 84) 저희 챌린지 환경에서는 576으로 설정했을 때 잘 보입니다.|
|`--height HEIGHT`|The height of the executable window of the environment(s) in pixels (ignored for editor training) (default: 84) 저희 챌린지 환경에서는 324으로 설정했을 때 잘 보입니다.|
|`--no-graphics`|Whether to run the Unity executable in no-graphics mode (i.e. without initializing the graphics driver. Use this only if your agents don't use visual observations. (default: False)|


# Tensorboard로 학습과정 확인하기

프롬프트 상에서 다음의 명령어 입력을 입력하여 tensorboard에서 학습 과정을 확인하실 수 있습니다. results 폴더에는 training 시에 설정했던 `run-id`에 해당하는 이름의 폴더로 학습 로그가 저장되어 있습니다.

```
tensorboard --logdir results
```
관련하여 더 자세한 사항은 [Using TensorBoard to Observe Training](https://github.com/Unity-Technologies/ml-agents/blob/main/docs/Using-Tensorboard.md)에서 확인하실 수 있습니다.

# 학습된 onnx file로 inference하기

위에서 학습한 agent는 `.onnx`파일로 저장됩니다. 위에서 training시에 `run-id`를 "RUN-ID"로 설정했다고 했을 때, 이 파일은 `results`→`RUN-ID`→`My Behavior`에서 확인하실 수 있습니다.

```
results
└── RUN-ID
     └── My Behavior
         └── My Behavior-00000.onnx
```

폴더의 구성이 다음과 같다고 가정하고 prompt의 경로가 `~/YourDirectory`라고 한다면, 

```
YourDirectory
├── RLVillage
│   ├── DroneDelivery.exe
│   ├── DroneDelivery_Data  
│   ├── MonoBleedingEdge  
│   ├── UnityCrashHandle64.exe             
│   └── UnityPlayer.dll
└── results
    └── RUN-ID
```

학습한 Agent의 inference 결과를 보기 위해서 다음과 같이 command를 입력합니다.

```
mlagents-learn --env=./RLVillage --resume --run-id=RUN-ID --inference
```

# Reference
- [1] [Training ML-Agents](https://github.com/Unity-Technologies/ml-agents/blob/main/docs/Training-ML-Agents.md)
- [2] [Training Configurations](https://github.com/Unity-Technologies/ml-agents/blob/main/docs/Training-ML-Agents.md#training-configurations) 
- [3] [Training Configuration File](https://github.com/Unity-Technologies/ml-agents/blob/main/docs/Training-Configuration-File.md)
- [4] [Using TensorBoard to Observe Training](https://github.com/Unity-Technologies/ml-agents/blob/main/docs/Using-Tensorboard.md)
