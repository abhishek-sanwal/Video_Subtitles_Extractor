
# Custom Exceptions
class NoSubtitlesException(Exception):
    pass


class VideoFileNotFoundException(Exception):
    pass

# Ffmpeg command failed
class CommandExecutionFailed(Exception):
    pass