# AnimalActivityRecognition

## Overview

**Animal Activity Recognition** is a deep learning project focused on animal activity recognition using **YOLO** object detection. The project aims to identify and classify various animal activities, such as running, walking, eating, etc., from video footage or live camera feed.

**Note:** This project was designed specifically to be used on Sheep. Modify it as required. 

## Instructions
1. **Clone the Repository:** Open your terminal or command prompt and clone this repository using the following command:

   ```bash
   git clone https://github.com/your-username/YoloAnimalActivityRecognition.git
   ```
2. **Navigate to the Project Directory:** Change the directory to the YoloAnimalActivityRecognition project:
   ```
   cd AnimalActivityRecognition
   ```
3. **Install Dependencies:** Ensure you have the required dependencies installed. You can set up a virtual environment and install the dependencies from the          requirements.txt file:

   ```bash
   python -m venv env
   source env/bin/activate      # On Windows, use: env\Scripts\activate
   pip install -r requirements.txt
   ```
   
## Training
   To train a new model, follow the `TrainModel.ipynb` notebook. This notebook is designed to be run in Google Colab to take advantage of GPU acceleration for        faster training. Make sure to upload the sample training data located in the data/ directory (../data) to your Google Colab workspace before executing the         notebook.
   
## Testing
   **Prepare Test Data:** Place the images or videos you want to test with the pre-trained `best.pt` model in the `Project/Test/` directory.
   
   **Run the Model:** Execute the `runModel.py` script to run the model on the test data:
   ```
   python runModel.py
   ```
   **View Results:** The results of the model's predictions will be saved in the `Project/Results/` directory.

