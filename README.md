# Real time face detection

- It can detect face mask in real time using *Python **OpenCV** (cv2)* and a pretrained **Keras** model.

## Topic and the Problem Statement

Corona Virus came and taught everyone the signifance of wearing a face mask.
We should have a camera detect faces and then classify wether or not they are wearing
a face mask, so that actions can be taken accordingly; this is accomplished via **Computer Vision** techniques.

## Our Approach

In project, I trained a **CNN** model using **Tensorflow/Keras** API for prediction (you can find the model's notebook [here on kaggle](https://www.kaggle.com/code/hikmatullahmohammadi/face-mask-detection)). 
I used [Face mask lite dataset](https://www.kaggle.com/datasets/prasoonkottarathil/face-mask-lite-dataset?rvi=1) which contains 20000 images of faces with and without mask, 50% each.
Then, using Opencv, I built a project to read frames from a webcam. After reading an image, it will use HAARCASCADE algorithm to detect faces within the image, and clip it.
Finally, it will classify (predict) the image into 1 (face mask) or 0 (no face mask) and display the result. 
 

## The Project Structure
**The project consists of 3 phases.**
1. Dataset examining
    In this phase, we did some research and tried a handful of different datasets to fullfil our desired performance;
    And after a while we decided to use [this dataset](https://www.kaggle.com/datasets/prasoonkottarathil/face-mask-lite-dataset?rvi=1) to train our model on;
    There were a dozen of reasons behind it most important of which are
    1: it is comprised of great amount of images (20,000), 2: there is no corrupted (not supported by Tensorflow) images in it.
2. Training the model
    After data cleaning, it was time to train the model. To build the model, I used Keras Sequential model, and trained it. I used 16,000 images as training set and 4,000 as validation set.
3. Model utilizing
  Built an OpenCV project to do prediction based on the pre-trained model. 

## Screen Shots
### With Mask:
!['With mask'](https://github.com/hikmatullah-mohammadi/real-time-face-mask-detection/blob/main/scr-shots/mask.jpg?raw=true)
### Without Mask:
![Without mask](https://github.com/hikmatullah-mohammadi/real-time-face-mask-detection/blob/main/scr-shots/no_mask.jpg?raw=true)
 
## Conclusion
    The project objective is to predict wether or not people in an image are wearing face masks. 

## Author

- Website - [Hikmatullah Mohammadi](https://hikmatullah-mohammadi.netlify.app)
- LinkedIn - [@hikmatullah-mohammadi](https://www.linkedin.com/in/hikmatullah-mohammadi-871550225)
- Github - [hikmatullah-mohammadi](https://www.github.com/hikmatullah-mohammadi)
