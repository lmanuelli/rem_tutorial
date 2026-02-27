"""
Basic smoke tests — verify that the package and its dependencies import correctly.
"""

import rem
import numpy as np
import pandas as pd
import matplotlib


def test_rem_importable():
    assert rem.__version__ == "0.1.0"


def test_numpy_importable():
    # Confirm numpy works by doing a trivial computation
    result = np.array([1, 2, 3]).mean()
    assert result == 2.0


def test_pandas_importable():
    df = pd.DataFrame({"a": [1, 2, 3]})
    assert len(df) == 3


def test_matplotlib_importable():
    # Just check the version string exists
    assert matplotlib.__version__
