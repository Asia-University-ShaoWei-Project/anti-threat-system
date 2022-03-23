from os import environ
import os

ON = True
OFF = False


def conf(name):
  return os.getenv(name)
