# This program solves fifth-degree polynomial equations using Newton’s method.

Newton’s method is a method to approximate solutions to an equation f(x) = 0 very quickly. 

It works by starting with a (more-or-less random) guess x0 for a solution, and then coming up with better and better approximations x1, x2, x3, etc., using the following process:

x1 = x0 − f(x0)/f0
(x0)

x2 = x1 − f(x1)/f0
(x1)

x3 = x2 − f(x2)/f0
(x2)

And so on and so forth, with xn+1 = xn − f(xn)/f0(xn) in general. x1 will usually be close to a solution, and x2 will be closer, and x3 closer still, etc.

Time for an example: Let’s try to solve x 2 − 4x + 1 = 0. Here, f(x) = x
2 − 4x + 1. We start with a guess of x0 = 1.

Then x0 = 1; f(x0) = −2; f
0
(x0) = −2; and so
x1 = 1 − (−2)/(−2) = 0.

Then x1 = 0; f(x1) = 1; f
0
(x1) = −4; and so
x2 = 0 − (1)/(−4) = 0.25.

Then:
x3 = 0.25 − f(0.25)/f0
(0.25) = 0.267857142 (approximately).

Then:
x4 = 0.267857142 − f(0.267857142)/f0
(0.267857142) = 0.267949190 (approximately).
