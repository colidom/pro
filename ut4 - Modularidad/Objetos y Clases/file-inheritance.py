class File:
    def __init__(self, path: str) -> None:
        self.path = path
        self.contents = []

    def add_content(self, content: str):
        self.contents.append(content)

    @property
    def size(self):
        return sum(len(content) for content in self.contents)

    def info(self) -> str:
        """/home/python/vanrossum.mp4 [size=19B]      # self.info() de File"""
        return f"{self.path} [size={self.size}B]"


class MediaFile(File):
    def __init__(self, path: str, codec: str, geoloc: tuple, duration: int) -> None:
        super().__init__(path)
        self.codec = codec
        self.geoloc = geoloc
        self.duration = duration

    def info(self) -> str:
        """Codec: h264                             # ┐
        Geolocalization: (23.5454, 31.4343)        # ├ self.info() de MediaFile
        Duration: 487s                             # ┘"""
        return f"Codec: {super().info()}\nGeolocalization: {self.geoloc}\nDuration: {self.duration}\n"


class VideoFile(MediaFile):
    def __init__(
        self, path: str, codec: str, geoloc: tuple, duration: int, dimensions: tuple
    ) -> None:
        super().__init__(path, codec, geoloc, duration)
        self.dimensions = dimensions

    def info(self) -> str:
        """Dimensions: (1920, 1080)  # self.info() de VideoFile"""
        return f"Dimensions: {super().info()}"


path = "/home/python/vanrossum.mp4"
codec = "h264"
geoloc = (23.5454, 31.4343)
duration = 487
dimensions = (1920, 1080)

video_file = VideoFile(path, codec, geoloc, duration, dimensions)
video_file.add_content("audio/ogg")
video_file.add_content("video/webm")
print(video_file.info())
