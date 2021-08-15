'''
Some issues with the recording right now.
ERROR: "unknown encoder 'libx264' ffmpeg"
Even after installing the specified encoder and ffmpeg with conda did not resolve this properly. Although now, the mp4 files are
generated in the 'recording' folder but the files don't open properly with QuickTime/VLC!
'''
import gym


if __name__ == "__main__":
    env = gym.make("CartPole-v0")
    env = gym.wrappers.Monitor(env, "recording", force=True)

    total_reward = 0.0
    total_steps = 0
    obs = env.reset()

    while True:
        action = env.action_space.sample()
        obs, reward, done, _ = env.step(action)
        total_reward += reward
        total_steps += 1
        if done:
            break

    print("Episode done in %d steps, total reward %.2f" % (
        total_steps, total_reward))
    env.close()
    env.env.close()
