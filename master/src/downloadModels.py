import os
import requests
import logging
from alive_progress import alive_bar
from coloredPrints import yellow, red, green

if os.name == "nt":
    appdata = os.getenv("APPDATA")
    mainPath = os.path.join(appdata, "AtlasAta")

    if not os.path.exists(mainPath):
        os.makedirs(mainPath)

    modelsDir = os.path.join(mainPath, "models")

else:
    dirPath = os.path.dirname(__file__)
    modelsDir = os.path.join(dirPath, "models")

TAGURL = "https://github.com/atlasfirarda/TheAtlasGUI/releases/download/tag-models/"


def modelsList() -> list[str]:
    return [
        "wtp-uds-esrgan",
        "bubble",
        "cugan",
        "anime-sharp",
        "rife20",
        "rife40",
        "rife417",
        "rife418",
        "rife419",
        "rife420",
        "rife421",
    ]


def modelsMap(
    model: str = "anime-sharp",
    upscaleFactor: int = 2,
    modelType="pth",
    half: bool = True,
    ensemble: bool = False,
) -> str:

    match model:
        case "anime-sharp" | "sharp" | "animesharp":
            if modelType == "pth":
                return "4x-AnimeSharp.pth"
            else:
                if not modelType == "ncnn":
                    if half:
                        return "4x-AnimeSharp_fp16.onnx"
                    else:
                        return "4x-AnimeSharp_fp32.onnx"
        case "wtp-uds-esrgan" | "uds-esrgan" | "wtp-uds":
            if modelType == "pth":
                return "4x-WTP-UDS-Esrgan.pth"
            elif modelType == "ncnn":
                if half:
                    return "4x-WTP-UDS-Esrgan_fp16-ncnn.rar"
                else:
                    return "4x-WTP-UDS-Esrgan_fp32-ncnn.rar"
            else:
                if half:
                    return "4x-WTP-UDS-Esrgan_fp16.onnx"
                else:
                    return "4x-WTP-UDS-Esrgan_fp32.onnx"
        case "bubble" | "anime-bubble":
            if modelType == "pth":
                return "2x-Bubble-AnimeScale-Compact-v1.pth"
            else:
                if not modelType == "ncnn":
                    if half:
                        return "2x-Bubble-AnimeScale-Compact-v1_fp16.onnx"
                    else:
                        return "2x-Bubble-AnimeScale-Compact-v1_fp32.onnx"
        case "cugan" | "cugan-pro":
            if modelType == "pth":
                return "cugan_pro-denoise3x-up2x.pth"
            else:
                if not modelType == "ncnn":
                    if half:
                        return "cugan_pro-denoise3x-up2x_fp16.onnx"
                    else:
                        return "cugan_pro-denoise3x-up2x_fp32.onnx"
        case "rife417":
            if modelType == "ncnn":
                if not ensemble:
                    if half:
                        return "rife-v4.17_lite_ensembleFalse.rar"
                    else:
                        return "rife-v4.17_ensembleFalse.rar"
                else:
                    if half:
                        return "rife-v4.17_lite_ensembleTrue.rar"
                    else:
                        return "rife-v4.17_ensembleTrue.rar"
        case "rife418":
            if modelType == "ncnn":
                if not ensemble:
                    return "rife-v4.18_ensembleFalse.rar"
                else:
                    return "rife-v4.18_ensembleTrue.rar"
        case "rife419":
            if modelType == "ncnn":
                if not ensemble:
                    return "rife-v4.19_beta_ensembleFalse.rar"
                else:
                    return "rife-v4.19_beta_ensembleTrue.rar"
        case "rife420":
            if modelType == "ncnn":
                if not ensemble:
                    return "rife-v4.20_ensembleFalse.rar"
                else:
                    return "rife-v4.20_ensembleTrue.rar"
        case "rife421":
            if modelType == "ncnn":
                if not ensemble:
                    return "rife-v4.21_ensembleFalse.rar"
        case "rife422":
            if modelType == "ncnn":
                if not ensemble:
                    if half:
                        return "rife-v4.22_lite_ensembleFalse.rar"
                    else:
                        return "rife-v4.22_ensembleFalse.rar"
        case "rife424":
            if modelType == "ncnn":
                if not ensemble:
                    return "rife-v4.24_ensembleFalse.rar"
                else:
                    return "rife-v4.24_ensembleTrue.rar"
        case "rife40":
            if modelType == "ncnn":
                if ensemble:
                    if half:
                        return "rife-v4_ensembleTrue_fastTrue.rar"
                    else:
                        return "rife-v4_ensembleTrue_fastFalse.rar"
        case _:
            if modelType == "pth":
                print(
                    yellow("WARNING:"),
                    red(f"the {model} CUDA model is not foundable.."),
                    yellow("Please use, certain CUDA models in the list."),
                )

                toLog = f"the {model} CUDA model is not foundable.."
                logging.info(toLog)

                return "no-cuda-model"
            elif modelType == "ncnn":
                print(
                    yellow("WARNING:"),
                    red(f"the {model} NCNN model is not foundable.."),
                    yellow("Please use, certain NCNN models in the list."),
                )

                toLog = f"the {model} NCNN model is not foundable.."
                logging.info(toLog)

                return "no-ncnn-model"
            elif modelType == "onnx":
                print(
                    yellow("WARNING:"),
                    red(f"the {model} ONNX model is not foundable.."),
                    yellow("Please use, certain ONNX models in the list."),
                )

                toLog = f"the {model} ONNX model is not foundable.."
                logging.info(toLog)

                return "no-onnx-model"


