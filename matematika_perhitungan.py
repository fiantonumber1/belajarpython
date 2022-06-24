import numpy as np
from numpy.testing import assert_allclose


def mean_naive(X):
    """Compute the sample mean for a dataset by iterating over the dataset.

    Args:
        X: `ndarray` of shape (N, D) representing the dataset. N
        is the size of the dataset and D is the dimensionality of the dataset.
    Returns:
        mean: `ndarray` of shape (D, ), the sample mean of the dataset `X`.
    """
    # YOUR CODE HERE
    ### Uncomment and edit the code below
#     iterate over the dataset and compute the mean vector.
    try:
        X = np.array(X)
    except:
        pass
    N, D = X.shape
    mean = np.zeros((D,))
    #N =4 , D=2
    #D = [a,b]
    for d in range(D):
        for n in range(N):
            mean[d]+=X[n][d]
            if n == (N-1):
                mean[d] = mean[d]/N
    return mean

def cov_naive(X):
    """Compute the sample covariance for a dataset by iterating over the dataset.

    Args:
        X: `ndarray` of shape (N, D) representing the dataset. N
        is the size of the dataset and D is the dimensionality of the dataset.
    Returns:
        ndarray: ndarray with shape (D, D), the sample covariance of the dataset `X`.
    """
    # YOUR CODE HERE
    ### Uncomment and edit the code below

    try:
        X = np.array(X)
    except:
        pass
    N, D = X.shape

      ### Edit the code below to compute the covariance matrix by iterating over the dataset.
    covariance = np.zeros((D, D))
    averange = mean(X)
    kumpulan_covar = 0
    for su in range(N):
        x_y_z_dst = X[su]
        n=0
        selisih = []
        for i in averange:
            selisih.append(0)
            selisih[n] = float(i)-float(x_y_z_dst[n])
            n+=1
        covar=1
        for m in selisih:
            covar = covar*m
        kumpulan_covar+=covar
        if su==(N-1):
            kumpulan_covar =kumpulan_covar/N

    kanans,kiris = N, D = covariance.shape
    for kanan in range(kanans):
        for kiri in range(kiris):
            covariance[kanan][kiri]=kumpulan_covar

    N, D = X.shape
    #print(N,D)
    # 4,2
    m = []

    for d in range(D):
        for n in range(N):
            #print(d,n)
            m.append(0)
            m[n]=X[n][d]
            if n == (N-1):
                covariance[d][d]=np.var(m)
                m = []


#     ### Update covariance

#     ###
    return covariance

def mean(X):
    """Compute the sample mean for a dataset.

    Args:
        X: `ndarray` of shape (N, D) representing the dataset. N
        is the size of the dataset and D is the dimensionality of the dataset.
    Returns:
        ndarray: ndarray with shape (D,), the sample mean of the dataset `X`.
    """
    # YOUR CODE HERE
    ### Uncomment and edit the code below
    # m = np.zeros((X.shape[1]))
    # return m
    N, D = X.shape
    m = np.zeros((X.shape[1]))
    m = X.mean(0)
    return m


def cov(X):
    """Compute the sample covariance for a dataset.

    Args:
        X: `ndarray` of shape (N, D) representing the dataset. N
        is the size of the dataset and D is the dimensionality of the dataset.
    Returns:
        ndarray: ndarray with shape (D, D), the sample covariance of the dataset `X`.
    """
    # YOUR CODE HERE

    # It is possible to vectorize our code for computing the covariance with matrix multiplications,
    # i.e., we do not need to explicitly
    # iterate over the entire dataset as looping in Python tends to be slow
    # We challenge you to give a vectorized implementation without using np.cov, but if you choose to use np.cov,
    # be sure to pass in bias=True.
    ### Uncomment and edit the code below
#     N, D = X.shape
#     ### Edit the code to compute the covariance matrix
#     covariance_matrix = np.zeros((D, D))
#     ### Update covariance_matrix here
#     ###
#     return covariance_matrix

    try:
        X = np.array(X).T
    except:
        pass
    N, D = X.shape
    ### Edit the code below to compute the covariance matrix by iterating over the dataset.
    covariance_matrix = np.zeros((D, D))
    covariance_matrix = np.cov(X,bias=True)
    return covariance_matrix


def affine_mean(mean, A, b):
    """Compute the mean after affine transformation
    Args:
        mean: `ndarray` of shape (D,), the sample mean vector for some dataset.
        A, b: `ndarray` of shape (D, D) and (D,), affine transformation applied to x
    Returns:
        sample mean vector of shape (D,) after affine transformation.
    """
    # YOUR CODE HERE
    ### Uncomment and edit the code below


#     ### Edit the code below to compute the mean vector after affine transformation
    affine_m = np.zeros(mean.shape) # affine_m has shape (D,)
    affine_m = A@mean + b
    #   ### Update affine_m

#     ###
    return affine_m


def affine_covariance(S, A, b):
    """Compute the covariance matrix after affine transformation

    Args:
        mean: `ndarray` of shape (D,), the sample covariance matrix for some dataset.
        A, b: `ndarray` of shape (D, D) and (D,), affine transformation applied to x

    Returns:
        sample covariance matrix of shape (D, D) after the transformation
    """
    # YOUR CODE HERE
    ### Uncomment and edit the code below
    ### EDIT the code below to compute the covariance matrix after affine transformation
    affine_cov = np.zeros(S.shape)  # affine_cov has shape (D, D)
    affine_cov = A @ S @ A.T

#     ### Update affine_cov

#     ###
    return affine_cov

