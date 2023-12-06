# Project Name: DNA Analysis and Facebook Sentiment Tool

## Introduction

This group project consists of two main parts: DNA analysis using the ADT SuffixTree and a Facebook sentiment analysis tool for forecasting the results of US presidential elections.

## Part 1: DNA Contamination Analysis

### SuffixTree Class

The SuffixTree class provides functionality for creating and analyzing suffix trees from a given tuple of strings. The following methods are implemented:

- `SuffixTree(S)`: Creates a suffix tree from the tuple of strings S.
- `T.getNodeLabel(P)`: Returns the substring that labels the node of the tree to which position P refers.
- `T.pathString(P)`: Returns the substring associated with the path in the tree from the root to the node to which position P refers.
- `T.getNodeDepth(P)`: Returns the length of the substring associated with the path from the root to the node to which position P refers.
- `T.getNodeMark(P)`: Returns the mark of the node to which position P refers.
- `T.child(P, s)`: Returns the position of the child of the node to which position P refers, based on the given substring s.

### DNAContamination Class

The DNAContamination class is designed to identify contaminants with a higher degree of contamination in a DNA string. It includes the following methods:

- `DNAContamination(s, l)`: Initializes a DNAContamination object with a given DNA string s and contamination threshold l.
- `addContaminant(c)`: Adds a contaminant c to the set and saves the degree of contamination of s by c.
- `getContaminants(k)`: Returns the k contaminants with the highest degree of contamination among the added contaminants.

## Part 2: Facebook Sentiment Analysis

### facebook_enmy Function

The `facebook_enmy` function takes a set of voters V and a dictionary E representing friendship relationships with assigned enmity levels. It returns two sets, D and R, corresponding to voters for Democrats and Republicans, respectively.

### facebook_friend Function

The `facebook_friend` function takes a dictionary V with voter likelihoods for Democrats and Republicans, and a dictionary E representing friendship relationships with assigned friendship levels. It returns two sets, D and R, corresponding to voters for Democrats and Republicans, respectively.

## Bonus Points

- For Part 1, bonus points are awarded based on the running time of the `facebook_enmy` function and the enmity level between D and R.
- For Part 2, bonus points are awarded based on the running time of the `facebook_friend` function.

## Implementation

All functions and classes must be implemented in a file named `facebook.py`. Solutions should be agnostic to the representation of voters.

## More Information
for more detailed information:
- About 1 Part [here](https://github.com/MattiaMarseglia/Design-and-Analysis-of-Algorithms/blob/main/Suffix%20Tree%20Text%20Processing/midterm_homework.pdf)
- About 2 Part [here](https://github.com/MattiaMarseglia/Design-and-Analysis-of-Algorithms/blob/main/Graphs%20Project/final_homework.pdf)
