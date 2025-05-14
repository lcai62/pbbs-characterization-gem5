
import subprocess

# list of input files
input_files = [
    'knn_1k',
    'knn_2k',
    'knn_4k',
    'knn_8k',
    'knn_16k',
    'knn_32k',
    'knn_64k',
    'knn_128k'
]

gem5_bin = '/u/csc368h/winter/pub/bin/gem5.opt'

gem5_script = 'run_pbbs.py'

for infile in input_files:
    outdir_name = f"{infile}_out"
    
    cmd = [
        gem5_bin,
        f'--outdir={outdir_name}', 
        gem5_script,
        '--binary_args', infile
    ]
    
    print(f"\nrunning gem5 with input file: {infile}")
    print("command: " + " ".join(cmd))
    
    subprocess.run(cmd, check=True)
