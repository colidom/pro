class File:
    def __init__(self, path: str) -> None:
        self.path = path
        self.contents = []

    def add_content(self, content: str):
        self.contents.append(content)

    def size(self):
        pass

    def info(self) -> str:
        return ...


class MediaFile(File):
    def __init__(self, path: str, codec: str, geoloc: tuple, duration: int) -> None:
        pass

    def info(self) -> str:
        return ...


class VideoFile(MediaFile):
    def __init__(
        self, path: str, codec: str, geoloc: tuple, duration: int, dimensions: tuple
    ) -> None:
        pass

    def info(self) -> str:
        return ...


path = "/home/python/vanrossum.mp4"
codec = "h264"
geoloc = (23.5454, 31.4343)
duration = 487
dimensions = (1920, 1080)

video_file = VideoFile(path, codec, geoloc, duration, dimensions)
video_file.add_content("audio/ogg")
video_file.add_content("video/webm")
print(video_file.info())
