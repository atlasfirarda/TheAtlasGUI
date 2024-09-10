import cv2
import sys
import os
import threading
import numpy as np
import logging
import shutil

from coloredPrints import red, green, yellow

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

# EXTRACT: rf'ffmpeg.exe -i "{self.input}" "{framesDir}\tmp_frames\%08d.png" -y -preset {self.preset}'
# MERGE: rf'ffmpeg.exe -r "{self.fps}" -i "{framesDir}\out_frames\%0d.png" -i "{self.input}" -c:v libx264 -preset {self.preset} -qp 0 -r {self.fps} "{self.output}.{self.ext}"'


class FFMPEG:

    def __init__(self, filePath: str):

        if '"' in filePath:
            self.filePath = filePath.replace('"', "")
        else:
            self.filePath = filePath

        capture = cv2.VideoCapture(self.filePath)
        try:
            self.frames = capture.get(cv2.CAP_PROP_FRAME_COUNT)
            self.fps = capture.get(cv2.CAP_PROP_FPS)
            self.name = os.path.splitext(os.path.basename(self.filePath))[0]
        except FileNotFoundError:
            self.frames = 0
            toLog = f"the {self.filePath} is can't be able to get video frames."
            logging.info(toLog)
            self.fps = 0
            toLog = f"the {self.filePath} is can't be able to get video fps."
            logging.info(toLog)

        try:
            self.duration = self.frames / self.fps
        except ZeroDivisionError:
            toLog = f"the {self.filePath} is can't be able to get video duration."
            logging.info(toLog)

            self.duration = 0.0

    def extract(self):

        tmpFileList = os.listdir(tmp_framesDir)

        if not len(tmpFileList) == 0:
            for file in tmpFileList:
                os.remove(os.path.join(tmp_framesDir, file))

        os.system(
            command=rf'ffmpeg.exe -i "{self.filePath}" "{tmp_framesDir}\%0d.png" -preset veryslow'
        )

    def merge(self):

        os.system(
            command=rf'ffmpeg.exe -r "{self.fps}" -i "{tmp_framesDir}\%0d.png" -i "{self.filePath}" -c:v libx264 -preset veryslow -qp 0 -r {self.fps} "{self.name}.mp4"'
        )

    def extractInfo(self):

        videoFrames = self.frames
        videoFps = self.fps
        videoDuration = self.duration
        videoName = self.name

        return videoFrames, videoFps, videoDuration, videoName
