# submission을 위한 Agent 파일 입니다.
# policy(), save_model(), load_model()의 arguments와 return은 변경하실 수 없습니다.
# 그 외에 자유롭게 코드를 작성 해주시기 바랍니다.

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.distributions import Categorical
from collections import deque
from Drone_gym import Drone_gym

## 이미지 관련 코드 
import matplotlib.pyplot as plt
from skimage.transform import resize
from skimage.color import rgb2gray

class A2C_network(nn.Module):
    def __init__(self):
        super(A2C_network, self).__init__()

        self.vector_fc = nn.Linear(95, 512) # embedding vector observation
        
        self.image_cnn = nn.Sequential(
            nn.Conv2d(4,32,kernel_size=8,stride=4),
            nn.ReLU(),
            nn.Conv2d(32,64,kernel_size=4,stride=2),
            nn.ReLU(),
            nn.Conv2d(64,64,kernel_size=3,stride=1),
            nn.ReLU()
            )
        self.image_fc = nn.Linear(1024,512) ## embedding image observation
    
        self.fc1 = nn.Linear(1024, 512)
        self.fc2 = nn.Linear(512, 512)

        self.fc_value1 = nn.Linear(512, 256)
        self.fc_value2 = nn.Linear(256, 1) 
        
        self.fc_action1 = nn.Linear(512, 256)
        self.fc_action2 = nn.Linear(256, 27)

    def forward(self,x):
        
        front_obs, right_obs, rear_obs, left_obs, btn_obs, vector_obs = x
        batch = front_obs.size(0)

        vector_obs = self.vector_fc(vector_obs).view(batch,-1) 
        
        front_obs = self.image_fc(self.image_cnn(front_obs).view(batch,-1)) 
        right_obs = self.image_fc(self.image_cnn(right_obs).view(batch,-1))
        rear_obs = self.image_fc(self.image_cnn(rear_obs).view(batch,-1))
        left_obs = self.image_fc(self.image_cnn(left_obs).view(batch,-1))
        btn_obs = self.image_fc(self.image_cnn(btn_obs).view(batch,-1))

        image_obs = (front_obs + right_obs + rear_obs + left_obs + btn_obs)
        
        x = torch.cat((vector_obs,image_obs),-1)
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))

        v = torch.relu(self.fc_value1(x))
        v = self.fc_value2(v)

        action_logit = torch.relu(self.fc_action1(x))
        action_logit = self.fc_action2(action_logit)
        action_distribution = F.softmax(action_logit, dim=-1) ## ouput is action distribution.

        return action_distribution, v
     
