
# dna seqauence of length k
# how many combinations of sequences (4**k)
# this is a recursion problem
# (k-mer probelm is a different problem)


k = int(input("Enter the desired sequence length k: "))

def generate_dna_sequences(current_sequence='', k=0):
    dna_bases = ['A', 'C', 'G', 'T']

    # Base case
    if len(current_sequence) == k:
        return [current_sequence]

    # Recursive case
    sequences = []
    for base in dna_bases:
        sequences += generate_dna_sequences(current_sequence + base, k)
    return sequences

# Main
print(generate_dna_sequences(k=k))


'''
USING TWO FUNCTIONS

k = int(input("Enter the desired sequence length k: "))

# Function
def generate_dna_sequences(k):
	dna_bases = ['A', 'C', 'G', 'T']
	sequences = []
	
	def backtrack(current_sequence):
		if len(current_sequence) == k:
			sequences.append(current_sequence)
			return

		for base in dna_bases: 
			backtrack(current_sequence + base)

	backtrack('')
	return sequences

# Main
print(generate_dna_sequences(k))

'''



'''
WITHOUT USING RECURSION

k = int(input("Enter the desired sequence length k: "))

def generate_dna_sequences(k):
    dna_bases = ['A', 'C', 'G', 'T']
    sequences = []

    # Start with a list containing an empty string
    sequences.append('')

    # Loop over each length from 1 to k
    for _ in range(k):
        # For each existing sequence, append each DNA base
        sequences = [seq + base for seq in sequences for base in dna_bases]
    
    return sequences

# Main
print(generate_dna_sequences(k))

'''



	



















