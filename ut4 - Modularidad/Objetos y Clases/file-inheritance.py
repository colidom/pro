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
