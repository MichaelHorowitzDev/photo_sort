import rearrange
import sys
import os

if __name__ == '__main__':
    if len(sys.argv) != 5:
        sys.exit('Error: Incorrect number of arguments passed')
    current_dir = sys.argv[1]
    output_dir = sys.argv[2]
    year = sys.argv[3].endswith('True')
    month = sys.argv[4].endswith('True')
    if not os.path.isdir(current_dir):
        sys.exit("Error: Current directory doesn't exist")
    elif not os.path.isdir(output_dir):
        sys.exit("Error: Output directory doesn't exist")
    else:
        rearrange.main(current_dir, output_dir, {'year': year, 'month': month})
