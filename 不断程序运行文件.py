from subprocess import Popen, PIPE


def run(file: str, command: str = ""):
  Popen(f"python {file} {command}" if command else f"python {file}", shell=True, stdout=PIPE)
