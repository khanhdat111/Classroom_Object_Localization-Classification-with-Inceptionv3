# Object Detection and Classification Project

## Project Description
This project focuses on object detection and classification in images using TensorFlow and OpenCV. It leverages the powerful deep learning capabilities of TensorFlow to train models on annotated datasets and OpenCV for image processing tasks. The goal is to accurately identify and classify objects within a variety of image contexts.

##Example images after processing data with truth label and bouding box 
<p align="center">
  <img src="Images/ex1.png" alt="Example Image 1" width="300"/>
  <img src="Images/ex2.png" alt="Example Image 2" width="300"/>
  <img src="Images/ex3.png" alt="Example Image 3" width="300"/>
</p>


## Features
- Use of TensorFlow for model training and inference.
- Image processing and manipulation with OpenCV.
- Evaluation of model accuracy and performance metrics.
- Visualization of detection results.

## Model
![Model](Images/model_img.png)

## Prerequisites
Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- pip (Python package installer)

## Example
You can run example notebook from `/notebooks/example.ipynb` to training model easier

## Data

The data used in this project were meticulously collected from Classroom Objects and processed by our team. We gathered images through photography and manually annotated each image with labels and bounding boxes to ensure high-quality training data for our model. This dataset is essential for the precision and effectiveness of the object detection and classification tasks.

If you wish to access the dataset, please visit the following Google Drive link:
[Access Dataset](https://drive.google.com/path_to_your_dataset)

Please note that the data is provided for academic and non-commercial use only.


## Results
**After training the model, we had a result with Mean IoU: 0.7363 - Acc: 0.9362**

<p align="center">
  <img src="Images/results.png" alt="Example Image 1" width="800"/>
</p>

## Installation

### Setting Up a Virtual Environment
It is recommended to use a virtual environment to avoid conflicts with existing Python packages from `requirements.txt`.

#### For Unix/macOS:
```bash
python3 -m venv env
source env/bin/activate
