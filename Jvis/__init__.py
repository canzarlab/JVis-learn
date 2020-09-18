from .jumap_ import UMAP, JUMAPBASE, JUMAP
from ._t_sne import TSNE, JTSNEBASE, JTSNE
# Workaround: https://github.com/numba/numba/issues/3341
import numba

import pkg_resources

try:
    __version__ = pkg_resources.get_distribution("Jvis-learn").version
except pkg_resources.DistributionNotFound:
    __version__ = "0.1-dev"
