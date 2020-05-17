params = {
    'type': 'MBPO',
    'universe': 'gym',
    'domain': 'PybulletHumanoid', ## mbpo/env/humanoid.py
    'task': 'v0',

    'log_dir': '~/ray_mbpo/',
    'exp_name': 'defaults',

    'kwargs': {
        'n_epochs': 5000,
        'epoch_length': 100,
        'train_every_n_steps': 1,
        'n_train_repeat': 20,
        'eval_render_mode': None,
        'eval_n_episodes': 1,
        'eval_deterministic': True,

        'discount': 0.99,
        'tau': 5e-3,
        'reward_scale': 1.0,

        'model_train_freq': 1000,
        'model_retain_epochs': 5,
        'rollout_batch_size': 100e3,
        'deterministic': False,
        'num_networks': 7,
        'num_elites': 5,
        'real_ratio': 0.05,
        'target_entropy': -2,
        'max_model_t': None,
        'rollout_schedule': [20, 300, 1, 25],
        # 'hidden_dim': 400,
    }
}
