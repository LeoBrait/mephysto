#!/bin/bash
conda config --add channels bioconda
conda config --add channels conda-forge
conda create --name mephysto --file installation/requirements.txt