#### ➡️ Index
- [Config 파일 작성하기]()
- [Training 하기]()
- [Tensorboard로 학습과정 확인하기]()
- [학습된 onnx file로 inference하기]()
- [Reference]()

---
RL Village 빌드파일을 다운로드한 후 ml-agents 2.0에서 제공하는 알고리즘으로 학습하기

# Config 파일 작성하기

ml-agents에서 제공하는 기본 알고리즘에는 `ppo`, `sac`, `poca`가 있습니다. 이중 `poca` 옵션은 multi-agent를 위한 알고리즘이므로 본 대회에서는 `ppo` 혹은 `sac` 옵션을 사용하실 수 있습니다. ml-agents에서 제공하는 알고리즘을 사용하기 위해 original RL paper를 읽어보시는 것을 권장합니다. 알고리즘들의 파라미터를 수정할 수 있는 Config를 작성하기 위해 어느정도의 이해가 필요합니다.
- ppo: https://arxiv.org/abs/1707.06347
- sac: https://arxiv.org/abs/1812.05905

## Config example
- ppo
    ```
    behaviors:
      My Behavior: 
        trainer_type: ppo
        hyperparameters:
          batch_size: 64
          buffer_size: 256
          learning_rate: 0.0003
          learning_rate_schedule: linear
    
          beta: 0.005
          epsilon: 0.2
          lambd: 0.95
          num_epoch: 3



        network_settings:
          vis_encode_type: simple
          normalize: true
          hidden_units: 128
          num_layers: 2
    
          memory:
            sequence_length: 64
            memory_size: 256
    
        max_steps: 500000
        time_horizon: 1000
        summary_freq: 12000
        keep_checkpoints: 5
        checkpoint_interval: 50000
        threaded: false
        init_path: null
    
        reward_signals:
          extrinsic:
            gamma: 0.99
            strength: 1.0
    ```

# Training 

### Command

```
usage: mlagents-learn [-h] [--env ENV_PATH] [--resume] [--force] [--run-id RUN_ID] [--initialize-from RUN_ID]
                          [--seed SEED] [--inference] [--base-port BASE_PORT] [--num-envs NUM_ENVS] [--debug]
                          [--env-args ...] [--torch] [--tensorflow] [--results-dir RESULTS_DIR] [--width WIDTH]
                          [--height HEIGHT] [--quality-level QUALITY_LEVEL] [--time-scale TIME_SCALE]
                          [--target-frame-rate TARGET_FRAME_RATE] [--capture-frame-rate CAPTURE_FRAME_RATE]
                          [--no-graphics] [--torch-device DEVICE]
                          [trainer_config_path]
```

### 기본 Commmand

```
mlagents-learn [Trainer_Path] --env=[Env_path] --run_id=[run_id]
```

- Trainer_Path: 학습 알고리즘 설정 YAML 파일이 위치한 경로 (default: ml-agent/config/)
- Env_Path: 학습을 실행시킬 환경의 빌드 파일이 위치한 경로
- Run_Id: 학습된 모델이 저장될 폴더의 이름

### 기본 Command 예시

(프롬프트 경로는 깃허브에서 받은 mlagents 폴더)

```
mlagents-learn config\ppo\3DBall --env=..\DroneDilivery\DroneDilivery --run-id=drone1
```

# Tensorboard로 학습과정 확인하기

프롬프트 상에서 다음의 명령어 입력

```
tensorboard --logdir results
```

# 학습된 onnx file로 inference하기

```
mlagents-learn --env=C:\Users\Jungyeon\Desktop\droneHackaton\windows --resume --run-id=test --inference --width 500 --height 250 
```

# Reference
- [1] [Training Configurations](https://github.com/Unity-Technologies/ml-agents/blob/main/docs/Training-ML-Agents.md#training-configurations) 
- [2] [Training Configuration File](https://github.com/Unity-Technologies/ml-agents/blob/main/docs/Training-Configuration-File.md)
