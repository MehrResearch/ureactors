# µ-Reactors
This repository contains both MicroPython code for execution of experiments on the Raspberry Pi Pico or compatible RP2040-based boards, as well as a Jupyter notebook for analyzing microscope images of the experiments for particle statistics.

## MicroPython code
The MicroPython code is located in the `lib` and `experiments` folders. The `lib` folder contains the `CtrlAer` library, which is a collection of modules for controlling the RP2040-based board and the peripherals connected to it. The `experiments` folder contains the scripts for running the experiments described in the paper.

To run the experiments, copy the contents of the `lib` and `experiments` folders to the using the Thonny IDE or the `rshell` tool. The exact GPIO pins used for the peripherals may need to be adjusted in the scripts depending on your specific board and circuit configuration. In our case, using the Pimoroni Tiny2040, GPIO 0 and 1 are used, which are connected to board pins 0 and 1, respectively.

## Jupyter notebook
The Jupyter notebook `particle_stats.ipynb` is used for analyzing microscope images of the experiments. The code in this repository has only been tested on Linux (x86-64) using Python 3.10 and can be run by following the manual steps below or by using the dev container, e.g. in Visual Studio Code.

### Requirements
* Python 3.10+
* nvidia drivers if using a GPU for image processing (highly recommended)

### Setup
The fastest way to get started is using a dev container. Simply open the folder in Visual Studio Code (locally or on a remote machine) and select "Reopen in Container" from the notification that appears. This will build the dev container and open the folder in a new window. All dependencies will be installed automatically.
