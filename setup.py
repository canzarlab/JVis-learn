from setuptools import setup


def readme():
    try:
        with open("README.rst", encoding="UTF-8") as readme_file:
            return readme_file.read()
    except TypeError:
        # Python 2.7 doesn't support encoding argument in builtin open
        import io

        with io.open("README.rst", encoding="UTF-8") as readme_file:
            return readme_file.read()


configuration = {
    "name": "testJvis-learn",
    "version": "0.0.6",
    "description": "A generalization of tSNE and UMAP to single cell multimodal data",
    "long_description": readme(),
    "long_description_content_type": "text/x-rst",
    "classifiers": [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "License :: OSI Approved",
        "Programming Language :: C",
        "Programming Language :: Python",
        "Topic :: Software Development",
        "Topic :: Scientific/Engineering",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Operating System :: MacOS",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.8",
    ],
    "keywords": "dimension reduction t-sne umap manifold multimodal data",
    "url": "http://github.com/xxx",
    "maintainer": "Van Hoan Do",
    "maintainer_email": "vanhoan310@gmail.com",
    "license": "BSD",
    "packages": ["Jvis"],
    "install_requires": [
        "numpy >= 1.17",
        "scikit-learn >= 0.20",
        "scipy >= 1.3.1",
        "numba >= 0.46, != 0.47",
    ],
    "extras_require": {
        "plot": [
            "pandas",
            "matplotlib",
            "datashader",
            "bokeh",
            "holoviews",
            "colorcet",
        ],
        "performance": ["pynndescent >= 0.4", "tbb >= 2019.5"],
    },
    "ext_modules": [],
    "cmdclass": {},
    "test_suite": "nose.collector",
    "tests_require": ["nose"],
    "data_files": (),
    "zip_safe": False,
}

setup(**configuration)
