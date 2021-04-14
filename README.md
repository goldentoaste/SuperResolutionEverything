# SuperResolutionEverything
Applies a simple super resolution model to all images in a directory and all sub directory.

Run superRes.py and follow prompts to use.


# Dependency & setup
This relies on (this)[https://github.com/tsurumeso/waifu2x-chainer]. Download the entire projects folder, add waifu2x.py to system environment PATH, and then setup .py file association with python.exe

Then use pip to install chainer and cupy-cuda112, also, get the lastest Cuda toolkit from nvidia to enable gpu acceleration. Cpu only too slow to be useful(~4minutes/image).

Finally, find cuda.py in chainer, and remove line 69(from cupy.util import PerformanceWarning as \_PerformanceWarning  # NOQA), this line causes import issues and is not needed at all.
