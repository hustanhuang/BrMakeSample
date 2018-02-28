#!/usr/local/bin/python3

# replace this file with bash script

import os
import sys

UNITY_PATH = "/Applications/Unity/Unity.app/Contents/MacOS/Unity"


def unity_build(platform):
    params = [
        "-quit",
        "-batchmode",
        "-logFile /dev/stdout", # add option
        "-projectPath " + os.getcwd(),
        "-executeMethod BrMake.Builder.Build" + platform
    ]

    os.system(UNITY_PATH + " " + " ".join(params))


if __name__ == "__main__":
    if sys.platform == "darwin":
        unity_build("Ios")
    else:
        print("currently only available under macOS ")
