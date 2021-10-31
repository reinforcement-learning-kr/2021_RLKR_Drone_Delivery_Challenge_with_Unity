# submission을 위한 Agent 파일 입니다.
# policy(), save_model(), load_model()의 arguments와 return은 지켜주시기 바랍니다.
# 그 외에 자유롭게 코드를 작성 해주시기 바랍니다.

import numpy as np

class Agent:
    def __init__(self):
        self.model = None

    def policy(self, state):
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
        action = np.random.randint(27) # Random policy for inferencing test.

        return action
    
    def save_model(self):
        """Save Policy network.
        
        Args:
            None
        
        Return:
            None
        """
        # self.model.save('./best_model/best_policy.pt') # save pytorch, tensorflow or etc.
        return Nones

    def load_model(self):
        """load Policy network.

        Args:
            None
        
        Return:
            None

        """
        # self.model.load('./best_model/best_policy.pt') # load pytorch, tensorflow or etc.
        return None
