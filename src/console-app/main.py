# This is the start of something cool

import os
from getpass import getpass
import argparse
#from ultralytics import YOLO

def parse_args():
    '''Parse input arguments'''

    parser = argparse.ArgumentParser("beyond-goal")
    parser.add_argument("--input_file", type=str, help="Name of the input file")
    parser.add_argument("--scale_percentage", type=int, help="Scale percentage of the output video")
    parser.add_argument("--action_type", type=int, help="Action Type 1. Track Players 2. Player Segmentation 3. Vehicle In and Out 4. Vehicle Number plate")
    
    input_args = parser.parse_args()

    return input_args

def main(args):
    print("PROGRAM START--------------------------------")
    os.environ['KAGGLE_USERNAME'] = getpass('anantheswarg881')
    os.environ['KAGGLE_KEY'] = getpass('7d088e57615257d28d5e4f5a5991b11b')
    HOME = os.getcwd()
    print(HOME)

if __name__ == "__main__":
    args = parse_args()
    main(args)