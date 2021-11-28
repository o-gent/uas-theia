from typing import List, Tuple
import numpy as np
from theia.spec import ImageRecognitionResult
from utils import logger

def image_recognition(image: np.ndarray,  gps_image_taken: Tuple(float, float)) -> List[ImageRecognitionResult]:
    """
    The resulting function of all this mess
    """
    logger.info("got image")
    return ImageRecognitionResult
