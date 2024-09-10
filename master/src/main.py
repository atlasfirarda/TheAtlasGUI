import subprocess
import os
import sys
import inquirer
import inquirer.prompt
import cv2
import logging

from coloredPrints import green, red, green
from downloadModels import modelsDir, modelsMap, download
from ffmpeg import FFMPEG
from rife import RIFE

# from ffmpeg import FFMPEG
# from rife import RIFE
# import torch


class Initialize:
    def __init__(self, model: str, modelType: str, half: bool, ensemble: bool) -> None:
        self.logo = rf"""
 /{green("$$$$$$$$")} /{green("$$")}                        /{green("$$$$$$")}    /{green("$$")}     /{green("$$")}                      /{green("$$$$$$")}  /{green("$$")}   /{green("$$")} /{green("$$$$$$")}
|__  {green("$$")}__/| {green("$$")}                       /{green("$$")}__  {green("$$")}  | {green("$$")}    | {green("$$")}                     /{green("$$")}__  {green("$$")}| {green("$$")}  | {green("$$")}|_  {green("$$")}_/
   | {green("$$")}   | {green("$$$$$$$")}   /{green("$$$$$$")}       | {green("$$")}  \ {green("$$")} /{green("$$$$$$")}  | {green("$$")}  /{green("$$$$$$")}   /{green("$$$$$$$")}| {green("$$")}  \__/| {green("$$")}  | {green("$$")}  | {green("$$")}
   | {green("$$")}   | {green("$$")}__  {green("$$")} /{green("$$")}__  {green("$$")}      | {green("$$$$$$$$")}|_  {green("$$")}_/  | {green("$$")} |____  {green("$$")} /{green("$$")}_____/| {green("$$")} /{green("$$$$")}| {green("$$")}  | {green("$$")}  | {green("$$")}
   | {green("$$")}   | {green("$$")}  \ {green("$$")}| {green("$$$$$$$$")}      | {green("$$")}__  {green("$$")}  | {green("$$")}    | {green("$$")}  /{green("$$$$$$$")}|  {green("$$$$$$")} | {green("$$")}|_  {green("$$")}| {green("$$")}  | {green("$$")}  | {green("$$")}
   | {green("$$")}   | {green("$$")}  | {green("$$")}| {green("$$")}_____/      | {green("$$")}  | {green("$$")}  | {green("$$")} /{green("$$")}| {green("$$")} /{green("$$")}__  {green("$$")} \____  {green("$$")}| {green("$$")}  \ {green("$$")}| {green("$$")}  | {green("$$")}  | {green("$$")}
   | {green("$$")}   | {green("$$")}  | {green("$$")}|  {green("$$$$$$$")}      | {green("$$")}  | {green("$$")}  |  {green("$$$$")}/| {green("$$")}|  {green("$$$$$$$")} /{green("$$$$$$$")}/|  {green("$$$$$$")}/|  {green("$$$$$$")}/ /{green("$$$$$$")}
   |__/   |__/  |__/ \_______/      |__/  |__/   \___/  |__/ \_______/|_______/  \______/  \______/ |______\ 
"""
        print(self.logo + "\n")

        self.model = model
        self.modelType = modelType
        self.half = half
        self.ensemble = ensemble

    def getModel(self) -> str:

        return modelsMap(
            model=self.model,
            modelType=self.modelType,
            half=self.half,
            ensemble=self.ensemble,
        )

    def downloadModel(self, model: str):

        download(
            model=self.model,
            modelType=self.modelType,
            half=self.half,
            ensemble=self.ensemble,
        )


