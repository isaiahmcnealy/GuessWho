# GuessWho - Facial Recognition Model Project
Facial recognition model built using the Faces in the Wild dataset, designed to identify and recognize celebrities and individuals for various applications in authentication, security, and personalized services.

## Introduction
Hey, friends! Ever found yourself racking your brain to remember the name of that actor or celebrity, only to end up calling them "that character from [insert show here]"? Well, I decided to tackle this head-on by diving into the world of facial recognition. In this project, I'll walk you through how I built and trained a facial recognition model using the Faces in the Wild dataset, aiming to solve not only my personal pet peeve but also various critical real-world problems.

## What I’m Doing
I'm creating a facial recognition model that can identify faces with impressive accuracy. By leveraging the Faces in the Wild dataset, I'm training a model to recognize and distinguish between thousands of different faces. This model will then be deployed and integrated into other applications I'm developing, making facial recognition a core feature.

## Problems It Solves
This model addresses a multitude of challenges:
- **Authentication**: Securely logging into devices and systems.
- **Security and Surveillance**: Enhancing monitoring systems to identify individuals in real-time.
- **Personal Assistance**: Instantly recognizing celebrities, making it easier to remember their names.
- **Personalized Services**: Providing tailored user experiences in retail and hospitality.

## Technologies, Libraries, and Packages
Here's the tech stack that's making all this magic happen:
- **Python**: The programming language driving the project.
- **Scikit-Learn**: For fetching and preprocessing the LFW dataset.
- **TensorFlow/Keras**: The backbone for building and training our neural network model.
- **StandardScaler**: From `sklearn.preprocessing` for normalizing the data.
- **PCA (Principal Component Analysis)**: For dimensionality reduction, helping our model to focus on the most critical features (a.k.a. Eigenfaces).

## Technical Walkthrough
1. **Loading the Dataset**: Using `fetch_lfw_people` to bring in the Faces in the Wild dataset, ensuring we have a robust set of images to work with.
2. **Data Preprocessing**: Normalizing the pixel values to enhance model performance and applying PCA to reduce dimensionality, making the model more efficient.
3. **Building the Model**: Utilizing TensorFlow/Keras to construct a convolutional neural network (CNN) with layers designed to extract and learn facial features.
4. **Training and Evaluation**: Splitting the data into training and testing sets, then training the model to recognize faces and evaluating its performance to ensure high accuracy.
5. **Deployment**: Once trained, the model will be deployed into various applications, enabling features like real-time face recognition and personalized user interactions.
