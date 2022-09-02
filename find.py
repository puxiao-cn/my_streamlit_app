
from pickle import TRUE
from re import T
import numpy as np
import pandas as pd
from PIL import Image
import csv
import subprocess
import os
import threading
import base64
import time
import shutil
import argparse
import warnings

cwdX = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
cwdUpper = os.path.dirname(cwdX)
subdir_path = cwdX + r"/CAP"

print(cwdX)
print(cwdUpper)
print(subdir_path)

a = os.getcwd()
print(a)
