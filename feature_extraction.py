import numpy as np


def get_embedding(model, file, max_sec):
    """
    Extract an embedding from an audio file using the supplied model.
    """
    # Placeholder for the audio feature-extraction pipeline
    # used by the original project.
    result = model.predict(file)

    return np.array(result)
