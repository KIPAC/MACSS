## Installation

<img src="./images/install.jpeg" height="200">

These instructions assume that you already have a conda installation on your computer.

If you need to install conda, you can find instructions online, e.g., [here](https://www.anaconda.com/docs/getting-started/miniconda/install).

Open a terminal and do:

```bash
conda create -n macss -y python=3.12
conda activate macss
git clone https://github.com/KIPAC/MACSS.git
cd MACSS
pip install -e ".[dev]"
```

This will create a conda environment called `macss` and install the
MACSS package and its dependencies in that environment.


Test the installation and download the data for the examples:

```bash
py.test
```

This will download the data, create a directory in your home directory
called `macss` and put the data there.   Depending on your setup you
might get error about the tests, but as long as the data are
downloaded you are fine.  *You should check to make sure that the data
have been succesfully downloaded.*

If the data did not download, you can download them by hand from
[https://s3df.slac.stanford.edu/people/echarles/xfer/macss.tgz](https://s3df.slac.stanford.edu/people/echarles/xfer/macss.tgz.)


To start a jupyter session in the MACSS/nb directory that you can use
to run notebooks.

```bash
conda activate macss  # if you have not already done so in that shell
jupyter-notebook nb
```
