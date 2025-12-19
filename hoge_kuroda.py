import numpy as np

def hoge_kuroda_method(A, b, x0=None, tol=1e-10, max_iter=1000):
    """
    Solve the linear system Ax = b using the Hoge-Kuroda iterative method.

    Parameters:
    A : ndarray
        Coefficient matrix (must be square).
    b : ndarray
        Right-hand side vector.
    x0 : ndarray, optional
        Initial guess for the solution. If None, a zero vector is used.
    tol : float, optional
        Tolerance for convergence.
    max_iter : int, optional
        Maximum number of iterations.

    Returns:
    x : ndarray
        Approximate solution vector.
    """
    n = A.shape[0]
    if x0 is None:
        x0 = np.zeros(n)
    
    x = x0.copy()
    
    for iteration in range(max_iter):
        x_old = x.copy()
        
        for i in range(n):
            sum1 = np.dot(A[i, :i], x[:i])
            sum2 = np.dot(A[i, i+1:], x_old[i+1:])
            x[i] = (b[i] - sum1 - sum2) / A[i, i]
        
        # Check for convergence
        if np.linalg.norm(x - x_old, ord=np.inf) < tol:
            print(f'Converged in {iteration+1} iterations.')
            return x
    
    print('Maximum iterations reached without convergence.')
    return x

