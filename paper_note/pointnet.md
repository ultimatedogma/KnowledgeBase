# PointNet

#deep_learning #point_cloud

## Overview

Core concept:

- Using point cloud directly as input rather than using voxels
- Using max pooling to achieve **permutation invariance**
- Using symmetric function to process individual points


```bibtex
@inproceedings{pointnet,
  title={Pointnet: Deep learning on point sets for 3d classification and segmentation},
  author={Qi, Charles R and Su, Hao and Mo, Kaichun and Guibas, Leonidas J},
  booktitle={Proceedings of the IEEE conference on computer vision and pattern recognition},
  pages={652--660},
  year={2017}
}
```

## Model

### Formulation

Input and output: 

- Input: Point cloud
- Output: Classification label for entire point cloud 
- Output: Segmentation label for each point



Problem statement:

- A point cloud is represented as a set of 3D points $\{P_i \ | \ i=1, \cdots, N\}$, where each point $P_i$ is a vector of its $(x, y, z)$ coordinates plus extra features (e.g. normal, color, etc.)
- For classification, our network outputs $k$ scores for each of the $k$ candidate classes
- For segmentation, our network outputs $n \times m$ scores for each of the $n$ points and $m$ semantic sub-categories


Main properties of point cloud:

- Unordered
- Interaction among points
- Invariance under transformations


### PointNet Architecture


Architecture: 

![PointNet Architecture](pointnet_asset/pointnet_architecture.png ':size=99%')

Three key modules:

- **Max pooling layer** as a symmetric function to aggregate information from all the points
- A **local and global information combination** structure
- Two **joint alignment networks** that align both input points and point features


### Symmetry Function for Unordered Input

To make a model invariant to input permutation, three strategies exist:

- Sort input into a canonical order
  - But there is no ordering that is stable for high-dimensional data
- Treat the input as a sequence to train an RNN, but augment the training data by all kinds of permutations
  - Order does matter and cannot be totally omitted in RNN
- Use a simple symmetric function to aggregate the information from each point
  - This is the idea of PointNet

Our idea is to approximate a general function defined on a point set by applying a symmetric function on transformed elements in the set:

$$
f(x_1,\cdots,x_n) \approx g(h(x_1),\cdots,h(x_n))
$$

- $h$ is a MLP
- $g$ is a symmetric function, composition of a single variable function and a max-pooling function


### Local and Global Information Aggregation

The output from the above section forms a vector $[f_1, \cdots, f_k]$, which is a global signature of the input set.

For segmentation, we need to combine the local and global information.

- We concatenate the global feature with each of the point features.
- Then we extract new per point features based on the combined point features


### Joint Alignment Network

The semantic labeling of a point cloud has to be invariant if the point cloud undergoes geometric transformations.

- Natural solution is to align all input set to a canonical space before feature extraction
  - **Spatial transformer** introduces the idea to align 2D images through sampling and interpolation, achieved by a specifically tailored layer implemented on GPU
- Our input form of point clouds allows us to achieve this goal in a much simpler way
  - We predict an affine transformation matrix by a mini-network (T-net) and directly apply this transformation to the coordinates of input points









## Extended Reading

- [Transformers in 3D Point Clouds](https://arxiv.org/pdf/2205.07417)
- [Point Transformer](https://openaccess.thecvf.com/content/ICCV2021/html/Zhao_Point_Transformer_ICCV_2021_paper.html?ref=;)
- [GeoTransformer](https://arxiv.org/abs/2308.03768)
- [PointNet++](https://arxiv.org/abs/1706.02413)


















