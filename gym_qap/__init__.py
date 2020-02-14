from gym.envs.registration import register

register(
    id='qap-v0',
    entry_point='gym_qap.envs:QapEnv',
)