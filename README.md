# Problem and goal

In genetic analysis, it is often necessary to remove closely related samples because many genetic models assume independence among samples. However, simply removing one of the related samples may not consider the connectivity among the samples.

To address this problem, I propose a graph-based method to break down the close relationships among samples while attempting to retain as many samples as possible for subsequent analysis. This graph-based approach aims to capture the connections between samples and utilize this information to make informed decisions about which samples to retain and which ones to remove.
# Algorithm to solve the problem

1. Graph Construction: Build a graph representation of relationships among the samples, where each sample is represented as a node in the graph. The connections between samples is determined based on kinship calculated by KING (Manichaikul A, Mychaleckyj JC, Rich SS, Daly K, Sale M, Chen WM (2010) Robust relationship inference in genome-wide association studies. Bioinformatics 26(22):2867-2873). 

Here we focus on the relationships among samples with a high degree of relatedness.

2. Breaking Down Relationships: Once the close relationships are identified, determine the optimal strategy to break down these relationships while preserving as many samples as possible. This step requires careful consideration to balance the removal of related samples with retaining as many samples possible.

```
Algorithm rel_breaker
Input: kinship file F, relatedness cutoff C
Output: a list of sample ids for removal
read in pairwise sample kinship from file, use sample id as vertex, build a graph G using the pairwise sample relationship with kinship greater than or equal to certain cutoff C;
initialzie an empty remove list L
while the graph G is not empty:
do
  Choose any vertex V of the graph G as start point
  Using Breadth First Traversal (BFS) algorithm to traverse over the graph G, and record the vertex V' with the maximum degree of connectivity.
  for all the vertex Vi connected to V'
  do 
    remove the edge between vertex Vi and vertex V'
    if no further vertex connected to vertex Vi
    then
      pop Vi from the graph G
    end if
  end for
  append V' to remove list L
  pop V'
end while
output remove list L
```

# Implementation and usage

Here I 
```
usage: graph.py [-h] -i INPUT [-o OUTPUT] [-c CUTOFF] [-t]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Filename of input (kinship file)
  -o OUTPUT, --output OUTPUT
                        Filename of output (removed eid list)
  -c CUTOFF, --cutoff CUTOFF
                        Cutoff for kinship, support absolute kinship value or degree such as (1, 2, or 3), default=0.0884
  -t, --has-title       The input has title or not, default=False
```

# Sample input
Sample input look like below (more pairs of relationship please refer to sample.txt)
```
SID1 SID2 HetHet IBS0 Kinship
S1000025 S2025656 0.045 0.0144 0.061
S1000130 S3375759 0.047 0.0133 0.0739
```
