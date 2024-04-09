# µ-Reactors
The code in this repository has only been tested on Linux (x86-64) using Python 3.10.

## Requriements
* Python 3.10+
* [uv](https://astral.sh/uv) (recommended)

## Setup
The fastest way to get started is using `uv`.
```sh
uv venv

uv pip sync -r requirements-<platform>.txt
```

Where `<platform>` can be one of the following:
* `linux_amd64`
* `linux_arm64`
* `macos_arm64`
* `windows_amd64`

Plain `pip` should work fine but will be slower:
```sh
pip install -r requirements-<platform>.txt
```

## Contents
* `particle_stats.ipynb` - Jupyter notebook for analyzing particle statistics from microscope images.
Make sure to include the path to downloaded dataset in the first cell.
* `lib` - MicroPython library folder containing the `CtrlAer` library.
* `experiments` - MicroPython scripts for experiments in the paper.