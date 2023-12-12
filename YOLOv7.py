
# cloing requirment libs for yolov7
!git clone https://github.com/WongKinYiu/yolov7.git

# your data set form the roboflow
!pip install roboflow

from roboflow import Roboflow
rf = Roboflow(api_key="BUQIxo9xwUYVHrkPx9Ik")
project = rf.workspace("nirma-university-1bjp1").project("demo_of_potholes")
dataset = project.version(8).download("yolov7")

# we are training our model with our own dataset
!python train.py --batch 25 --epochs 150 --data {dataset.location}/data.yaml --weights '/content/yolov7/yolov7_training.pt' --device 0

# fro detection 
!python detect.py --weights yolov7.pt  --source 0
