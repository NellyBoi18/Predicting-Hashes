# Predicting Hashes

[![Python Version](https://img.shields.io/badge/python-3.10.7-blue)](https://www.python.org/downloads/release/python-3107/)

## Description
This Python program takes in a CSV file containing a history of hashes and their results and uses machine learning techniques to predict future hashes. It aims to provide insights into the patterns and trends of hash generation.

## Features
- Import CSV file with hash history
- Preprocess and analyze the data
- Train a machine learning model
- Predict future hashes based on the trained model

## Installation
1. Clone the repository:
    ```shell
    git clone https://github.com/NellyBoi18/Predicting-Hashes.git
    ```
2. Navigate to the project directory:
    ```shell
    cd Predicting-Hashes
    ```
3. Install the required dependencies:
    ```shell
    pip install -r requirements.txt
    ```

## Usage
1. Make sure historical_data.csv is in the same directory as predict_hashes.py. You can use provided historical_data.csv or create your own.
2. Run the program:
    ```shell
    python3 predict_hashes.py
    ```
3. Input a hash to predict the result of.

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).