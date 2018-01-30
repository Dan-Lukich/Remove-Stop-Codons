# remove_stop_codons.py

This script is designed to remove the stop codons TAG, TGA, and TAA in FASTA
(.fas) formatted biological data.  It takes one FASTA file as input and writes
its output to a file called ```output.fas```.

### Instructions

  - Place your input file in the directory with ```remove_stop_codons.py```
  (to keep things organized).
  - Fill in the the ```''``` in the ```path=''``` argument of the function
  definitions for both ```LineCount()``` and ```RemoveStopCodons()``` with the
  path to your input file with forward slashes or just the name of your input
  file if it is in the same directory as ```remove_stop_codons.py```.
  - Navigate to the working directory and run ```remove_stop_codons.py``` from
  the command line.

### Sidenotes

  - A sample input file is included called ```input.fas```.
