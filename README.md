# Crop-Recommendation

This project aims to recommend the best crop(s) to grow in a particular farm based on the soil properties and weather conditions of the area. The system uses k-Nearest Neighbors (kNN) algorithm to predict the crop(s) that are most likely to thrive in a given location.

# Dataset
The dataset used for this project contains information about the nitrogen (N), phosphorus (P) , potassium (K), temperature, humidity, ph, rainfall along with the crops that were grown in those locations. 

# Algorithm
The kNN algorithm was chosen for this project because it is a simple and effective classification algorithm that works well with small to medium sized datasets. The algorithm is implemented using scikit-learn library in Python.



 # Getting Started
To run the crop recommendation system, follow the steps below:

1. Clone the repository:
```bash
git clone https://github.com/prakrutipathak/Crop-Recommendation.git
```

2. Install the required dependencies:
```bash 
pip install -r requirements.txt
```

3. Run the Streamlit app:
```bash 
streamlit run crop.py
```
Open your web browser and navigate to http://localhost:8501 to access the Crop Recommendation application.

# Results
The model achieved an accuracy of 97% on the test set, which indicates that it can make reliable crop recommendations based on the input parameters.

 

