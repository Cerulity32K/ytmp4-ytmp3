# YT to MP4 & MP3
Converts a YouTube video to an MP4, then an MP3.\
Many YouTube to MP3 converters are either defunct, deprecated, outdated, filled with ads or sketchy. This small Python script was made out of frustration. While crude, it can get the job done.
# Running
Run with `python3 ytmp3.py "<url>" <name>` where url is the YouTube URL (must be in quotes) and name is the name the files will be saved as (without extension)
You MUST have pytube and moviepy installed (using pip3)
# PyTube returns an error!
Pytube can throw a RegexMatchError. This is likely due to PyTube itself not updating it's module to fit YouTube's API that might have been updated. Looking at the recent issues in PyTube should give a fix. It changes all the time, so there's no true way to solve it.
