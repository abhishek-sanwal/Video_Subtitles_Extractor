
# Custom Exceptions
class NoSubtitlesException(Exception):
    pass


class VideoFileNotFoundException(Exception):
    pass

# Ffmpeg command failed
class CommandExectionFailed(Exception):
    pass