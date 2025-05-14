#!/usr/bin/env python3
import subprocess

# List of input files that we want to pass to isort.
input_files = [
    'random_1k_int',
    'random_2k_int',
    'random_4k_int',
    'random_8k_int',
    'random_16k_int',
    'random_32k_int',
    'random_64k_int',
    'random_128k_int'
]

# Path to gem5 binary
gem5_bin = '/u/csc368h/winter/pub/bin/gem5.opt'

# Path to your gem5 Python config script that calls isort
gem5_script = 'run_pbbs.py' # switch here

for infile in input_files:
    # The --outdir argument for gem5
    outdir_name = f"{infile}_out"
    
    # Construct the gem5 command
    cmd = [
        gem5_bin,
        f'--outdir={outdir_name}',  # override output directory
        gem5_script,
        '--binary_args', infile
    ]
    
    print(f"\nRunning gem5 with input file: {infile}")
    print("Command: " + " ".join(cmd))
    
    # Run the command as a subprocess
    subprocess.run(cmd, check=True)
