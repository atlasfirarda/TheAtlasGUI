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
                else:
                    print(
                        yellow("WARNING:"),
                        red("the ANIMESHARP model is not supported by NCNN.."),
                        yellow("Please use, CUDA version anyway."),
                    )
                    return "no-model"
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
                else:
                    print(
                        yellow("WARNING:"),
                        red("the BUBBLE model is not supported by NCNN.."),
                        yellow("Please use, CUDA version anyway."),
                    )
                    return "no-model"
        case "cugan" | "cugan-pro":
            if modelType == "pth":
                return "cugan_pro-denoise3x-up2x.pth"
            else:
                if not modelType == "ncnn":
                    if half:
                        return "cugan_pro-denoise3x-up2x_fp16.onnx"
                    else:
                        return "cugan_pro-denoise3x-up2x_fp32.onnx"
                else:
                    print(
                        yellow("WARNING:"),
                        red("the CUGAN model is not supported by NCNN.."),
                        yellow("Please use, CUDA version anyway."),
                    )
                    return "no-model"
        case "rife417":
            if modelType == "ncnn":
                if not ensemble:
                    if half:
                        return "rife417-lite.rar"
                    else:
                        return "rife417.rar"
                else:
                    if half:
                        return "rife417-ensemble-lite.rar"
                    else:
                        return "rife417-ensemble.rar"
            else:
                print(
                    yellow("WARNING:"),
                    red("the RIFE417 model is currently not supported by CUDA.."),
                    yellow("Please use, NCNN version anyway."),
                )
                return "no-model"
        case "rife418":
            if modelType == "ncnn":
                if not ensemble:
                    return "rife418.rar"
                else:
                    return "rife418-ensemble.rar"
            else:
                print(
                    yellow("WARNING:"),
                    red("the RIFE418 model is currently not supported by CUDA.."),
                    yellow("Please use, NCNN version anyway."),
                )
                return "no-model"
        case "rife419":
            if modelType == "ncnn":
                if not ensemble:
                    return "rife419.rar"
                else:
                    return "rife419-ensemble.rar"
            else:
                print(
                    yellow("WARNING:"),
                    red("the RIFE419 model is currently not supported by CUDA.."),
                    yellow("Please use, NCNN version anyway."),
                )
                return "no-model"
        case "rife420":
            if modelType == "ncnn":
                if not ensemble:
                    return "rife420.rar"
                else:
                    return "rife420-ensemble.rar"
            else:
                print(
                    yellow("WARNING:"),
                    red("the RIFE420 model is currently not supported by CUDA.."),
                    yellow("Please use, NCNN version anyway."),
                )
                return "no-model"
        case "rife421":
            if modelType == "ncnn":
                if not ensemble:
                    return "rife421.rar"
                else:
                    print(
                        yellow("WARNING:"),
                        red("the RIFE421 model is not supported by ENSEMBLE anymore.."),
                    )
                return "no-model"
            else:
                print(
                    yellow("WARNING:"),
                    red("the RIFE421 model is currently not supported by CUDA.."),
                    yellow("Please use, NCNN version anyway."),
                )
                return "no-model"
        case "rife20":
            if modelType == "ncnn":
                if not ensemble:
                    return "rife20.rar"
                else:
                    print(
                        yellow("WARNING:"),
                        red("the RIFE20 model is not supported by ENSEMBLE.."),
                    )
                return "no-model"
            else:
                print(
                    yellow("WARNING:"),
                    red("the RIFE20 model is currently not supported by CUDA.."),
                    yellow("Please use, NCNN version anyway."),
                )
                return "no-model"
        case "rife40":
            if modelType == "ncnn":
                if not ensemble:
                    if half:
                        return "rife40-fast.rar"
                    else:
                        print(
                            yellow("WARNING:"),
                            red("the RIFE40 model is not supported by FULL VERSION.."),
                            yellow("Please use, LITE version anyway."),
                        )
                        return "no-model"
                else:
                    if half:
                        return "rife40-ensemble-fast.rar"
                    else:
                        return "rife40-ensemble.rar"
            else:
                print(
                    yellow("WARNING:"),
                    red("the RIFE40 model is currently not supported by CUDA.."),
                    yellow("Please use, NCNN version anyway."),
                )
                return "no-model"
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
        if not os.path.exists(os.path.join(folderPath, "ncnn")):
            os.makedirs(os.path.join(folderPath, "ncnn"))

        if "-ensemble-lite" in filename or "-ensemble-fast" in filename:
            if not os.path.exists(os.path.join(folderPath, "ncnn", "ensemble-fast")):
                os.makedirs(os.path.join(folderPath, "ncnn", "ensemble-fast"))
        elif "-lite" in filename or "-fast" in filename:
            if not os.path.exists(os.path.join(folderPath, "ncnn", "fast")):
                os.makedirs(os.path.join(folderPath, "ncnn", "fast"))
        elif "-ensemble" in filename:
            if not os.path.exists(os.path.join(folderPath, "ncnn", "ensemble")):
                os.makedirs(os.path.join(folderPath, "ncnn", "ensemble"))

        if "-ensemble-lite" in filename or "-ensemble-fast" in filename:
            os.rename(
                os.path.join(folderPath, filename),
                os.path.join(folderPath, "ncnn", "ensemble-fast", filename),
            )
            downloadPath = os.path.join(folderPath, "ncnn", "ensemble-fast")
        elif "-lite" in filename or "-fast" in filename:
            os.rename(
                os.path.join(folderPath, filename),
                os.path.join(folderPath, "ncnn", "fast", filename),
            )
            downloadPath = os.path.join(folderPath, "ncnn", "fast")
        elif "-ensemble" in filename:
            os.rename(
                os.path.join(folderPath, filename),
                os.path.join(folderPath, "ncnn", "ensemble", filename),
            )
            downloadPath = os.path.join(folderPath, "ncnn", "ensemble")
        else:
            os.rename(
                os.path.join(folderPath, filename),
                os.path.join(folderPath, "ncnn", filename),
            )
            downloadPath = os.path.join(folderPath, "ncnn")

    if filename.endswith(".rar"):
        import rarfile

        if "-ensemble-lite" in filename or "-ensemble-fast" in filename:
            file = rarfile.RarFile(
                os.path.join(folderPath, "ncnn", "ensemble-fast", filename)
            )
            file.extractall(path=os.path.join(folderPath, "ncnn", "ensemble-fast"))
            os.remove(os.path.join(folderPath, "ncnn", "ensemble-fast", filename))
        elif "-lite" in filename or "-fast" in filename:
            file = rarfile.RarFile(os.path.join(folderPath, "ncnn", "fast", filename))
            file.extractall(path=os.path.join(folderPath, "ncnn", "fast"))
            os.remove(os.path.join(folderPath, "ncnn", "fast", filename))
        elif "-ensemble" in filename:
            file = rarfile.RarFile(
                os.path.join(folderPath, "ncnn", "ensemble", filename)
            )
            file.extractall(path=os.path.join(folderPath, "ncnn", "ensemble"))
            os.remove(os.path.join(folderPath, "ncnn", "ensemble", filename))
        else:
            file = rarfile.RarFile(os.path.join(folderPath, "ncnn", filename))
            file.extractall(path=os.path.join(folderPath, "ncnn"))
            os.remove(os.path.join(folderPath, "ncnn", filename))

    print(
        green("SUCCESS"),
        yellow(filename[:-4]),
        green("model is downloaded to"),
        yellow(downloadPath),
    )
    toLog = f"{filename[:-4]} is downloaded to {downloadPath}"
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

    folderPath = os.path.join(modelsDir, model)
    os.makedirs(folderPath, exist_ok=True)

    downloadUrl = f"{TAGURL}{filename}"

    return downloadModels(model, filename, downloadUrl, folderPath)
