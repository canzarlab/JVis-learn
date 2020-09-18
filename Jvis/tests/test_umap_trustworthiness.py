from Jvis import UMAP
from sklearn.datasets import make_blobs
from nose.tools import assert_greater_equal
import numpy as np

try:
    # works for sklearn>=0.22
    from sklearn.manifold import trustworthiness
except ImportError:
    # this is to comply with requirements (scikit-learn>=0.20)
    # More recent versions of sklearn have exposed trustworthiness
    # in top level module API
    # see: https://github.com/scikit-learn/scikit-learn/pull/15337
    from sklearn.manifold.t_sne import trustworthiness

# ===================================================
#  UMAP Trustworthiness Test cases
# ===================================================


def test_umap_sparse_trustworthiness(sparse_test_data):
    embedding = UMAP(n_neighbors=10).fit_transform(sparse_test_data[:100])
    trust = trustworthiness(sparse_test_data[:100].toarray(), embedding, 10)
    assert_greater_equal(
        trust,
        0.89,
        "Insufficiently trustworthy embedding for"
        "sparse test dataset: {}".format(trust),
    )


def test_umap_trustworthiness_fast_approx(nn_data):
    data = nn_data[:50]
    embedding = UMAP(
        n_neighbors=10,
        min_dist=0.01,
        random_state=42,
        n_epochs=100,
        force_approximation_algorithm=True,
    ).fit_transform(data)
    trust = trustworthiness(data, embedding, 10)
    assert_greater_equal(
        trust,
        0.75,
        "Insufficiently trustworthy embedding for" "nn dataset: {}".format(trust),
    )


def test_umap_trustworthiness_random_init(nn_data):
    data = nn_data[:50]
    embedding = UMAP(
        n_neighbors=10, min_dist=0.01, random_state=42, init="random"
    ).fit_transform(data)
    trust = trustworthiness(data, embedding, 10)
    assert_greater_equal(
        trust,
        0.75,
        "Insufficiently trustworthy embedding for" "nn dataset: {}".format(trust),
    )


def test_supervised_umap_trustworthiness():
    data, labels = make_blobs(50, cluster_std=0.5, random_state=42)
    embedding = UMAP(n_neighbors=10, min_dist=0.01, random_state=42).fit_transform(
        data, labels
    )
    trust = trustworthiness(data, embedding, 10)
    assert_greater_equal(
        trust,
        0.97,
        "Insufficiently trustworthy embedding for" "blobs dataset: {}".format(trust),
    )


def test_semisupervised_umap_trustworthiness():
    data, labels = make_blobs(50, cluster_std=0.5, random_state=42)
    labels[10:30] = -1
    embedding = UMAP(n_neighbors=10, min_dist=0.01, random_state=42).fit_transform(
        data, labels
    )
    trust = trustworthiness(data, embedding, 10)
    assert_greater_equal(
        trust,
        0.97,
        "Insufficiently trustworthy embedding for" "blobs dataset: {}".format(trust),
    )


def test_metric_supervised_umap_trustworthiness():
    data, labels = make_blobs(50, cluster_std=0.5, random_state=42)
    embedding = UMAP(
        n_neighbors=10,
        min_dist=0.01,
        target_metric="l1",
        target_weight=0.8,
        n_epochs=100,
        random_state=42,
    ).fit_transform(data, labels)
    trust = trustworthiness(data, embedding, 10)
    assert_greater_equal(
        trust,
        0.95,
        "Insufficiently trustworthy embedding for" "blobs dataset: {}".format(trust),
    )


def test_string_metric_supervised_umap_trustworthiness():
    data, labels = make_blobs(50, cluster_std=0.5, random_state=42)
    labels = np.array(["this", "that", "other"])[labels]
    embedding = UMAP(
        n_neighbors=10,
        min_dist=0.01,
        target_metric="string",
        target_weight=0.8,
        n_epochs=100,
        random_state=42,
    ).fit_transform(data, labels)
    trust = trustworthiness(data, embedding, 10)
    assert_greater_equal(
        trust,
        0.95,
        "Insufficiently trustworthy embedding for" "blobs dataset: {}".format(trust),
    )


def test_discrete_metric_supervised_umap_trustworthiness():
    data, labels = make_blobs(50, cluster_std=0.5, random_state=42)
    embedding = UMAP(
        n_neighbors=10,
        min_dist=0.01,
        target_metric="ordinal",
        target_weight=0.8,
        n_epochs=100,
        random_state=42,
    ).fit_transform(data, labels)
    trust = trustworthiness(data, embedding, 10)
    assert_greater_equal(
        trust,
        0.95,
        "Insufficiently trustworthy embedding for" "blobs dataset: {}".format(trust),
    )


def test_count_metric_supervised_umap_trustworthiness():
    data, labels = make_blobs(50, cluster_std=0.5, random_state=42)
    labels = (labels ** 2) + 2 * labels
    embedding = UMAP(
        n_neighbors=10,
        min_dist=0.01,
        target_metric="count",
        target_weight=0.8,
        n_epochs=100,
        random_state=42,
    ).fit_transform(data, labels)
    trust = trustworthiness(data, embedding, 10)
    assert_greater_equal(
        trust,
        0.95,
        "Insufficiently trustworthy embedding for" "blobs dataset: {}".format(trust),
    )
