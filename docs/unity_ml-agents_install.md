# ml-agents 2.0 설치하기
[Official Installation docs](https://github.com/Unity-Technologies/ml-agents/blob/release_18_docs/docs/Installation.md)의 설치 가이드를 따라 ml-agents를 설치합니다.

## Unity ML-Agents란
- Unity를 이용한 인공지능 Agent 학습을 지원하는 도구
- 기본적으로 강화학습을 이용한 학습을 지원
- 다양한 학습 방식 지원

## 설치 전 참고사항

ML-Agents는 다음과 같이 유니티와 파이썬에 따로 설치를 할 수 있습니다. 

- 유니티를 통해 *강화학습 환경을 제작하기 위해* 유니티에서 package의 형태로 설치
- Python에서 *ML-Agents 관련 내용을 사용하기 위해* 파이썬에 라이브러리로 설치 

본 챌린지의 경우 참가자분들이 *Unity를 통해 환경을 수정하실 필요는 없기 때문에* 유니티에 대한 설치를 따로 진행하지 않으셔도 괜찮습니다. 

**따라서 아래의 설치 방법을 따라 설치하실 때에 `1.`의 유니티의 설치는 진행하지 않으셔도 괜찮습니다.([OPTIONAL])**


## 설치 방법

1. Unity ML-Agents를 설치하기전, Unity(with Unity Hub)와 Python version은 아래와 같은 조건을 만족하는지 확인합니다. 

    - *[OPTIONAL]* [Unity](https://unity3d.com/get-unity/download) (2019.4 or later)

    - [Python](https://www.python.org/downloads/) (3.6.1 or higher)
    
    - (For Windows) [Pytorch](https://pytorch.org/get-started/locally/) 설치 필요

2. 공식 Unity ML-Agents Github 페이지에서 [Releases & Documentation](https://github.com/Unity-Technologies/ml-agents#releases--documentation)에서 `Release 18`를 Download를 해줍니다.<sub>(2021.07.14기준)<sub/>
    - 주의: 드라이브를 분할해서 사용하시는 경우 Anaconda가 설치된 동일한 드라이브에 파일을 다운로드 해주세요.

3. Challenge에서 사용할 가상환경을 Anaconda로 하나 만들어 줍니다.

    `conda create -n [new_virtual_env]`

4. 해당 가상환경을 activate 한 후에 (2)에서 ml-agents를 다운 받은 경로로 이동합니다.

    `cd [directory of ml-agents file]`
    

5. `pip install -e ml-agents`와 `pip install -e ml-agents-envs`를 입력하여 설치합니다.

6. Prompt 창에 mlagents-learn `--help`를 입력했을 때, 아래와 같은 message가 prompt 창에 뜬다면 설치 성공한 것 입니다.

    ```
        usage: mlagents-learn [-h] [--env ENV_PATH] [--resume] [--force]
                          [--run-id RUN_ID] [--initialize-from RUN_ID]
                          [--seed SEED] [--inference] [--base-port BASE_PORT]
                          [--num-envs NUM_ENVS] [--debug] [--env-args ...]
                          [--torch] [--tensorflow] [--results-dir RESULTS_DIR]
                          [--width WIDTH] [--height HEIGHT]
                          [--quality-level QUALITY_LEVEL]
                          [--time-scale TIME_SCALE]
                          [--target-frame-rate TARGET_FRAME_RATE]
                          [--capture-frame-rate CAPTURE_FRAME_RATE]
                          [--no-graphics] [--torch-device DEVICE]
                          [trainer_config_path]
    ```

# Reference
- [1] [Unity Dev Weeks 2021: ML Agent 2.0 + AI Competition 소개](https://youtu.be/OE8Q9e0FPzU)
- [2] [Unity Technologies Blog ML-Agents v2.0 release: Now supports training complex cooperative behaviors](https://blog.unity.com/technology/ml-agents-v20-release-now-supports-training-complex-cooperative-behaviors) 
- [3] [ML-Agents Toolkit Overview](https://github.com/Unity-Technologies/ml-agents/blob/main/docs/ML-Agents-Overview.md)
- [4] [Unity ML-Agents Toolkit Github](https://github.com/Unity-Technologies/ml-agents)