# Structure Token



# General idea

We want to model dynamic properties

- Local token: residue +- 5 residues
- Interaction token: different interaction patterns (more coarse-grained)

Models we want to have:

- Token assignment model: given structure, assign the token (actually, we first have a labeled set)
- Token distribution prediction model: given sequence, predict the distribution of tokens
- Structure generation model: given token distribution, generate the dynamic structure

How to train the models?

- Token assignment model: Easy
- Token distribution prediction model: Need discussion, but this is the last model to train
- Structure generation model: Using token assignment model as cost function, need auxiliary loss to ensure conformation diversity and reasonability.
  - e.g. the distance, or transformation rotation between two neighboring residues