def downloadModels(
    model: str,
    filename: str,
    download_url: str,
    folderPath: str,
):

    response = requests.get(download_url, stream=True)

    try:
        total_size_in_bytes = int(response.headers.get("content-length", 0))
        total_size_in_megabytes = total_size_in_bytes / (1024 * 1024)
    except Exception:
        total_size_in_megabytes = 0

    with alive_bar(
        int(total_size_in_megabytes + 1),
        bar="filling",
        unit="MB",
        spinner=False,
        enrich_print=False,
        receipt=True,
        monitor=True,
        elapsed=True,
        stats=True,
        dual_line=True,
        force_tty=True,
        refresh_secs=0,
    ) as bar:
        with open(os.path.join(folderPath, filename), "wb") as file:
            for data in response.iter_content(chunk_size=1024 * 1024):
                file.write(data)
                bar(int(len(data) / (1024 * 1024)))

    if filename.endswith(".pth"):
        if not os.path.exists(os.path.join(folderPath, "pth")):
            os.makedirs(os.path.join(folderPath, "pth"))
        os.rename(
            os.path.join(folderPath, filename),
            os.path.join(folderPath, "pth", filename),
        )

        downloadPath = os.path.join(folderPath, "pth")

    elif filename.endswith(".onnx"):
        if not os.path.exists(os.path.join(folderPath, "onnx")):
            os.makedirs(os.path.join(folderPath, "onnx"))
        os.rename(
            os.path.join(folderPath, filename),
            os.path.join(folderPath, "onnx", filename),
        )

        downloadPath = os.path.join(folderPath, "onnx")

    elif filename.endswith(".rar"):
        if not os.path.exists(os.path.join(folderPath)):
            os.makedirs(os.path.join(folderPath))

        downloadPath = os.path.join(folderPath)

    if filename.endswith(".rar"):
        import rarfile

        file = rarfile.RarFile(os.path.join(folderPath, filename))
        file.extractall(path=os.path.join(folderPath))
        os.remove(os.path.join(folderPath, filename))

    print(
        green("SUCCESS"),
        yellow(filename),
        green("model is downloaded to"),
        yellow(downloadPath),
    )
    toLog = f"{filename} is downloaded to {downloadPath}"
    logging.info(toLog)

    # if filename.endswith(".pth"):
    #     return os.path.join(folderPath, "pth", filename) # NO NEED IT
    # elif filename.endswith(".onnx"):
    #     return os.path.join(folderPath, "onnx", filename) # NO NEED IT
    # elif filename.endswith(".rar"):
    #     return os.path.join(folderPath, "ncnn", filename) # NO NEED IT

    return os.path.join(folderPath, filename)


def download(
    model: str = None,
    upscaleFactor: int = 2,
    modelType: str = "pth",
    half: bool = True,
    ensemble: bool = False,
) -> str:

    os.makedirs(modelsDir, exist_ok=True)

    filename = modelsMap(model=model, modelType=modelType, half=half, ensemble=ensemble)

    folderPath = os.path.join(modelsDir, filename[:-4])
    os.makedirs(folderPath, exist_ok=True)

    downloadUrl = f"{TAGURL}{filename}"

    return downloadModels(model, filename, downloadUrl, folderPath)
