class File:
    def __init__(self, path: str) -> None:
        pass

    def add_content(self, content: str):
        pass

    def size(self):
        pass

    def info(self):
        pass


class MediaFile(File):
    def __init__(self, path: str, codec: str, geoloc: tuple, duration: int) -> None:
        pass

    def info(self):
        pass


class VideoFile(MediaFile):
    def __init__(
        self, path: str, codec: str, geoloc: tuple, duration: int, dimensions: tuple
    ) -> None:
        pass

    def info(self):
        pass


path = "/home/python/vanrossum.mp4"
codec = "h264"
geoloc = (23.5454, 31.4343)
duration = 487
dimensions = (1920, 1080)

video_file = VideoFile(path, codec, geoloc, duration, dimensions)
print(video_file)
