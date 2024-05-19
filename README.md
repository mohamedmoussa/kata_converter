# Kata: Number to French Converter

**NOTE:** the code developed in this project is based on the code from this repositroy https://github.com/DeathReaper0965/kata-number-convert-french.


This repo presents an adventure of approaches for converting a number to french format strings(words).

Made using [Streamlit](https://streamlit.io/) 
## Features
This application has TWO core functionalities. Their details are as follows:

### Accepts the input numbers as a string and returns their french form as outputs 

1. **Input List of numbers:** [MANDATORY] This is a comma separated string that is splitted internally to process one number at a time.
2. **French Style**: [OPTIONAL] Currently two French Styles are followed, select from either of `France-French` or `Belgium-french`. Defaults to `France-French`.
3. **Output Type**: [OPTIONAL] Either of `JSON` or `LIST`. Defaults to `LIST`.
    - if `JSON` is selected, a Dictionary of values corresponding to each input number is displayed.
    - if `LIST` is selected, a List of values are displayed in the given order of the input.


## Installation
Follow the below steps to run the application in your local machine:
1. Clone the repo: `git clone https://github.com/DeathReaper0965/kata-number-convert-french.git`
2. Navigate to the repo: `cd kata`
3. Create a new python 3.11 environment using: `virtualenv kata-env` (This is helpful for separating the application's dependencies from system dependencies)
4. Activate the environment: `source kata-env/bin/activate`
5. Install all required dependencies: `pip install -r requirements.txt`

**TIP**: All the steps from 3-5 can also be done by just executing `source install.sh` from terminal. However, you still have to download `ffmeg` separately.

#### That's it, we're all done with the installation and all that's left is to start the app.

## Start the Application
To start the [Gradio](https://www.gradio.app/) app, just execute the below command from the root folder of the repo.<br>
`python app.py`
<br>

Once started, just head over to [http://localhost:8501/](http://localhost:7860/) in any browser of your choice to see the application in action 😄


## Executing Tests
UnitTest cases are added under the folder `tests/`. From root folder, execute the test cases using the following command:<br>
`python -m unittest discover tests "*.py" -v`

## Executing Tests