# IPL Win Predictor

## Overview
The IPL Win Predictor is a web application that combines data science, machine learning, and web development to provide users with insightful predictions about the outcome of IPL matches. It also includes an API that allows users to make predictions programmatically.

## Software Requirements
1. [Visual Studio Code (VSCODE) IDE](https://code.visualstudio.com/)
2. [GitHub Account](https://github.com/)
3. [Git CLI](https://git-scm.com/downloads)
4. [Streamlit](https://streamlit.io/cloud)
5. [Data Source](https://www.kaggle.com/)

## Getting Started

### 1. Clone the Repository
Clone the repository to your local machine:

```bash
git clone https://github.com/sohel1807/IPL_WIN_PREDICTOR.git
```

### 2. Navigate to the project directory
```bash
cd IPL_WIN_PREDICTOR
```

### 3. Install dependencies
```bash
pip install streamlit
```

### 4. Run the development server
Run the project on your local machine:
```bash
streamlit run iplapp.py
```

The web application will start running.

## IPL Win Predictor API

This API predicts the winning probabilities of an IPL match based on the current game situation.

### Endpoint
**URL:** `https://sohel1807--predict.modal.run`  
**Method:** `POST`  
**Content-Type:** `application/json`

### Request

#### Sample Input
```json
{
    "batting_team": "Chennai Super Kings",
    "bowling_team": "Royal Challengers Bangalore",
    "city": "Bengaluru",
    "total_runs": 120,
    "current_score": 110,
    "wickets": 5,
    "overs_completed": 12.0
}
```

#### Parameters
- **batting_team**: The team currently batting.
- **bowling_team**: The team currently bowling.
- **city**: The city where the match is being played.
- **total_runs**: The target score that the batting team needs to achieve.
- **current_score**: The current score of the batting team.
- **wickets**: The number of wickets that the batting team has lost.
- **overs_completed**: The number of overs that have been completed.

### Usage

#### Python Example
```python
import requests

url = "https://sohel1807--predict.modal.run"
data = {
    "batting_team": "Chennai Super Kings",
    "bowling_team": "Royal Challengers Bangalore",
    "city": "Bengaluru",
    "total_runs": 120,
    "current_score": 110,
    "wickets": 5,
    "overs_completed": 12.0
}

response = requests.post(url, json=data)
print(response.json())
```

### Deployment
This API is built and deployed. The model used for prediction is trained with `scikit-learn` and serialized using `pickle`.

## Contributing
If you'd like to contribute to the project, feel free to fork the repository, make your changes, and submit a pull request. Contributions are welcome and appreciated!

## Issues
If you encounter any issues or have suggestions for improvement, please open an issue on GitHub, and we'll address it as soon as possible.

### Author
- [Sohel1807](https://github.com/sohel1807)