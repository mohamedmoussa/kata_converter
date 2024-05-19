#!/bin/bash
virtualenv kata-env
source "kata-env/bin/activate"
pip install -r requirements.txt
streamlit run app.py