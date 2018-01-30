import textwrap

#Counts the lines in the input file.  Input file must be in FASTA format (.fas)
def LineCount(path=''):
	#Open the file
	with open(path) as input:
		#Put all the lines together in a list
		line_list = list(input)
		print(line_list)
		#Store the length of the list
		line_count = len(line_list)
		return line_count

def RemoveStopCodons(path=''):
	with open(path) as input:
		#Initialize variables
		line_count = LineCount()
		codon_list = []
		sequence = ''
		stop_codons = ['TAG','TGA','TAA']
		sequence_found = False
		sequence_num = 1
		lines_counted = 0

		#Initiate main loop
		#Loop through each line of the file
		for line in input:
			#Keep track of what number line the loop is on
			lines_counted += 1

			#Finds and stores the FASTA header for each nucleotide sequence
			if '>' in line and sequence_found == False:
				header = line
				sequence_found = True

			#If the loop has reached the end of a sequence, the beginning of
			#a new sequence, or the final line of DNA bases of the file,
			#enter secondary loop that concatenates the sequence, reads it
			#and replaces stop codons with gaps
			elif line == '\n' or ('>' in line and sequence_found == True) or (lines_counted == line_count):

				#If the last line with DNA information on it has been reached,
				#concatenate sequence as done before in the else statement near
				#the end of the script
				if lines_counted == line_count:
						edited_line = line.replace('\n','')
						sequence = sequence + edited_line

				#Find the index for each nucleotide in the sequence.
				for base in range(len(sequence)):
					base += 1

					#For every third character in the sequence, append it and
					#the previous two characters concatenated together as an
					#entry in codon_list
					if base % 3 == 0:
						three_bases = sequence[base - 3] + sequence[base - 2] + sequence[base - 1]

						codon_list.append(three_bases)

				#For each codon in the list of codons, if the codon is
				#in the list of stop codons, replace it with 'NNN' in codon_list
				index = 0
				for codon in codon_list:
					if codon in stop_codons:
						codon_list[index] = 'NNN'
					index += 1

				#Now, concatenate codon_list together as a string, new_seq
				sequence = ''
				new_seq = sequence.join(codon_list)

				#Write outputted sequence to a new .fas file
				if sequence_num == 1:
					with open('output.fas','w') as output:
						output.write(header)
						#Turn new_seq into a list of <= 79 character nucleotide
						#chunks
						wrapped_sequence = textwrap.wrap(new_seq)
						for chunk in wrapped_sequence:
							output.write(chunk)
							output.write('\n')
						output.write('\n')
				else:
					with open('output.fas','a') as output:
						output.write(header)

						wrapped_sequence = textwrap.wrap(new_seq)
						for chunk in wrapped_sequence:
							output.write(chunk)
							output.write('\n')
						if lines_counted == line_count:
							pass
						else:
							output.write('\n')

				#Re-initliaze relevent variables to start over for next sequence
				sequence = ''
				codon_list = []
				sequence_found = False
				sequence_num += 1

			#Concatenate the bits of sequence together
			else:
				edited_line = line.replace('\n','')
				sequence = sequence + edited_line

RemoveStopCodons()
