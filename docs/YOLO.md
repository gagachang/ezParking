# Test YOLO

## Installation

Run the bash file in `/scripts`

```bash
cd ezParking/scripts
bash yolo.sh
```

## Test Images

The test images are stored in `ezParking/testImage`
Copy them into YOLO directory

```bash
cd ezParking/testImage
cp *.jpg ~/darknet/data/
```

## Usage

Run the YOLO detector

```bash
cd ezParking/darknet
./darknet detect cfg/yolov3.cfg yolov3.weights data/car1.jpg
```
