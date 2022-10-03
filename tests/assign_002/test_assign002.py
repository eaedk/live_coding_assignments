# importation of the solution function to test
from src.assign_002.script import solution
import pandas as pd
import os

FILE_DIR = os.path.dirname(os.path.relpath(__file__))

def test_solution_True():
    """This is the test for the implemented solution passing
    valid inputs"""

    valid_inputs = [
        {"filepath":"src/assets/data_to_process.csv"},
    ]
    
    expected_df = [
        pd.read_csv(os.path.join(FILE_DIR, "processed_data.csv")).sort_values(by=["email"]).reset_index(drop=True),
    ]

    outputs_df = []

    for (i, input) in enumerate(valid_inputs):
        outputs_df.append(
            solution(**input).sort_values(by=["email"]).reset_index(drop=True)[expected_df[i].columns.tolist()]
            )
    
    expected_outputs = [ True for i in range(len(expected_df))]
    outputs = []

    for (out, expected) in zip(outputs,expected_outputs):
        try:
            pd.testing.assert_frame_equal(out, expected) 
            outputs.append(True)
        except: 
            outputs.append(False) 

    assert outputs == expected_outputs


def test_solution_False():
    """This is the test for the implemented solution passing
    valid inputs"""

    valid_inputs = [
        {"filepath":"src/assets/shuffled_data.csv"},
    ]
    
    expected_df = [
        pd.read_csv(os.path.join(FILE_DIR, "processed_data.csv")).sort_values(by=["email"]).reset_index(drop=True),
    ]

    outputs_df = []

    for (i, input) in enumerate(valid_inputs):
        outputs_df.append(
            solution(**input).sort_values(by=["email"]).reset_index(drop=True)[expected_df[i].columns.tolist()]
            )
    
    expected_outputs = [ False for i in range(len(expected_df))]
    outputs = []

    for (out, expected) in zip(outputs,expected_outputs):
        try:
            pd.testing.assert_frame_equal(out, expected) 
            outputs.append(True)
        except: 
            outputs.append(False) 

    assert outputs == expected_outputs