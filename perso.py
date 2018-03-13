import random
import math

import numpy as np
import tensorflow as tf


from pysc2.agents import base_agent
from pysc2.lib import actions
from pysc2.lib import features

_NO_OP = actions.FUNCTIONS.no_op.id
_MOVE_SCREEN = actions.FUNCTIONS.Attack_screen.id
_SELECT_ARMY = actions.FUNCTIONS.select_army.id

_NOT_ADD = [0]
_NOT_QUEUED = [0]
_QUEUED = [1]

_PLAYER_RELATIVE = features.SCREEN_FEATURES.player_relative.index
_PLAYER_NEUTRAL = 3 # beacon ??????



class OneLayerCompass:
        def __init__(self, learning_rate=0.1):
            #this learning rate is random
            tf.logging.set_verbosity(tf.logging.INFO)



        def cnn_model_fn(features, labels, mode):
            # implementer svp
            pool1 = tf.layers.max_pooling2d(inputs=conv1, pool_size=[2, 2], strides=2)




class TestAgent(base_agent.BaseAgent):
    def __init__(self):
        super(TestAgent, self).__init__()
        self.first_select = False
        self.compass = None

    def step(self, obs):
        super(TestAgent, self).step(obs)

        if _MOVE_SCREEN in obs.observation['available_actions']:

            player_relative = obs.observation["screen"][_PLAYER_RELATIVE]

            ####### TOTAL CHEAT : go deep
            neutral_y, neutral_x = (player_relative == _PLAYER_NEUTRAL).nonzero()

            print("\n le neutre de ROLAND BARTHES :")
            print(neutral_x)
            print(neutral_y)
            print("")
            exit()

            if not neutral_y.any():
                return actions.FunctionCall(_NO_OP, [])
            target = [int(neutral_x.mean()), int(neutral_y.mean())]
            ######

            return actions.FunctionCall(_MOVE_SCREEN, [_NOT_QUEUED, target])

        else :
            return actions.FunctionCall(_SELECT_ARMY, [_NOT_ADD])

        return actions.FunctionCall(_NO_OP, [])
