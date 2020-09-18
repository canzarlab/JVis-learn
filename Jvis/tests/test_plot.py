import numpy as np
import pytest
import Jvis
from unittest import mock

np.random.seed(42)


@pytest.fixture(scope="session")
def mapper(iris):
    return Jvis.UMAP(n_epochs=100).fit(iris.data)


def test_umap_plot_dependency():
    with mock.patch.dict("sys.modules", pandas=mock.MagicMock()):
        try:
            from Jvis import plot
        except ImportError:
            assert True
        else:
            assert False, "Exception not raised for missing dependency"


# Check that the environment is actually setup for testability
# i.e. all the extra packages have been installed
def test_umap_plot_testability():
    try:
        from Jvis import plot

        assert True
    except ImportError:
        assert False, "Missing dependencies - unable to test!"


# These tests requires revision: Refactoring is
# needed as there is no assertion nor
# property verification.
def test_plot_runs_at_all(mapper, iris):
    from Jvis import plot as umap_plot

    umap_plot.points(mapper)
    umap_plot.points(mapper, labels=iris.target)
    umap_plot.points(mapper, values=iris.data[:, 0])
    umap_plot.points(mapper, theme="fire")
    umap_plot.diagnostic(mapper, diagnostic_type="all")
    umap_plot.diagnostic(mapper, diagnostic_type="neighborhood")
    umap_plot.connectivity(mapper)
    umap_plot.interactive(mapper)
    umap_plot.interactive(mapper, labels=iris.target)
    umap_plot.interactive(mapper, values=iris.data[:, 0])
    umap_plot.interactive(mapper, theme="fire")
    umap_plot._datashade_points(mapper.embedding_)
