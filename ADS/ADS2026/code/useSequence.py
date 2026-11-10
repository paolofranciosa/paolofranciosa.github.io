# TRY USING ONE OF THE FOLLOWING THREE IMPLEMENATIONS

import moduleSequence as ms
#import moduleSequenceSmart as ms
#import moduleSequenceSet as ms

dim = 30000
seq = ms.Sequence(dim, dim * 10)
print('created')
found, spent = seq.searches(seq, dim) 
print(f'found {found} in {spent} seconds for {dim} searches')

dim = 300000
seq = ms.Sequence(dim, dim * 10)
print('created')
found, spent = seq.searches(seq, dim) 
print(f'found {found} in {spent} seconds for {dim} searches')

