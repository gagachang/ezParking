# Test YOLO

YOLO website: [YOLO: Real-Time Object Detection](https://pjreddie.com/darknet/yolo/)

## Installation

Run the bash file in `ezParking/scripts`

```bash
cd ~/ezParking/scripts
bash yolo.sh
```

## Test Images

The test images are stored in `ezParking/static/img` <br />
Copy them into YOLO's directory

```bash
cd ~/ezParking/static/img
cp car2.jpg ~/darknet/data/
```

## Usage

Run the YOLO detector

```bash
cd ~/darknet
./darknet detect cfg/yolov3.cfg yolov3.weights data/car2.jpg
```

## Results

The detect result will put in `darknet` directory and named `predictions.jpg`

![image](https://github.com/gagachang/ezParking/blob/master/static/img/car2-result.png)
