from typing import Any

from geu_cog import BasePredictor

class Predictor(BasePredictor):
    def setup(self):
        """Load the YOLO model
        1、加载模型
        2、直接读取配置文件中的视屏流地址，多线程进行持续的处理
        """
        # You can change this to your custom model path if needed
        # self.model = YOLO("weight/yolov8n.pt")
        # Uncomment for GPU acceleration if available
        # self.model.to('cuda')
        print("setup")

    def predict(self,stream_source: str,output_path: str,push_stream: str = None) -> Any:
        """Perform object detection on a video
        接收视频流地址并处理
        """
        print(stream_source,output_path,push_stream)
        return