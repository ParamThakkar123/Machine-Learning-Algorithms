# Neural Ordinary Differential Equation

- Instead of specifying a discrete sequence of hidden layers, we parameterize the derivative of the hidden state using a neural network.
- The output of the neural network is computed using a black box differential equation solver.
- These continuous depth models have constant memory cost, adapth their evaluation strategy to each input, and can explicitly trade numerical precision for speed.

Definining and evaluating models using ODE solvers has several benefits:
- Memory Efficiency : We can computer gradients of a scalar valued loss with respect to all inputs of any ODE solver, without backpropagating through the operations of the solver. Not storing any intermediate quantities of the forward pass allows us to train our models with constant memory cost as a function of depth, a major bottleneck of training deep models.

- Adaptive computation: Euler's method is perhaps the simplest method for solvign ODEs. Modern ODE solvers provide guarantees about the growth of approximation error, monitor the level of error, and adapt their evaluation strategy on the flyto acheive the requested level of accuracy.  This allows the cost of evaluating a model to scale with
problem complexity. After training, accuracy can be reduced for real-time or low-power applications.

- Scalable and invertible normalizing flows
- Continuous time-series models: Unlike recurrent neural networks, which require discretizing observation and emission intervals, continuously-defined dynamics can naturally incorporate data which arrives at arbitrary times. 