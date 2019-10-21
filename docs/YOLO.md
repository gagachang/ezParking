# Test YOLO

## Installation

Run the bash file in `ezParking/scripts`

```bash
cd ezParking/scripts
bash yolo.sh
```

## Test Images

The test images are stored in `ezParking/testImage` <br />
Copy them into YOLO directory

```bash
cd ezParking/testImage
cp *.jpg ~/darknet/data/
```

## Usage

Run the YOLO detector

```bash
cd ezParking/darknet
./darknet detect cfg/yolov3.cfg yolov3.weights data/car2.jpg
```

## Results

The detect result for `car2.jpg`

![image](https://github.com/gagachang/ezParking/blob/master/testImage/car2-result.png)
