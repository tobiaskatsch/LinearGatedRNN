import jax.numpy as jnp

def get_model_hparams(model_variation_name):
    return dict(
        positional_encoding_mode="sinusoidal",
        n_head=6,
        use_causal_mask=True,
    )











