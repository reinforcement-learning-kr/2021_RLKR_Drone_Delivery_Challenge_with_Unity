[TOC]


# Contents
- [Ml-agents 2.0 설치하기]()
- [RL Village build 파일 열기]()
- [Config 파일 작성하기]()
- [Training 하기]()
- [Tensorboard로 학습과정 확인하기]()
- [학습된 onnx file로 inference하기]()
- [Reference]()

# Ml-agents 2.0 설치하기
1. 공식 Github 페이지에서 Download를 해줍니다. test[^test]

2. conda에 가상환경을 하나 만듭니다. conda create -n [name]
3. ml-agents를 다운 받은 파일을 열어서
4. CLI 창에 mlagents-learn ==--help==를 입력했을 때, 아래와 같은 

# RL Village build 파일 열기

# Config 파일 작성하기

ml-agents에서 제공하는 기본 알고리즘에는 ppo, sac, poca가 있습니다. 이중 poca 옵션은 multi-agent를 위한 알고리즘이므로 본 대회에서는 ppo 혹은 sac 옵션을 사용하실 수 있습니다. ml-agents에서 제공하는 알고리즘을 사용하기 위해 original RL paper를 읽어보시는 것을 권장합니다. 알고리즘들의 파라미터를 수정할 수 있는 Config를 작성하기 위해 어느정도의 이해가 필요합니다.
- ppo: https://arxiv.org/abs/1707.06347
- sac: https://arxiv.org/abs/1812.05905

# Training 하기

Command
```
usage: mlagents-learn.exe [-h] [--env ENV_PATH] [--resume] [--force] [--run-id RUN_ID] [--initialize-from RUN_ID]
                          [--seed SEED] [--inference] [--base-port BASE_PORT] [--num-envs NUM_ENVS] [--debug]
                          [--env-args ...] [--torch] [--tensorflow] [--results-dir RESULTS_DIR] [--width WIDTH]
                          [--height HEIGHT] [--quality-level QUALITY_LEVEL] [--time-scale TIME_SCALE]
                          [--target-frame-rate TARGET_FRAME_RATE] [--capture-frame-rate CAPTURE_FRAME_RATE]
                          [--no-graphics] [--torch-device DEVICE]
                          [trainer_config_path]
s
```

# Tensorboard로 학습과정 확인하기

tensorboard --logdir results

# 학습된 onnx file로 inference하기

```
mlagents-learn --env=C:\Users\Jungyeon\Desktop\droneHackaton\windows --resume --run-id=test --inference --width 500 --height 250 
```

# Reference

- [Unity Technologies Blog ML-Agents v2.0 release: Now supports training complex cooperative behaviors](https://blog.unity.com/technology/ml-agents-v20-release-now-supports-training-complex-cooperative-behaviors)<sup>1<sup/>
- 
- []()
- []()
- []()

---
[^test]: [https://github.com/Unity-Technologies/ml-agents](https://github.com/Unity-Technologies/ml-agents)