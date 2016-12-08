# https://zulko.github.io/moviepy/crash_course/crash_course.html
import os
import sys
from moviepy.editor import *


def main():
    # Load myHolidays.mp4 and select the subclip 00:00:50 - 00:00:60
    clip = VideoFileClip("0KRt1FCSpIQ.mp4").subclip(51,52)

    # Composite video clips
    video = concatenate([clip])

    # Write the result to a file
    video.write_videofile("movie.mp4")

if __name__ == "__main__":
    main()
