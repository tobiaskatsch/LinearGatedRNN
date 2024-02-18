import jax.numpy as jnp

def get_model_hparams(model_variation_name):
    if model_variation_name == "expressive":
        return dict(
            positional_encoding_mode="none",
            d_h=384*2,
            use_true_recurrence=True,
            bidirectional=False,
        )
    elif model_variation_name == "efficient":
        return dict(
            positional_encoding_mode="none",
            d_h=384*2,
            use_true_recurrence=False,
            bidirectional=False,
        )
    else:
        raise NotImplementedError
















