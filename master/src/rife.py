import os
import numpy as np
from downloadModels import modelsDir, modelsMap

from coloredPrints import red, green

if os.name == "nt":
    appdata = os.getenv("APPDATA")
    mainPath = os.path.join(appdata, "AtlasAta")

    if not os.path.exists(mainPath):
        os.makedirs(mainPath)

    framesDir = os.path.join(mainPath, "frames")
    tmp_framesDir = os.path.join(mainPath, "frames", "tmpFrames")
    out_framesDir = os.path.join(mainPath, "frames", "outFrames")

    if not os.path.exists(framesDir):
        os.makedirs(framesDir)
    if not os.path.exists(tmp_framesDir):
        os.makedirs(tmp_framesDir)
    if not os.path.exists(out_framesDir):
        os.makedirs(out_framesDir)

else:
    dirPath = os.path.dirname(__file__)
    framesDir = os.path.join(dirPath, "frames")
    tmp_framesDir = os.path.join(dirPath, "frames", "tmpFrames")
    out_framesDir = os.path.join(dirPath, "frames", "outFrames")


class RIFE:
    def __init__(
        self,
        model: str,
        duration: float,
        frames: float,
        fps: float,
        factor: int,
    ):
        self.model = model
        self.duration = duration
        self.frames = frames
        self.fps = fps
        self.factor = factor

        self.upFps = self.fps * self.factor
        self.upFrames = self.frames * self.factor
        self.upDuration = self.upFrames / self.upFps

    def run(self):

        fileList = os.listdir(tmp_framesDir)
        outList = []

        file1 = 1
        file2 = 2

        for file in fileList:

            outList = os.listdir(out_framesDir)
            if file not in outList:
                os.system(
                    command=rf'rife-ncnn.exe -i "{tmp_framesDir}" -o "{out_framesDir}" -n "{self.upFrames}" -s "0.1" -m "{self.model}" -f "%0d.png"'
                )
            else:
                file1 += 1
                file2 += 1