class Agent:
    def __init__(self, device):
        self.policy_net = A2C_network().to(device)
        self.device = device
        self.data_buffer = deque(maxlen=8)
        self.learning_rate = 0.00025
        self.a2c_optimizer = optim.Adam(self.policy_net.parameters(), lr=self.learning_rate)

    def policy(self, obs): 
        """Policy function p(a|s), Select three actions.

        Args:
            obs: all observations. consist of 6 observations.
                   (front image observation, right image observation, 
                   rear image observation, left image observation, 
                   bottom observation, vector observation)

        Return:
            3 continous actions vector (range -1 ~ 1) from policy.
            ex) [-1~1, -1~1, -1~1]
        """
        action_distribution, _ = self.policy_net(obs)
        distribution = Categorical(action_distribution) ## pytorch categorical 함수는 array에 담겨진 값들을 확률로 정해줍니다.
        action = distribution.sample().item()
     
        return self.convert_action(action) ## inference를 위한 (x, y, z) 위치 action.

    def train_policy(self, obs):
        action_distribution, _ = self.policy_net(obs)
        distribution = Categorical(action_distribution) ## pytorch categorical 함수는 array에 담겨진 값들을 확률로 정해줍니다.
        action = distribution.sample().item()
     
        return self.convert_action(action), action
    
    def save_model(self):
        torch.save(self.policy_net.state_dict(), './best_model/best_model.pkl')
        return None

    def load_model(self):
        self.policy_net.load_state_dict(torch.load('./best_model/best_model.pkl'))
        return None

    def store_trajectory(self, traj):
        """
           store data
        """
        self.data_buffer.append(traj)

    def init_buffer(self):
        """
           initialize data buffer
        """
        del self.data_buffer
        self.data_buffer = deque(maxlen=8)

    def re_scale_frame(self, obs):
        """
        change rgb to gray.
        """
        return resize(rgb2gray(obs),(64,64))

    def init_image_obs(self, obs):
        """
        set initial observation s_0, stacked 4 s_0 frames.
        """
        obs = self.re_scale_frame(obs)
        frame_obs = [obs for _ in range(4)]
        frame_obs = np.stack(frame_obs, axis=0)

        return frame_obs

    def init_obs(self, obs):
        """
           set initial observation
        """
        front_obs = self.init_image_obs(obs[0])
        right_obs = self.init_image_obs(obs[1])
        rear_obs = self.init_image_obs(obs[2])
        left_obs = self.init_image_obs(obs[3])
        btn_obs = self.init_image_obs(obs[4])
        vector_obs = obs[5]
        
        return (front_obs,right_obs,rear_obs,left_obs,btn_obs,vector_obs)

    def torch_obs(self, obs):
        """
            convert to torch tensor
        """
        front_obs = torch.Tensor(obs[0]).unsqueeze(0).to(self.device)
        right_obs = torch.Tensor(obs[1]).unsqueeze(0).to(self.device)
        rear_obs = torch.Tensor(obs[2]).unsqueeze(0).to(self.device)
        left_obs = torch.Tensor(obs[3]).unsqueeze(0).to(self.device)
        btn_obs = torch.Tensor(obs[4]).unsqueeze(0).to(self.device)
        vector_obs = torch.Tensor(obs[5]).to(self.device) # 16
  
        return (front_obs,right_obs,rear_obs,left_obs,btn_obs,vector_obs)

    def accumulated_image_obs(self, obs, new_frame):
        """
            accumulated image observation.
        """
        temp_obs = obs[1:,:,:]
        new_frame = np.expand_dims(self.re_scale_frame(new_frame), axis=0)
        frame_obs = np.concatenate((temp_obs, new_frame),axis=0)
    
        return frame_obs

    def accumulated_all_obs(self, obs, next_obs): 
        """
            accumulated all observation.
        """
        front_obs = self.accumulated_image_obs(obs[0], next_obs[0])
        right_obs = self.accumulated_image_obs(obs[1], next_obs[1])        
        rear_obs = self.accumulated_image_obs(obs[2], next_obs[2])
        left_obs = self.accumulated_image_obs(obs[3], next_obs[3])
        btn_obs = self.accumulated_image_obs(obs[4], next_obs[4])
        vector_obs = next_obs[5]
     
        return (front_obs,right_obs,rear_obs,left_obs,btn_obs,vector_obs)

    def convert_action(self, action):
        if action == 0:
            return [-1, -1, -1]
        elif action == 1:
            return [-1, -1,  0]
        elif action == 2:
            return [-1, -1,  1]
        elif action == 3:
            return [-1,  0, -1]
        elif action == 4:
            return [-1,  0,  0]
        elif action == 5:
            return [-1,  0,  1]
        elif action == 6:
            return [-1,  1, -1]
        elif action == 7:
            return [-1,  1,  0]
        elif action == 8:
            return [-1,  1,  1]
        elif action == 9:
            return [ 0, -1, -1]
        elif action == 10:
            return [ 0, -1,  0]
        elif action == 11:
            return [ 0, -1,  1]
        elif action == 12:
            return [ 0,  0, -1]
        elif action == 13:
            return [ 0,  0,  0]
        elif action == 14:
            return [ 0,  0,  1]
        elif action == 15:
            return [ 0,  1, -1]
        elif action == 16:
            return [ 0,  1,  0]
        elif action == 17:
            return [ 0,  1,  1]
        elif action == 18:
            return [ 1, -1, -1]
        elif action == 19:
            return [ 1, -1,  0]
        elif action == 20:
            return [ 1, -1,  1]
        elif action == 21:
            return [ 1,  0, -1]
        elif action == 22:
            return [ 1,  0,  0]
        elif action == 23:
            return [ 1,  0,  1]
        elif action == 24:
            return [ 1,  1, -1]
        elif action == 25:
            return [ 1,  1,  0]
        elif action == 26:
            return [ 1,  1,  1]

    
    def td_target(self, values, rewards, masks):
        gamma = 0.99
        
        target_y = torch.zeros_like(rewards)
        next_value = 0
        
        for t in reversed(range(0,len(rewards))):
            target_y[t] = rewards[t] + gamma*next_value*masks[t] ## 특정 t 시점부터 expected next~t에 해당하는 value가 discounted 됨.
            next_value = values.data[t]
        return target_y
    
    def batch_torch_obs(self, obs):
        front_obs = torch.Tensor(np.stack([s[0] for s in obs], axis=0)).to(self.device)
        right_obs = torch.Tensor(np.stack([s[1] for s in obs], axis=0)).to(self.device)      
        rear_obs = torch.Tensor(np.stack([s[2] for s in obs], axis=0)).to(self.device)
        left_obs = torch.Tensor(np.stack([s[3] for s in obs], axis=0)).to(self.device)
        btn_obs = torch.Tensor(np.stack([s[4] for s in obs], axis=0)).to(self.device)
        vector_obs = torch.Tensor(np.stack([s[5] for s in obs], axis=0)).to(self.device)
        
        return (front_obs,right_obs,rear_obs,left_obs,btn_obs,vector_obs)

    def train(self):        
        # data 분배
        obs_list, action_list, reward_list, next_obs_list, mask_list = [], [], [], [], []
        
        for all_obs in self.data_buffer:
            s, a, r, next_s, mask = all_obs
            obs_list.append(s)
            action_list.append(a)
            reward_list.append(r)
            next_obs_list.append(next_s)
            mask_list.append(mask)
        
        # tensor.
        obss = self.batch_torch_obs(obs_list)
        actions = torch.LongTensor(action_list).unsqueeze(1).to(self.device)
        rewards = torch.Tensor(reward_list).to(self.device)
        next_obss = self.batch_torch_obs(next_obs_list)
        masks = torch.Tensor(mask_list).to(self.device)

        # actor_loss
        action_distribution, values = self.policy_net(obss)
        entropy = Categorical(action_distribution).entropy().mean()
        policy = action_distribution.gather(1,actions)
        log_policy = torch.log(policy).view(-1)
        values = values.view(-1)

        target_y = self.td_target(values, rewards, masks) ## 시간차 타겟을 구한다.
    
        advantages = target_y - values ## r_t + gamma * v(s_t+1) - v(s_t) 
        actor_loss = torch.sum(-log_policy*advantages.detach())
    
        # critic_loss
        mse_loss = torch.nn.MSELoss()
        critic_loss = mse_loss(target_y.detach(), values)
     
        a2c_loss = actor_loss + (0.5 * critic_loss) - (0.001 * entropy)

        # backward
        self.a2c_optimizer.zero_grad()
        torch.nn.utils.clip_grad_norm_(self.policy_net.parameters(), 0.5)
        a2c_loss.backward()
        self.a2c_optimizer.step()
        self.init_buffer()

