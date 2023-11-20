from dataclasses import dataclass, field

import cv2
import numpy as np


@dataclass
class OriginFrame:
    """
    video data와 frame data 정보 저장용 클래스. 영상을 프레임화한 후 프레임 기본 정보를 담는다.
    """

    image_path: str
    ref_video_path: str
    image_array: np.ndarray = field(init=False)
    height: int = field(init=False)
    width: int = field(init=False)

    def load_image(self) -> np.ndarray:
        """image_path 이미지 로드하여 array로 반환"""
        return cv2.imread(self.image_path)  # HWC

    def __post_init__(self) -> None:
        """image_path와 매핑되는 이미지 어레이와 사이즈 변수 초기화"""
        self.image_array = self.load_image()
        self.height, self.width = list(self.image_array.shape)[:-1]
