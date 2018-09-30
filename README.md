# Global Anchor Method for Corpus Dissimilarity and Domain Transferrability 

This is the repo for the experiments in the paper `Quantifying Linguistic Shifts: the Global Anchor Method and Its Applications`  

The global anchor method is a powerful tool for comparing language usage between different corpora through word vectors. It can be used for
- Transfer learning: determining whether a model trained on one corpus will transfer to another. If the corpora are very different in terms of their language usage, transfer learning may not perform well.
- Discover linguistic shifts: one can use this method to determine the rate at which language changes with respect to time.
- Discover domain variations: one can use this method to discover whether language adapts to specific domains.

In particular, we showed that the global anchor method is 
- theoretically as powerful as the alignment method, 
- practically more widely applicable and easier to implement than the alignment method, 
- reveals finer structures than frequency-based methods (e.g. Pechenick et. al. [Characterizing the Google Books corpus: Strong limits to inferences of socio-cultural and linguistic evolution](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0137041))

Here is a short overview of what is in this directory.

Directory | What's in it?
--- | ---
`equivalence.py` | In the paper we showed that the alignment and global anchor methods, when viewed as metrics, are equivalent. This provides numerical verification for that claim.
`jsd_loss.ipynb` | This is the script for computing the Jensen-Shannon divergence for the Google ngram corpus. We demonstrate the jsd method does not provide fine-grained details as our method, in particular we show it does not capture the war-effect on English language and literature.
`laplacian.ipynb` | The script of the Laplacian method for language evolution trajectory and topic clustering.
`pip_loss.ipynb` | The script for calculating the PIP loss for Google ngram corpus between every year.
`plot.ipynb` | The script for the war-effect on English language evolution. 
`validate_equivalence.ipynb` | The script for empirical validation of the equivalence of the global anchor method and the alignment method.


We also provides a set of processed corpora:

Dataset name | Download
--- | ---
Google Books | [Google Books Ngram Dataset](https://books.google.com/ngrams) (We have trained a set of word vectors for years between 1800-2008, which can be found [here](https://drive.google.com/file/d/1TDBCLHzmt8yu2LVs6Ragl_wP8tvkFLZ-/view?usp=sharing)) 