def main():
    env = Drone_gym(
            time_scale=1.0,
            port=11000,
            filename='../RL_Drone/DroneDelivery.exe')

    score = 0
    reward_score = 0
    episode_step = 0
    train_step = 0
    episode = 999999999999

    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu") 
    agent = Agent(device)
  
    for epi in range(episode):
        obs = env.reset()
        obs = agent.init_obs(obs)
        while True:

            action, dis_action = agent.train_policy(agent.torch_obs(obs))
            next_obs, reward, done = env.step(action)

            next_obs = agent.accumulated_all_obs(obs, next_obs)
            mask = 0 if done else 1
            
            score += reward
            # reward = np.clip(reward, -2, 2) # reward clipping 사용 자유.
            reward_score += reward
            agent.store_trajectory((obs, dis_action, reward, next_obs,  mask))
            obs = next_obs
            

            if train_step % 8 == 0 and train_step != 0:
                agent.train() # batch마다 train한다.
                if train_step % 16 == 0:
                    agent.save_model() # 16 step마다 model 저장.
            episode_step += 1
            train_step += 1

            if done:
                break
            
        print('episode: ', epi, ' True_score: ', score, ' everage score: ', reward_score/episode_step)
        score = 0
        reward_score = 0
        episode_step = 0
    
if __name__ == '__main__':
    main()