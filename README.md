# A Printed Character Recognition System for Meetei-Mayek Script using Transfer Learning

DEPARTMENT OF COMPUTER SCIENCE & ENGINEERING NATIONAL INSTITUTE OF TECHNOLOGY, MANIPUR

© 2023 ALL RIGHTS RESERVED. 





Goal is to develop a Character Recognition System where a database consists of images containing printed characters of Meetei Mayek, using segmentation and Convolutional Neural Network. The CNN’s can be built using the concept of transfer learning and the base CNN’s used are: MobileNetV2, ResNet152V2, VGG16, VGG19, and Xception.

Developing an Optical Character Recognition System with high accuracy for Meetei-Mayek involves concentrated research efforts, large datasets, and the use of advanced deep learning models. It is conceivable to construct a dependable system that can contribute to the preservation and development of regional scripts in northeastern India by resolving the complexity and challenges specifically here for Meetei-Mayek characters. And this can be achieved by building a good segmentation system along with a Convolutional Neural Network with high accuracy


To build an OCR system the following subproblems are to be addressed: Preprocessing, Segmentation, Database Creation, Convolutional Neural Network (feature extraction and classification). Instead of building a CNN from scratch it can be built using the Transfer Learning which utilizes the “previous model”


In order to build a character recognition system, we need a segmentation system and a Convolutional Neural Network (CNN). The segmentation system takes an image consisting of Meetei-Mayek text as input and gives us the segmented images of the input images, This output images are nothing but individual character images that are in the input image. Now these individual character images are sent to the trained Convolutional Neural Network (CNN) which gives us a number (assigned to the most active neuron) which is then used to get the corresponding unicode character. All the unicode characters are printed as text in the format of lines and words that are in the input image

### A brief ocr system architecture 
![Meetei-Mayek Character Recognition System architecture ](https://github.com/Mr-barnes/Final_Year_project/blob/main/meetei_mayek_Article%20images/images/1.3.png)

- A article image undergoes Image Segmentation which is done in three parts: line, word and character
- Each outcome character manually segregate into respective character folders
- The classification task has been carried out using transfer learning with pre-trained models: MobileNet-V2, VGG-16, VGG-19, ResNet152-V2 and Xception convolutional neural networks inorder to carry out predictions
- The conversion of Predictions carryout by unicode characters (fonts are downloded from google)
- These unicode characters process with respective CNN and Finally Converted into text.
### The Final Output of Meetei-Mayek Character Recognition System.
![Meetei-Mayek Character Recognition System architecture ](https://github.com/Mr-barnes/Final_Year_project/blob/main/meetei_mayek_Article%20images/images/4.12.png)
