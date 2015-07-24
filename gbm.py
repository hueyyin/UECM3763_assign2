import pylab as p
import numpy as np

# Setup parameters

mu = 0.1; sigma = 0.26;
S0 = 39 # Initial price
n_path = 1000 # Simulate 1000 runs
n = n_partitions = 1000 # 1000 partitions within interval



# Create Brownian paths

t = p.linspace(0, 3, n+1) # Partition [0,3] to 1000 partitions
dB = p.randn(n_path, n+1) / p.sqrt(n);
dB[:,0] = 0 # First column of dB is 0
B = dB.cumsum(axis=1) # Cummulative sum



# Calculate stock prices

nu = mu - sigma*sigma/2.0
S = p.zeros_like(B);
S[:,0] = S0
S[:, 1 :] = S0*p.exp(nu*t[1:]+sigma*B[:, 1 :])



# Plot 5 realizations of GBM

S_plot= S[0:5]
p.plot(t,S_plot.transpose());
p.xlabel('Time, $t$');
p.ylabel('Stock prices, $S_t$');
p.show()



# Calculate the expectation value and variance of S(3)

S3 = p.array(S[:,-1])
E_S3 = np.mean(S3)
Var_S3 = np.var(S3)
print('Expected Value: E[S(3)] = ' + str(E_S3))
print('Variance: Var[S(3)] = ' + str(Var_S3))



# Calculate P[S(3)> 39]

Prob = sum(S3 > 39) / len(S3 > 39)
print('P[S(3)> 39] = ' + str(Prob))



# Calculate E[S(3) | S(3) > 39]

Exp = sum(S3 * (S3 > 39)) / sum(S3 > 39)
print('E[S(3) | S(3) > 39] = ' + str(Exp))
