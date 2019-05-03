+++
date=2019-05-02
title="Two papers accepted at SIGIR"
+++

The IR lab got two papers accepted at the 42nd International ACM SIGIR Conference on Research and Development in Information Retrieval.

<a href={{<ref "publication/hansensigirlong/index.md">}}><h3>Unsupervised Neural Generative Semantic Hashing</h3></a> 
Fast similarity search is a key component in large-scale information retrieval, where semantic hashing has become a popular strategy for representing documents as binary hash codes. Recent advances in this area have been obtained through neural network based models: generative models trained by learning to reconstruct the original documents. We present a novel unsupervised generative semantic hashing approach, \textit{Ranking based Semantic Hashing} (RBSH) that consists of both a variational and a ranking based component. Similarly to variational autoencoders, the variational component is trained to reconstruct the original document conditioned on its generated hash code, and as in prior work, it only considers documents individually. The ranking component solves this limitation by incorporating inter-document similarity into the hash code generation, modelling document ranking through a hinge loss. To circumvent the need for labelled data to compute the hinge loss, we use a weak labeller and thus keep the approach fully unsupervised. 

Extensive experimental evaluation on four publicly available datasets against traditional baselines and recent state-of-the-art methods for semantic hashing shows that RBSH significantly outperforms all other methods across all evaluated hash code lengths. In fact, RBSH hash codes are able to perform similarly to state-of-the-art hash codes while using 2-4x fewer bits. 

<a href={{<ref "publication/hansensigirshort/index.md">}}><h3>Contextually Propagated Term Weights for Document Representation</h3></a>
Word embeddings predict a word from its neighbours by learning small, dense embedding vectors. In practice, this prediction  corresponds to a semantic score given to the predicted word (or term weight). We present a novel model that, given a target word, redistributes part of that word's weight (that has been computed with word embeddings) across words occurring in similar contexts as the target word. Thus, our model aims to simulate how semantic meaning is shared by words occurring in similar contexts, which is incorporated into bag-of-words document representations. Experimental evaluation in an unsupervised setting against 8 state of the art baselines shows that our model yields the best micro and macro F1 scores across datasets of increasing difficulty.
