
Materials for the photometric redshift (PZ) project in the MACSS.


Installation.

These instructions assume that you already have a conda installation on your computer.

```bash
conda create -n macss python=3.12
git clone https://github.com/KIPAC/MACSS.git
cd MACSS
pip install -e ".[dev]"
```


Test the installation and download the data for the exampes

```bash
py.test
```




[Page source](https://github.com/kipac/macss)
