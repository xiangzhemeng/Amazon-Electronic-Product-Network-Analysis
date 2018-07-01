# Amazon Electronic Products Network Analysis

#### EPFL EE-558 Network & Data Science Project

**`Team Members`:** Tao Sun, Xiangzhe Meng, Xingce Bao, Süha Kagan Köse

**Network Graph page:** [Network Graph](https://xiangzhemeng.github.io/project/network-science-project/index.html)

### Abstract

Amazon is reshaping and recording our life as the biggest online retailer and as an invisible social network. We are connected with each other because we bought or reviewed the same product. Thanks to our behaviors, like purchasing, reviewing or viewing, the products in Amazon are also connected together. In this project, we mainly focus on electronic products.

We generate our network from three products: **Macbook**, **Surface** and **ThinkPad**, which we call "core" here. Starting from the core, we add the also_bought prodcuts into our network, which we call the "first layer" of our network. Then, we add the also_bought products of the first layer. In this project, we only add two layers of products. And, intuitively, each core is going to form a group of nodes. To visualize the network, we utilized **D3.js**, a javascript library for producing dynamic, interactive data visualizations in web browsers.

<img src="https://user-images.githubusercontent.com/25604193/35408980-38fe397e-0211-11e8-8893-930a8031a0eb.png" width="25%" height="25%">

After generating our network, we use **spectral graph theory**, **transductive learning** and **surpervised classification** to do clustering and comparison.

The project is a combination of two spearate analysis, one is only based on Macbook and Surface and the other is the study of all three groups. In each analysis, we weight our edge in two distinct ways and try to find out the difference.
