# submission후 evaluation이 진행 과정을 보여주는 code입니다.
# 채점 서버에서 다음과 같이 제출한 python script로 부터
# Agent class를 상속받고, load_model()로 제출한 model을 불러온 후
# 채점이 시작됩니다.

from Drone_gym import Drone_gym
import numpy as np
from Agent import Agent

def main():
    env = Drone_gym(
            time_scale=1,
            port=11000,
            filename='../DroneDelivery.exe')

    score = 0
    episode_step = 0
    episode = 10

    agent = Agent('cpu') # user가 제출한 Agent class에서 불러오기.
    try:
        agent.load_model() # user의 모델 불러오기. 경로는 best_model 폴더.
        print("Succeed load User's model")
    except:
        print("Fail load User's model'")
        raise

    for epi in range(episode):
        
        state = env.reset()
        while True:

            action = agent.policy(state)
            next_state, reward, done = env.step(action)

            score += reward
            episode_step += 1
            state = next_state

            if done:
                break
        print('episode: ', epi, ' score: ', score, ' everage score: ', score/episode_step)
        score = 0
        episode_step = 0
    

if __name__ == '__main__':
    main()