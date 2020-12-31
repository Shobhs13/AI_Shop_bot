# AI_Shop_bot {Contextual Chatbot in PyTorch}
AI shop bot using Pytorch, Deep Learning and Natural Language Processing.  

## Installation

### Create an virtual environment
Whatever you prefer (e.g. `conda` or `venv`)
```console
conda create -n envname python=x.x anaconda
```

### Activate the virtual environment
```console
conda activate envname
```

### Install PyTorch and dependencies

For Installation of PyTorch see [official website](https://pytorch.org/).

You also need `nltk`:
 ```console
pip install nltk
 ```

If you get an error install `nltk.tokenize.punkt`:
Run this once in your terminal:
 ```console
$ python
>>> import nltk
>>> nltk.download('punkt')
```

## Usage {Command Line}
Run
```console
python train.py
```
This will dump `data.pth` file. And then run
```console
python chat.py
```
