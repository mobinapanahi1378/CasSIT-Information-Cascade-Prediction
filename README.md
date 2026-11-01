# CasSIT
### Structural-Influence-Aware Cascade Prediction

CasSIT is a deep learning project for predicting information cascade size in social networks.

This project extends the original **CasCIFF** framework by incorporating additional mechanisms for jointly modeling structural, user-related, and temporal information.

## Key Contributions

- **Structural-Influence-Aware Temporal Attention (SIATA):** A temporal attention mechanism that jointly considers BiGRU temporal representations and structural-influence representations of cascade subgraphs.
- **Structural-Influence Temporal Fusion Gate (SITFG):** An adaptive fusion mechanism that combines global structural-influence information with attention-weighted temporal representations.
- **Joint Representation Learning:** Combines local graph structural features and global user embeddings through an autoencoder.
- **Cascade Size Prediction:** Uses a BiGRU-based temporal modeling architecture and adaptive feature fusion for final cascade size prediction.

## Model Architecture

The main components of CasSIT include:

1. Global user representation learning
2. Subgraph-level user representation aggregation
3. Local structural feature extraction using BiGCN
4. Joint structural-influence representation learning using an autoencoder
5. Temporal modeling using BiGRU
6. Structural-influence-aware temporal attention (SIATA)
7. Structural-influence temporal fusion (SITFG)
8. Final cascade size prediction

## Datasets

The model was evaluated using three real-world social network datasets:

- APS
- Weibo
- Twitter

## Technologies

- Python
- PyTorch
- Deep Learning
- Graph Neural Networks
- Autoencoders
- BiGRU
- Attention Mechanisms

## Project Background

This project was developed as part of my Master's thesis in Computer Engineering – Software.

It is based on the original CasCIFF framework:

Zhu, H., et al. (2024). *CasCIFF: A Cross-Domain Information Fusion Framework Tailored for Cascade Prediction in Social Networks.* Knowledge-Based Systems.

Original implementation:  
https://github.com/XiaoYuan011/CasCIFF

The project introduces additional structural-influence-aware temporal attention and adaptive fusion mechanisms on top of the original framework.

## Repository Status

This repository contains the implementation of the CasSIT model developed for my Master's thesis.
