
This Python project aims to classify text as either generated by an artificial intelligence model or authored by a human. The classification is based on three metrics: surprise value (entropy), burst value (ratio of unique words to total words), and compatibility score with a dataset used to train AI models.
How it Works
1. Metrics Calculation

    Surprise Value: Calculates the entropy of the text, determining its unpredictability based on word frequency.
    Burst Value: Evaluates the ratio of unique words to the total number of words in the text.
    Compatibility Score: Compares the text with a pre-existing dataset to determine similarity.

2. AI Text Detection

    detect_ai_text(text): Combines the three metrics and computes a probability indicating the likelihood of AI generation.
    If the probability exceeds a defined threshold, it categorizes the text as AI-generated; otherwise, it categorizes it as human-authored.

Usage

    Clone the repository:

bash

git clone https://github.com/your_username/AI-vs-Human-Text-Detection.git

    Install the required libraries:

bash

pip install -r requirements.txt

    Run the detection script:

bash

python text_detection.py

Requirements

    Python 3.x
    datasets library
    math library
    collections library

Example

python

text = "Sample text to check if it's authored by AI or a human."
detect_ai_text(text)

Contributions

Contributions are welcome! If you have any improvements or suggestions, feel free to fork this repository and create a pull request.
License

This project is licensed under the MIT License - see the LICENSE file for details.
