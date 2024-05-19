import logging
from typing import Any
from utils.constants import FrenchStyle, UnitsFrenchForm, OutputType
import streamlit as st
from french_converter import FrenchConverter
from parsers import *

logger = logging.getLogger(__name__)


def convert_to_french(nums_str: str, french_style: str, output_type: str) -> Any:
    """
        Function that initiates the conversion of the given numerical number to its french form

        Parameters
        ----------
        nums_str: str
            A comma-separated string of the numbers passed through Gradio input field.
        french_style: str
            The type of french to use for conversion. See Enum `FrenchStyle` in `constants.py` file for more details.
        output_type: str
            The type of output desired by user after conversion. See Enum `OutputType` in `constants.py` file for more details.

        Returns
        -------
            A dictonary/list conversion of each `valid` value in the input. Based on the selected `output_type`.
            If any of the value is not a number, `None` is produced as its conversion.


        Limitations:
            1. Currently supports only the numerical part conversion. 
            2. Decimal part and Fractional numbers conversion will be added in the future.
        
    """

    print(f"Given Input, french-style and output-type: {nums_str}, {french_style}, {output_type}")
    logger.info("Extracting numbers from string, replacing rudimentary symbols and splitting")
    original_values = nums_str.replace("[", "").replace("]", "").replace('"', "").replace("'", "").split(",")
    nums_list = [int(_) if _.strip().isnumeric() else None for _ in original_values]

    french_converted_list = []
    french_converted_json = {}

    logger.info("Loop through the extracted numbers and convert them to french form!")
    for idx, num in enumerate(nums_list):
        if num is None or len(str(num)) > 12:
            french_converted_list.append(None)
            french_converted_json[original_values[idx]] = None
            continue

        if num == 0:
            converted_val = UnitsFrenchForm.ZERO.value
        else:
            fc_obj = FrenchConverter(num, french_style)
            converted_val = fc_obj.convert()
        
        french_converted_list.append(converted_val)
        french_converted_json[original_values[idx]] = converted_val

    print(f"Generated Output: {french_converted_json}\n")

    if output_type == OutputType.JSON.value:
        return french_converted_json
    
    return french_converted_list




def main():
    # Initializes the streamlit App
    st.title("Kata: Number to French Converter")

    french_style_options = [style.value for style in FrenchStyle]
    output_type_options = [type.value for type in OutputType]
    number_to_convert_list = [0, 1, 5, 10, 11, 15, 20, 21, 30, 35, 50, 51, 68, 70, 75, 99, 100, 101, 105, 111, 123, 168, 171, 175, 199, 200, 201, 555, 999, 1000, 1001, 1111, 1199, 1234, 1999, 2000, 2001, 2020, 2021, 2345, 9999, 10000, 11111, 12345, 123456, 654321, 999999]

    input_numbers_txt = st.text_input("Input List of Numbers (Comma Separated, as shown in placeholder)", placeholder="[0, 10]",value=number_to_convert_list)
    french_style_dropdown_txt = st.selectbox("Select a French Style",
                                             [FrenchStyle.FRANCE_FRENCH.value, FrenchStyle.BELGIUM_FRENCH.value], index=french_style_options.index(FrenchStyle.default()))
    output_type_dropdown_txt = st.selectbox("Desired Output Type", [OutputType.JSON.value, OutputType.LIST.value], index=output_type_options.index(OutputType.default()))

    if st.button("Convert to French Form"):
        french_output = convert_to_french(input_numbers_txt, french_style_dropdown_txt, output_type_dropdown_txt)

        st.write("French Form of the input number list:")
        st.write(french_output)


if __name__ == '__main__':
    main()
