#!/usr/bin/env python3
import os
import sys
import argparse
sys.path.append(os.path.join(os.path.dirname(__file__), 'source'))


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("folderName", help="Your desired folder")

