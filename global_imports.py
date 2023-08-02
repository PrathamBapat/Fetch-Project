from global_imports import *

import pandas as pd
import numpy as np
import os
import shutil
from annoy import AnnoyIndex
from transformers import AutoTokenizer, AutoModel
import torch

# load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained('sentence-transformers/all-mpnet-base-v2')
model = AutoModel.from_pretrained('sentence-transformers/all-mpnet-base-v2')
