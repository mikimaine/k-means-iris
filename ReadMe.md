# K-means

Based on the results, the SSE value decreases as the value of k increases. 
This is expected because adding more clusters generally reduces the SSE.
However, the rate of decrease in SSE slows down significantly after a certain point. 

To determine the best value of k, we typically look for an “elbow” point in the SSE plot where the rate of decrease sharply diminishes. 

From the SSE values, it appears that the elbow point is around k=3, as the reduction in SSE becomes less pronounced beyond this value.
Therefore, k=3 might be considered the optimal number of clusters for the Iris dataset, balancing the trade-off between SSE reduction and simplicity of the model.
Yes, I am satisfied with these results.
Here are the results of the k-means clustering for different values of k:

| Experiment Number | Value of k | SSE Value  |
|-------------------|------------|------------|
| 1                 | 3          | 191.024737 |
| 2                 | 4          | 114.354072 |
| 3                 | 5          |  91.047670 |
| 4                 | 6          |  81.550757 |
| 5                 | 7          |  80.777739 |
| 6                 | 8          |  64.426748 |
| 7                 | 9          |  55.706900 |
| 8                 | 10         |  51.121095 |
| 9                 | 12         |  40.410667 |
| 10                | 15         |  35.044381 |


 <img src="/k-means.png" />