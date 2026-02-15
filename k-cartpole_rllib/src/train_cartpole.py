import ray
from ray.rllib.algorithms.ppo import PPOConfig

def main():
    ray.init()

    config = (
        PPOConfig()
        .environment("CartPole-v1")
        .framework("torch")
        .resources(num_gpus=0)
        .env_runners(num_env_runners=1)
    )

    algo = config.build()

    for i in range(10):
        result = algo.train()

        reward_mean = (
            result.get("env_runners", {})
                  .get("episode_return_mean", None)
        )

        print(f"Iter {i}, reward_mean={reward_mean}")

        if reward_mean is not None and reward_mean >= 450:
            print("Solved CartPole!")
            break

    checkpoint = algo.save()
    print("Checkpoint saved at:", checkpoint)

    algo.stop()
    ray.shutdown()

if __name__ == "__main__":
    main()
