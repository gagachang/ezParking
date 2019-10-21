#!/bin/bash

# Go into home directory
cd ~

# Clone the YOLO project
git clone https://github.com/pjreddie/darknet

# Compile and install YOLO
cd darknet
make

# Download the pre-trained weight file
wget https://pjreddie.com/media/files/yolov3.weights