if __name__ == "__main__":

    os.system(command="cls")

    Initialize("", "", "", "")

    # initialize = Initialize(
    #     model="rife418", modelType="ncnn", half=False, ensemble=True
    # )

    # model = initialize.getModel()

    # if model in ["no-model", "no-cuda-model", "no-onnx-model", "no-ncnn-model"]:
    #     exit(404)

    # if model.endswith(".pth"):
    #     model = model[:-4]
    #     modelType = "pth"
    # elif model.endswith(".onnx"):
    #     model = model[:-5]
    #     modelType = "onnx"
    # elif model.endswith(".rar"):
    #     model = model[:-4]
    #     modelType = "ncnn"

    # if not os.path.exists(os.path.join(modelsDir, modelType, model)):
    #     initialize.downloadModel(model)
    selOptions = [
        inquirer.List(
            "sel",
            message="Choose one of the GUIs",
            choices=[
                "Interpolate GUI",
                "Upscale GUI",
                "Youtube GUI",
                "Spotify GUI",
            ],
        ),
    ]
    selAnswers = inquirer.prompt(selOptions)
    sel = selAnswers["sel"]
    os.system(command="cls")
    Initialize("", "", "", "")

    if sel == "Interpolate GUI":

        file = "no-file"
        rifeModel = "rife418"
        rifeModelType = "ncnn"
        rifeEnsemble = False
        rifeHalf = False

        interpolateOptions = [
            inquirer.List(
                "intSel",
                message="Which model do you prefer to use interpolate?",
                choices=[
                    "Rife-2.0",
                    "Rife-4.0",
                    "Rife-4.17",
                    "Rife-4.18",
                    "Rife-4.19",
                    "Rife-4.20",
                    "Rife-4.21",
                ],
            )
        ]

        intAnswers = inquirer.prompt(interpolateOptions)
        intSel = intAnswers["intSel"]
        os.system(command="cls")
        Initialize("", "", "", "")

        if intSel == "Rife-2.0":

            rifeModel = "rife20"

            rifeOptions = [
                inquirer.List(
                    "rifeSel",
                    message="Which RIFE-2.0 model do you prefer?",
                    choices=["Normal"],
                )
            ]

            rifeAnswers = inquirer.prompt(rifeOptions)
            rifeSel = rifeAnswers["rifeSel"]

        elif intSel == "Rife-4.0":

            rifeModel = "rife40"

            rifeOptions = [
                inquirer.List(
                    "rifeSel",
                    message="Which RIFE-4.0 model do you prefer?",
                    choices=["Normal", "Ensemble", "Ensemble-Fast"],
                )
            ]

            rifeAnswers = inquirer.prompt(rifeOptions)
            rifeSel = rifeAnswers["rifeSel"]

            if rifeSel == "Ensemble":
                rifeEnsemble = True
            elif rifeSel == "Ensemble-Fast":
                rifeEnsemble = True
                rifeHalf = True

        elif intSel == "Rife-4.17":

            rifeModel = "rife417"

            rifeOptions = [
                inquirer.List(
                    "rifeSel",
                    message="Which RIFE-4.17 model do you prefer?",
                    choices=["Normal", "Lite", "Ensemble", "Ensemble-Lite"],
                )
            ]

            rifeAnswers = inquirer.prompt(rifeOptions)
            rifeSel = rifeAnswers["rifeSel"]

            if rifeSel == "Lite":
                rifeHalf = True
            elif rifeSel == "Ensemble":
                rifeEnsemble = True
            elif rifeSel == "Ensemble-Lite":
                rifeEnsemble = True
                rifeHalf = True
        elif intSel == "Rife-4.18":

            rifeModel = "rife418"

            rifeOptions = [
                inquirer.List(
                    "rifeSel",
                    message="Which RIFE-4.18 model do you prefer?",
                    choices=["Normal", "Ensemble"],
                )
            ]

            rifeAnswers = inquirer.prompt(rifeOptions)
            rifeSel = rifeAnswers["rifeSel"]

            if rifeSel == "Ensemble":

                rifeEnsemble = True
        elif intSel == "Rife-4.19":

            rifeModel = "rife419"

            rifeOptions = [
                inquirer.List(
                    "rifeSel",
                    message="Which RIFE-4.19 model do you prefer?",
                    choices=["Normal", "Ensemble"],
                )
            ]

            rifeAnswers = inquirer.prompt(rifeOptions)
            rifeSel = rifeAnswers["rifeSel"]

            if rifeSel == "Ensemble":
                rifeEnsemble = True

        elif intSel == "Rife-4.20":

            rifeModel = "rife420"

            rifeOptions = [
                inquirer.List(
                    "rifeSel",
                    message="Which RIFE-4.20 model do you prefer?",
                    choices=["Normal", "Ensemble"],
                )
            ]

            rifeAnswers = inquirer.prompt(rifeOptions)
            rifeSel = rifeAnswers["rifeSel"]

            if rifeSel == "Ensemble":

                rifeEnsemble = True
        elif intSel == "Rife-4.21":

            rifeModel = "rife421"

            rifeOptions = [
                inquirer.List(
                    "rifeSel",
                    message="Which RIFE-4.21 model do you prefer?",
                    choices=["Normal"],
                )
            ]

            rifeAnswers = inquirer.prompt(rifeOptions)

        os.system(command="cls")

        interpolateFOptions = [
            inquirer.List(
                "intFSel",
                message="Which multiplication of interpolation do you choose?",
                choices=[
                    "2x",
                    "3x",
                    "4x",
                    "5x",
                    "6x",
                    "7x",
                    "8x",
                ],
            )
        ]

        intFAnswers = inquirer.prompt(interpolateFOptions)
        intFSel = intFAnswers["intFSel"]
        os.system(command="cls")
        Initialize("", "", "", "")

        if intFSel == "2x":
            intFactor = 2
        elif intFSel == "3x":
            intFactor = 3
        elif intFSel == "4x":
            intFactor = 4
        elif intFSel == "5x":
            intFactor = 5
        elif intFSel == "6x":
            intFactor = 6
        elif intFSel == "7x":
            intFactor = 7
        elif intFSel == "8x":
            intFactor = 8

        os.system(command="cls")

        if file == "no-file":

            fileOptions = [
                inquirer.Text("filePath", message="Please, Drag & Drop your input file")
            ]
            fileAnswer = inquirer.prompt(fileOptions)

        os.system(command="cls")

        initialize = Initialize(
            model=f"{rifeModel}",
            modelType=f"{rifeModelType}",
            half=rifeHalf,
            ensemble=rifeEnsemble,
        )

        model = initialize.getModel()

        if "rife" in model:
            model = model[:-4]

        if "-ensemble-lite" in model or "-ensemble-fast" in model:
            folderPath = os.path.join(modelsDir, model[:-14])
        elif "-lite" in model or "-fast" in model:
            folderPath = os.path.join(modelsDir, model[:-5])
        elif "-ensemble" in model:
            folderPath = os.path.join(modelsDir, model[:-9])
        elif (
            "-ensemble" not in model
            or "-ensemble-fast" not in model
            or "-lite" not in model
            or "-fast" not in model
            and "rife" in model
        ):
            folderPath = os.path.join(modelsDir, model)

        if "-ensemble-lite" in model or "-ensemble-fast" in model:
            modelPath = os.path.join(folderPath, "ncnn", "ensemble-fast")
        elif "-lite" in model or "-fast" in model:
            modelPath = os.path.join(folderPath, "ncnn", "fast")
        elif "-ensemble" in model:
            modelPath = os.path.join(folderPath, "ncnn", "ensemble")
        elif (
            "-ensemble" not in model
            or "-ensemble-fast" not in model
            or "-lite" not in model
            or "-fast" not in model
            and "rife" in model
        ):
            modelPath = os.path.join(folderPath, "ncnn")

        model = initialize.getModel()

        if model in ["no-model", "no-cuda-model", "no-onnx-model", "no-ncnn-model"]:
            exit(404)

        if model.endswith(".rar"):
            model = model[:-4]
            modelType = "ncnn"

        if not os.path.exists(os.path.join(modelPath)):
            initialize.downloadModel(model)

            ffmpeg = FFMPEG(filePath=fileAnswer["filePath"])

            videoFrames = ffmpeg.extractInfo()[0]
            videoFps = ffmpeg.extractInfo()[1]
            videoDuration = ffmpeg.extractInfo()[2]
            videoName = ffmpeg.extractInfo()[3]

            rife = RIFE(
                rf"{os.path.join(modelPath)}",
                videoDuration,
                videoFrames,
                videoFps,
                factor=intFactor,
            )

            ffmpeg.extract()
            rife.run()
            ffmpeg.merge()

        else:
            ##### FFMPEG RUNS #####

            ffmpeg = FFMPEG(filePath=fileAnswer["filePath"])

            videoFrames = ffmpeg.extractInfo()[0]
            videoFps = ffmpeg.extractInfo()[1]
            videoDuration = ffmpeg.extractInfo()[2]
            videoName = ffmpeg.extractInfo()[3]

            rife = RIFE(
                rf"{os.path.join(modelPath)}",
                videoDuration,
                videoFrames,
                videoFps,
                factor=intFactor,
            )

            ffmpeg.extract()
            rife.run()
            ffmpeg.merge()
