import os
import inquirer
import inquirer.prompt
import shutil

from coloredPrints import green, red, green
from downloadModels import modelsDir, modelsMap, download
from ffmpeg import FFMPEG, framesDir, tmp_framesDir, out_framesDir
from rife import RIFE


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
                    "Rife-V4.0",
                    "Rife-V4.17",
                    "Rife-V4.18",
                    "Rife-V4.19",
                    "Rife-V4.20",
                    "Rife-V4.21",
                    "Rife-V4.22",
                    "Rife-V4.24",
                ],
            )
        ]

        intAnswers = inquirer.prompt(interpolateOptions)
        intSel = intAnswers["intSel"]
        os.system(command="cls")
        Initialize("", "", "", "")

        if intSel == "Rife-V4.0":

            rifeModel = "rife40"

            rifeOptions = [
                inquirer.List(
                    "rifeSel",
                    message="Which RIFE-V4.0 model do you prefer?",
                    choices=["Ensemble", "Ensemble-Lite"],
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

        elif intSel == "Rife-V4.17":

            rifeModel = "rife417"

            rifeOptions = [
                inquirer.List(
                    "rifeSel",
                    message="Which RIFE-V4.17 model do you prefer?",
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

        elif intSel == "Rife-V4.18":

            rifeModel = "rife418"

            rifeOptions = [
                inquirer.List(
                    "rifeSel",
                    message="Which RIFE-V4.18 model do you prefer?",
                    choices=["Normal", "Ensemble"],
                )
            ]

            rifeAnswers = inquirer.prompt(rifeOptions)
            rifeSel = rifeAnswers["rifeSel"]

            if rifeSel == "Ensemble":

                rifeEnsemble = True
        elif intSel == "Rife-V4.19":

            rifeModel = "rife419"

            rifeOptions = [
                inquirer.List(
                    "rifeSel",
                    message="Which RIFE-V4.19 model do you prefer?",
                    choices=["Normal", "Ensemble"],
                )
            ]

            rifeAnswers = inquirer.prompt(rifeOptions)
            rifeSel = rifeAnswers["rifeSel"]

            if rifeSel == "Ensemble":
                rifeEnsemble = True

        elif intSel == "Rife-V4.20":

            rifeModel = "rife420"

            rifeOptions = [
                inquirer.List(
                    "rifeSel",
                    message="Which RIFE-V4.20 model do you prefer?",
                    choices=["Normal", "Ensemble"],
                )
            ]

            rifeAnswers = inquirer.prompt(rifeOptions)
            rifeSel = rifeAnswers["rifeSel"]

            if rifeSel == "Ensemble":

                rifeEnsemble = True
        elif intSel == "Rife-V4.21":

            rifeModel = "rife421"

            rifeOptions = [
                inquirer.List(
                    "rifeSel",
                    message="Which RIFE-V4.21 model do you prefer?",
                    choices=["Normal"],
                )
            ]

            rifeAnswers = inquirer.prompt(rifeOptions)
        elif intSel == "Rife-V4.22":

            rifeModel = "rife422"

            rifeOptions = [
                inquirer.List(
                    "rifeSel",
                    message="Which RIFE-V4.22 model do you prefer?",
                    choices=["Normal", "Lite"],
                )
            ]

            rifeAnswers = inquirer.prompt(rifeOptions)
            rifeSel = rifeAnswers["rifeSel"]

            if rifeSel == "Lite":
                rifeHalf = True
        elif intSel == "Rife-V4.24":

            rifeModel = "rife424"

            rifeOptions = [
                inquirer.List(
                    "rifeSel",
                    message="Which RIFE-V4.24 model do you prefer?",
                    choices=["Normal", "Ensemble"],
                )
            ]

            rifeAnswers = inquirer.prompt(rifeOptions)
            rifeSel = rifeAnswers["rifeSel"]

            if rifeSel == "Ensemble":
                rifeEnsemble = True

        os.system(command="cls")
        Initialize("", "", "", "")

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
        Initialize("", "", "", "")

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

        folderPath = os.path.join(modelsDir, model)

        if model in ["no-model", "no-cuda-model", "no-onnx-model", "no-ncnn-model"]:
            exit(404)

        if model.endswith(".rar"):
            model = model[:-4]
            modelType = "ncnn"

        if not os.path.exists(os.path.join(modelsDir, model)):
            initialize.downloadModel(model)

            ffmpeg = FFMPEG(filePath=fileAnswer["filePath"], factor=intFactor)

            videoFrames = ffmpeg.extractInfo()[0]
            videoFps = ffmpeg.extractInfo()[1]
            videoDuration = ffmpeg.extractInfo()[2]
            videoName = ffmpeg.extractInfo()[3]

            rife = RIFE(
                rf"{os.path.join(modelsDir, model)}",
                videoDuration,
                videoFrames,
                videoFps,
                factor=intFactor,
            )

            ffmpeg.extract()
            rife.run()
            ffmpeg.merge()
            shutil.rmtree(os.path.join(framesDir))

        else:
            ##### FFMPEG RUNS #####

            ffmpeg = FFMPEG(filePath=fileAnswer["filePath"], factor=intFactor)

            if not os.path.exists(framesDir):
                os.makedirs(framesDir)
            if not os.path.exists(tmp_framesDir):
                os.makedirs(tmp_framesDir)
            if not os.path.exists(out_framesDir):
                os.makedirs(out_framesDir)

            videoFrames = ffmpeg.extractInfo()[0]
            videoFps = ffmpeg.extractInfo()[1]
            videoDuration = ffmpeg.extractInfo()[2]
            videoName = ffmpeg.extractInfo()[3]

            rife = RIFE(
                rf"{os.path.join(modelsDir, model)}",
                videoDuration,
                videoFrames,
                videoFps,
                factor=intFactor,
            )

            ffmpeg.extract()
            rife.run()
            ffmpeg.merge()
            shutil.rmtree(os.path.join(framesDir))
