# GPUwatch
GPUwatch is a Windows only tool that counts the connected GPUs and let's you take action if one of them has not initialized

## Requirements

* <b>wcim</b> should be in your <b>PATH</b>
* Python 3
* A rig with GPU problems

## CommandLine Arguments

```
-h,--help : Shows the help
-l,--limit : sets the GPU limit, if connected GPUs are below this number, fail script will run, if not the success script will run
-fs,--failscript : location or name of the script to run in case of failure
-ss,--successscript : location or name of the script to run in case of failure
--gpucount : counts the currently connected GPUs, run it for the first time and use it as the limit
```

## Usage
Clone this repo and put it anywhere you want.
You can simply edit the run.bat file and add your desired parameters or run the file using CommandLine.
It's also not necessary to use the fail.bat or success.bat, you can point to any file to open, [maybe a cat video?](https://www.youtube.com/watch?v=7yLxxyzGiko)
here's some examples below

``
python.exe GPUwatch.py --gpucount   #good for the first time, take the count and use it as the limit
``
``
python.exe GPUwatch.py -l 5 -fs fail.bat -ss success.bat   #if the connected GPUs go below 5, fail.bat will run, otherwise success.bat will be executed
``

That's it, Happy Mining!
