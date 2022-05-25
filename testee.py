#Generate samples from Rayleigh distribution
#Rayleigh.MC(x, sigma, m = 10000, antithetic = TRUE)

#Nakagami
#x=runif(10,min=0,max=1)
#dnakagami(x)
#pnakagami(x)
#varnakagami(x)
#esnakagami(x)

#rice
dRice(1, nu=c(0.1, 0.5, 0.9), sigma=10)
pRice(c(0.1, 0.5, 0.9), nu=0.5, sigma=10)
qRice(0.5, nu=0.5, sigma=c(5, 10, 15))
rRice(5, nu=0.5, sigma=10)
