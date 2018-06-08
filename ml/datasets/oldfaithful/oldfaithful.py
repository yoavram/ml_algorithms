"""=============================================================================
Old Faithful eruptions dataset.
============================================================================="""

import numpy as np

from   ml.normalization import feature_scaling

# ------------------------------------------------------------------------------

def load():
    """
    :return: Old faithful reuprtions data with shape (272, 2).
    """
    X = np.loadtxt('ml/datasets/oldfaithful/data', skiprows=1)[:, 1:]
    return feature_scaling(X)
