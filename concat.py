import os

def concatenate_files(output_file):
    # List of directories to search for .py files
    directories = []#['models', 'views', 'viewmodels']
    
    # Start with main.py
    files_to_concatenate = ['main.py', 'sound_manager.py', 'border_manager.py', 'timer.py', 'PomodoroUI.py' ]
    
    # Discover .py files in specified directories
    for directory in directories:
        for filename in os.listdir(directory):
            if filename.endswith(".py") and filename != "__init__.py":
                files_to_concatenate.append(os.path.join(directory, filename))

    # Write all files to the output file
    with open(output_file, 'w') as outfile:
        for fname in files_to_concatenate:
            with open(fname, 'r') as infile:
                outfile.write("#" * 80)
                outfile.write(f"\n# File: {fname}\n")
                outfile.write("#" * 80)
                outfile.write("\n\n")
                outfile.write(infile.read())
                outfile.write("\n\n")

# Usage
concatenate_files('combined.py')
