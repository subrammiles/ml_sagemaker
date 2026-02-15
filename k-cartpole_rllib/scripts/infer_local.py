import numpy as np
from ray.rllib.policy.policy import Policy

policy = Policy.from_checkpoint("model")

# Example state:
# [cart_pos, cart_vel, pole_angle, pole_ang_vel]
obs = np.array([0.0, 0.1, 0.0, -0.1], dtype=np.float32)

action, _, _ = policy.compute_single_action(obs)

print("Action:", action)
