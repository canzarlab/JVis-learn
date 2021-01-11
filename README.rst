

====
Jvis
====

Emerging single-cell technologies profile multiple types of molecules within individual cells. A fundamental step in the analysis of the produced high-dimensional data is their visualization using dimensionality reduction techniques such as t-SNE and UMAP. We introduce j-SNE and j-UMAP as their natural generalizations to the joint visualization of multimodal omics data. Our approach automatically learns the relative contribution of each modality to a concise representation of cellular identity that promotes discriminative features but suppresses noise. On eight datasets, j-SNE and j-UMAP produce unified embeddings that better agree with known cell types and that harmonize RNA and protein velocity landscapes. j-SNE and j-UMAP are available in the JVis Python package.

The details for the underlying mathematics can be found in
https://www.biorxiv.org/content/10.1101/2021.01.10.426098v1.

Van Hoan Do, Stefan Canzar, A generalization of t-SNE and UMAP to single-cell multimodal omics, 
bioRxiv (2021). doi: https://doi.org/10.1101/2021.01.10.426098


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

    pip install Jvis-learn

If you have a problem with pip installation then we'd suggest installing
the dependencies manually using anaconda followed by pulling umap from pip:

.. code:: bash

    conda install numpy scipy
    conda install scikit-learn
    conda install numba
    pip install Jvis-learn

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
in our paper are available at GitHub: https://github.com/canzarlab/JVis_paper

Tunning parameters of t-SNE and UMAP can be found here:
https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html

https://umap-learn.readthedocs.io/en/latest/api.html


-------
License
-------

The JVis package is 3-clause BSD licensed.

Jvis package is inherited from scikit-learn and UMAP
package under 3-clause BSD license.



