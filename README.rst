.. image:: https://img.shields.io/pypi/v/testJvis-learn.svg
    :target: https://pypi.python.org/pypi/testJvis-learn/
    :alt: PyPI Version
.. image:: https://anaconda.org/conda-forge/umap-learn/badges/version.svg
    :target: https://anaconda.org/conda-forge/testJvis-learn
    :alt: Conda-forge Version
.. image:: https://anaconda.org/conda-forge/umap-learn/badges/downloads.svg
    :target: https://anaconda.org/conda-forge/testJvis-learn
    :alt: Downloads from conda-forge
.. image:: https://img.shields.io/pypi/l/testJvis-learn.svg
    :target: https://github.com/lmcinnes/umap/blob/master/LICENSE.txt
    :alt: License
.. image:: http://joss.theoj.org/papers/10.21105/joss.00861/status.svg
    :target: xxx_paper_link
    :alt: JOSS article for this repository

====
Jvis
====

Emerging single-cell genomics technologies profile multiple types of molecules
within a single cell. A fundamental step in the analysis of the produced high
dimensional data is their visualization using dimensionality reduction techniques
such as t-SNE and UMAP. We developed Jvis, a dimensionality reduction framework
that naturally generalizes t-SNE and UMAP to the joint visualization of
multimodal omics data. Our approach  automatically learns a weighting of individual
modalities from the data that promotes discriminative features but suppresses
random noise. On 8 single-cell multimodal data sets across 5 different technologies,
Jvis produced a unified embedding that better agrees with known cell states and RNA
and protein velocity landscapes compared to unimodal representations.

The details for the underlying mathematics can be found in
insert link here.

Van Hoan Do, Stefan Canzar, A generalization of tSNE and UMAP to single cell multimodal
data, xxx.


----------
Installing
----------

Requirements:

* Python 3.6 or greater
* numpy
* scipy
* scikit-learn
* numba


**Install Options**

PyPI install, presuming you have numba and sklearn and all its requirements
(numpy and scipy) installed:

.. code:: bash

    pip install testJvis-learn

If you have a problem with pip installation then we'd suggest installing
the dependencies manually using anaconda followed by pulling umap from pip:

.. code:: bash

    conda install numpy scipy
    conda install scikit-learn
    conda install numba
    pip install testJvis-learn

---------------
How to use Jvis
---------------

The Jvis package inherits from sklearn TSNE, and UMAP. Therefore, all parameters of
tSNE and UMAP are naturally extended for Jvis.

An example of making use of these options:

.. code:: python

    from Jvis import JUMAP, JTSNE
    import numpy as np

    # Create a toy example from a random distribution (n_cells = 500)
    rna_rand = np.random.rand(500, 100)
    adt_rand = np.random.rand(500, 15)
    data = {'rna': rna_rand, 'adt': adt_rand} # create a dictionary of modalities.

    # Run joint TSNE of the two "random" modalities.
    embedding_jtsne = JTSNE(n_components=2).fit_transform(data)

    # Run joint UMAP of the two "random" modalities.
    embedding_jumap = JUMAP(n_neighbors=20,
                            min_dist=0.3,
                            metric='correlation').fit_transform(data)

For more realistic examples and Python scripts to reproduce the results
in our paper are available at GitHub: xxx

Tunning parameters of t-SNE and UMAP can be found here:
https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html

https://umap-learn.readthedocs.io/en/latest/api.html


-------
License
-------

The JVis package is 3-clause BSD licensed.

Note that the Jvis package is inherited from scikit-learn and UMAP
package under 3-clause BSD license.



