# Project Name: DNA Analysis and Facebook Sentiment Tool

## Introduction

This repository contains two distinct projects developed for the course on Design and Analysis of Algorithms. The first project focuses on DNA analysis using the Abstract Data Type (ADT) SuffixTree, and the second project aims to forecast US presidential election results using Facebook sentiment analysis.

## Part 1: DNA Contamination Analysis

### Overview

The DNA contamination analysis project addresses the problem of identifying and analyzing potential contaminants in a DNA sequence. This is crucial in ensuring the integrity of DNA sequencing processes, which can be compromised by unwanted DNA fragments.

### SuffixTree Class

The `SuffixTree` class provides a robust implementation for creating and analyzing suffix trees from a given tuple of strings. Key methods include:

- `SuffixTree(S)`: Initializes a suffix tree from the tuple of strings `S`.
- `T.getNodeLabel(P)`: Returns the substring labeling the node at position `P`.
- `T.pathString(P)`: Retrieves the substring associated with the path from the root to node `P`.
- `T.getNodeDepth(P)`: Provides the length of the path substring from the root to node `P`.
- `T.getNodeMark(P)`: Returns the mark of the node at position `P`.
- `T.child(P, s)`: Finds the child node of `P` based on substring `s`.

### DNAContamination Class

The `DNAContamination` class is designed to identify contaminants with a high degree of contamination in a DNA string. Its main methods include:

- `DNAContamination(s, l)`: Initializes the class with a DNA string `s` and contamination threshold `l`.
- `addContaminant(c)`: Adds a contaminant `c` to the set and calculates its contamination degree in `s`.
- `getContaminants(k)`: Returns the `k` contaminants with the highest contamination degree.

### Implementation Details

The implementation adheres to the following time complexities:
- `SuffixTree(S)` operates in O(n^2) time, with `n` being the total length of strings in `S`.
- `T.getNodeLabel(P)`, `T.getNodeMark(P)`, and `T.getNodeDepth(P)` run in O(1) time.
- `T.pathString(P)` runs in O(s) time, where `s` is the path substring length.
- `T.child(P, s)` has an amortized time complexity of O(len(s)).

## Part 2: Facebook Sentiment Analysis

### Overview

The Facebook sentiment analysis project leverages the vast amount of data on social networks to predict voting behaviors in US presidential elections. It considers friendship and enmity relationships among voters to classify them into groups supporting Democrats or Republicans.

### facebook_enmy Function

The `facebook_enmy` function determines voter groups based on enmity levels:

- **Input**: A set of voters `V` and a dictionary `E` with enmity levels for voter pairs.
- **Output**: Two sets, `D` (Democrats) and `R` (Republicans).

### facebook_friend Function

The `facebook_friend` function classifies voters based on friendship levels and voting likelihoods:

- **Input**: A dictionary `V` with voter likelihoods and a dictionary `E` with friendship levels.
- **Output**: Two sets, `D` (Democrats) and `R` (Republicans).

### Implementation Details

- `facebook_enmy` aims to maximize enmity between groups and minimize intra-group enmity.
- `facebook_friend` maximizes intra-group friendship and the total likelihood of group votes.

## Bonus Points

- **Part 1**: Bonus points are awarded based on the running time of the `facebook_enmy` function and the inter-group enmity level.
- **Part 2**: Bonus points are awarded based on the running time of the `facebook_friend` function.

## Implementation

All functions and classes should be implemented in a file named `facebook.py`. Solutions should be robust to various representations of voters.

## More Information

For detailed information on the projects:
- [DNA Contamination Analysis](https://github.com/MattiaMarseglia/Design-and-Analysis-of-Algorithms/blob/main/Suffix%20Tree%20Text%20Processing/midterm_homework.pdf)
- [Facebook Sentiment Analysis](https://github.com/MattiaMarseglia/Design-and-Analysis-of-Algorithms/blob/main/Graphs%20Project/final_homework.pdf)
