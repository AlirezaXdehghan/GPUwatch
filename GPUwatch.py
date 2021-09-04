import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--gpucount",action='store_true' , help = "Shows you how many gpus are connected right now")
parser.add_argument("-l", "--limit",type=int, help = "Quantity of gpus which should be connected: -l 5")
parser.add_argument("-fs", "--failscript", help = "the script (or file) which should be executed in case of a problem: -fs script.bat")
parser.add_argument("-ss", "--successscript", help = "the script (or file) which should be executed in case everything was ok: -ss script.bat")
args = parser.parse_args()

import os
stream = os.popen('wmic path win32_VideoController get name')
output = stream.read()
output = output.strip()
count = output.count('\n\n')

if args.gpucount:
    print("\nConnected GPUs: ", end=""),  print(count)
    print("if you're seeing more than what you have don't get excited, it's probably your integrated gpu\nUse this Number as your limit if all gpus are working now\n")

if args.limit:
    if count<args.limit:
        os.startfile(args.failscript)
    elif args.successscript:
        os.startfile(args.successscript)



