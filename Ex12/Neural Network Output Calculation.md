
# Neural Network Output Calculation

## Question

The weight values between nodes $i$ and $j$ in the network are given as $\omega_{ij}$:

$$\omega_{13} = -2$$ 

$$\omega_{23} = 3$$


$$
\omega_{14} = 4
$$

$$
\omega_{24} = -1
$$

$$
\omega_{35} = 1
$$

$$
\omega_{45} = -1
$$

$$
\omega_{36} = -1
$$

$$
\omega_{46} = 1
$$

Nodes 3, 4, 5, 6 use the following activation function:

$$
\varphi(\nu) = \begin{cases} 
1 & \nu \geq 0 \\ 
0 & else 
\end{cases}
$$

Where $\nu$ denotes the sum of the weights at the node. The input to nodes 1 and 2 has a value of 0 or 1.

Calculate the output vector of the network for the following input patterns:

| Pattern | P_1 | P_2 | P_3 | P_4 |
|---------|-----|-----|-----|-----|
| Node 1  | 1   | 0   | 1   | 1   |
| Node 2  | 1   | 1   | 0   | 1   |

## Solution

To calculate the output vector of the network for the given input patterns, we need to follow these steps for each pattern:

1. Compute the input to the hidden layer nodes (nodes 3 and 4).
2. Apply the activation function to get the output of the hidden layer nodes.
3. Compute the input to the output layer nodes (nodes 5 and 6).
4. Apply the activation function to get the final output.

### Pattern P1:
Input: Node 1 = 1, Node 2 = 1

1. **Input to hidden layer nodes:**

$$
\nu_3 = \omega_{13} \cdot 1 + \omega_{23} \cdot 1 = -2 \cdot 1 + 3 \cdot 1 = 1
$$

$$
\nu_4 = \omega_{14} \cdot 1 + \omega_{24} \cdot 1 = 4 \cdot 1 - 1 \cdot 1 = 3
$$

2. **Output of hidden layer nodes (using activation function):**

$$
\varphi(\nu_3) = \varphi(1) = 1
$$

$$
\varphi(\nu_4) = \varphi(3) = 1
$$

3. **Input to output layer nodes:**

$$
\nu_5 = \omega_{35} \cdot \varphi(\nu_3) + \omega_{45} \cdot \varphi(\nu_4) = 1 \cdot 1 + (-1) \cdot 1 = 1 - 1 = 0
$$

$$
\nu_6 = \omega_{36} \cdot \varphi(\nu_3) + \omega_{46} \cdot \varphi(\nu_4) = (-1) \cdot 1 + 1 \cdot 1 = -1 + 1 = 0
$$

4. **Output of output layer nodes (using activation function):**

$$
\varphi(\nu_5) = \varphi(0) = 1
$$

$$
\varphi(\nu_6) = \varphi(0) = 1
$$

Final output for Pattern P1: \([1, 1]\)

### Pattern P2:
Input: Node 1 = 0, Node 2 = 1

1. **Input to hidden layer nodes:**

$$
\nu_3 = \omega_{13} \cdot 0 + \omega_{23} \cdot 1 = -2 \cdot 0 + 3 \cdot 1 = 3
$$

$$
\nu_4 = \omega_{14} \cdot 0 + \omega_{24} \cdot 1 = 4 \cdot 0 - 1 \cdot 1 = -1
$$

2. **Output of hidden layer nodes (using activation function):**

$$
\varphi(\nu_3) = \varphi(3) = 1
$$

$$
\varphi(\nu_4) = \varphi(-1) = 0
$$

3. **Input to output layer nodes:**

$$
\nu_5 = \omega_{35} \cdot \varphi(\nu_3) + \omega_{45} \cdot \varphi(\nu_4) = 1 \cdot 1 + (-1) \cdot 0 = 1
$$

$$
\nu_6 = \omega_{36} \cdot \varphi(\nu_3) + \omega_{46} \cdot \varphi(\nu_4) = (-1) \cdot 1 + 1 \cdot 0 = -1
$$

4. **Output of output layer nodes (using activation function):**

$$
\varphi(\nu_5) = \varphi(1) = 1
$$

$$
\varphi(\nu_6) = \varphi(-1) = 0
$$

Final output for Pattern P2: \([1, 0]\)

### Pattern P3:
Input: Node 1 = 1, Node 2 = 0

1. **Input to hidden layer nodes:**

$$
\nu_3 = \omega_{13} \cdot 1 + \omega_{23} \cdot 0 = -2 \cdot 1 + 3 \cdot 0 = -2
$$

$$
\nu_4 = \omega_{14} \cdot 1 + \omega_{24} \cdot 0 = 4 \cdot 1 - 1 \cdot 0 = 4
$$

2. **Output of hidden layer nodes (using activation function):**

$$
\varphi(\nu_3) = \varphi(-2) = 0
$$

$$
\varphi(\nu_4) = \varphi(4) = 1
$$

3. **Input to output layer nodes:**

$$
\nu_5 = \omega_{35} \cdot \varphi(\nu_3) + \omega_{45} \cdot \varphi(\nu_4) = 1 \cdot 0 + (-1) \cdot 1 = -1
$$

$$
\nu_6 = \omega_{36} \cdot \varphi(\nu_3) + \omega_{46} \cdot \varphi(\nu_4) = (-1) \cdot 0 + 1 \cdot 1 = 1
$$

4. **Output of output layer nodes (using activation function):**

$$
\varphi(\nu_5) = \varphi(-1) = 0
$$

$$
\varphi(\nu_6) = \varphi(1) = 1
$$

Final output for Pattern P3: \([0, 1]\)

### Pattern P4:
Input: Node 1 = 1, Node 2 = 1

1. **Input to hidden layer nodes:**

$$
\nu_3 = \omega_{13} \cdot 1 + \omega_{23} \cdot 1 = -2 \cdot 1 + 3 \cdot 1 = 1
$$

$$
\nu_4 = \omega_{14} \cdot 1 + \omega_{24} \cdot 1 = 4 \cdot 1 - 1 \cdot 1 = 3
$$

2. **Output of hidden layer nodes (using activation function):**

$$
\varphi(\nu_3) = \varphi(1) = 1
$$

$$
\varphi(\nu_4) = \varphi(3) = 1
$$

3. **Input to output layer nodes:**

$$
\nu_5 = \omega_{35} \cdot \varphi(\nu_3) + \omega_{45} \cdot \varphi(\nu_4) = 1 \cdot 1 + (-1) \cdot 1 = 1 - 1 = 0
$$

$$
\nu_6 = \omega_{36} \cdot \varphi(\nu_3) + \omega_{46} \cdot \varphi(\nu_4) = (-1) \cdot 1 + 1 \cdot 1 = -1 + 1 = 0
$$

4. **Output of output layer nodes (using activation function):**

$$
\varphi(\nu_5) = \varphi(0) = 1
$$

$$
\varphi(\nu_6) = 
\varphi(0) = 1
$$

Final output for Pattern P4: \([1, 1]\)

## Summary of Outputs:

$$
\begin{array}{c|c|c}
Pattern & Input (Node 1, Node 2) & Output (Node 5, Node 6) \\
\hline
P1 & (1, 1) & [1, 1] \\
P2 & (0, 1) & [1, 0] \\
P3 & (1, 0) & [0, 1] \\
P4 & (1, 1) & [1, 1] \\
\end{array}
$$
