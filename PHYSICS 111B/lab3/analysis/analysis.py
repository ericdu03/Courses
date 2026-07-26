import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as opt
import os
import glob

def f1(x):
    return 1/np.cosh(np.log(x)/2.403)

def f2(x):
    return 1 - ((1 - x)/(1 + x))**2 * np.log(2)/2 - ((1 - x)/(1 + x))**4 * (np.log(2)**2/4 - np.log(2)**3/12)

def compute_rho(R1, R2, d, f):
    return np.pi * d/np.log(2) * (R1 + R2)/2 * f(R1/R2)

def compute_RH(V, I, B, d):
    return ((V * d)/(I * B)).to_numpy()

def linear(x, m, b):
    return m * x + b

def exp(x, alpha):
    return x**alpha

def zero_interp(x, y):
    zero_crossings = np.where(np.diff(np.sign(y)))[0]
    x1, x2 = x[zero_crossings], x[zero_crossings + 1] 
    y1, y2 = y[zero_crossings], y[zero_crossings + 1]
    return x1 - y1 * (x2 - x1) / (y2 - y1)

def analyze(filename):
    data = pd.read_csv(f'{filename}.csv', skiprows = [0, 1, 2], delimiter = '\t')
    data.dropna(axis = 1, how = 'all', inplace = True)
    if filename == '45uA':
        data.drop(labels = np.arange(30), axis = 0, inplace = True)
    # display(data)

    nonzero_field = np.abs(data['B-Field (Gauss)']) > 50
    nonzero_table = data.where(nonzero_field).dropna()

    I_AB = nonzero_table['sample I AB']
    I_BA = nonzero_table['sample I -AB']

    I_AD = nonzero_table['sample I AD']
    I_DA = nonzero_table['sample I -AD']

    I_AC = nonzero_table['sample I AC']
    I_CA = nonzero_table['sample I -AC']

    I_BD = nonzero_table['sample I BD']
    I_DB = nonzero_table['sample I -BD']

    V_AC = nonzero_table['Voltage AC']
    V_CA = nonzero_table['Voltage -AC']

    V_BD = nonzero_table['Voltage BD']
    V_DB = nonzero_table['Voltage -BD']

    V_BC = nonzero_table['Voltage BC']
    V_CB = nonzero_table['Voltage -BC']

    V_DC = nonzero_table['Voltage DC']
    V_CD = nonzero_table['Voltage -DC']

    field = nonzero_table['B-Field (Gauss)']
    T = nonzero_table['Temperature (K)']
    
    
    R_ABDC = V_DC/I_AB
    R_ABDC_neg = -V_CD/I_BA
    
    R_ADBC = V_BC/I_AD
    R_ADBC_neg = -V_CB/I_DA
    
    
    d = 1.25e-3
    e = 1.6e-19
    rho = compute_rho(R_ABDC, R_ADBC, d, f1)
    
    rho2 = compute_rho(-R_ABDC_neg, -R_ADBC_neg, d, f1)

    rho = np.mean([rho, rho2], axis = 0)

    RH = np.array([compute_RH(V_AC, I_BD, field, d), compute_RH(V_BD, I_AC, field, d), compute_RH(V_DB, I_CA, field, d), compute_RH(V_CA, I_DB, field, d)])
    # print(RH)
    # RH2 = compute_RH(V_BD, I_AC, field, s)

    plt.figure()
    plt.scatter(1/T[field > 0], np.mean(RH, axis = 0)[field > 0], s = 2, c = 'orange')
    plt.scatter(1/T[field < 0], np.mean(RH, axis = 0)[field < 0], s = 2, c = 'blue')
    plt.title(f"$R_H$ vs 1/T at {filename}") 
    plt.xlabel('1/T [1/K]')
    plt.ylabel("$R_H$")
    plt.legend(['Field > 0', 'Field < 0'])
    plt.savefig(fname = f'../writeup/images/{filename}-rh-plot.png', bbox_inches = 'tight')
    # plt.show()
    plt.close()
    
    plt.figure()
    plt.scatter(1/T[field >0], rho[field > 0], s = 2, c = 'orange')
    plt.scatter(1/T[field < 0], rho[field < 0], s = 2, c = 'blue')
    plt.legend(['Field > 0', 'Field < 0'])
    plt.xlabel('T [K]')
    plt.ylabel('$\\rho$')
    plt.title(f"$\\rho$ vs. 1/T plot at {filename}")
    plt.savefig(fname = f'../writeup/images/{filename}-rho-plot1.png')
    plt.close()

    plt.figure()
    plt.scatter(1/T[field >0], 1/rho[field > 0], s = 2, c = 'orange')
    plt.scatter(1/T[field < 0], 1/rho[field < 0], s = 2, c = 'blue')
    plt.legend(['Field > 0', 'Field < 0'])
    plt.xlabel('1/T [1/K]')
    plt.ylabel('$1/\\rho$')
    plt.title(f"$1/\\rho$ vs. 1/T plot at {filename}")
    plt.savefig(fname = f'../writeup/images/{filename}-rho-plot2.png')
    plt.close()

    plt.scatter(np.mean(RH, axis = 0)[field > 0], np.mean([V_AC, V_BD, -V_CA, -V_DB], axis = 0)[field > 0], s = 2, c = 'orange')
    plt.scatter(np.mean(RH, axis = 0)[field < 0], np.mean([V_AC, V_BD, -V_CA, -V_DB], axis = 0)[field < 0], s = 2, c = 'blue')
    plt.legend(['Field > 0', 'Field < 0'])
    plt.title("V vs. RH")
    plt.close()
    
    RH_avg = np.mean(RH, axis = 0)

    p = -1/(RH_avg * e) # computes the hole mobility in extrinsic regime
    mu_p = 1/(rho * e * p)
    fit, cov = opt.curve_fit(exp, T[T < 230], mu_p[T < 230])
    alpha_fit = fit
    alpha_err = np.sqrt(np.diag(cov))
    
    # chisq = np.sum((mu_p - exp(T, alpha_fit))**2/exp(T, alpha_fit))

    x_vals = np.linspace(np.min(T), np.max(T), 200)
    plt.figure()
    plt.scatter(T, mu_p, s = 2, c = 'orange')
    plt.plot(x_vals, exp(x_vals, alpha_fit))
    plt.legend(['Data', 'Fit'])
    plt.title(f"$\\mu_p$ vs. T at {filename}")
    plt.xlabel("T [K]")
    plt.ylabel("$\\mu_p$")
    plt.text(np.max(T) - 80, np.max(mu_p) - 3e-5, f"$\\alpha$ = {np.round(alpha_fit[0], 3)} \u00b1 {np.round(alpha_err[0], 4)}")
    # plt.text(np.max(T) - 80, np.max(mu_p) - 4e-5, f"$\\chi^2$: {np.round(chisq, 3)} ")
    plt.savefig(fname = f'../writeup/images/{filename}-mu-plot.png', bbox_inches = "tight")
    plt.close()
    
    plt.figure()
    plt.scatter(T[field > 0], -RH_avg[field > 0] * 1/rho[field > 0], s = 2, c = 'orange')
    plt.scatter(T[field < 0], -RH_avg[field < 0] * 1/rho[field < 0], s = 2, c = 'blue')
    plt.legend(['Field > 0', 'Field < 0'])
    plt.xlabel('T [K]')
    plt.ylabel('$\\mu_H$')
    plt.title('$\\mu_H$ vs. T at 30uA')
    # plt.savefig(fname = f'../writeup/images/{filename}-hall-mobility.png', bbox_inches = "tight")
    plt.close()


    
    
    
    N_a = np.mean(p[T < 200])
    T_zero = zero_interp(T.values, RH_avg)[0]

    sigma_e = T_zero**alpha_fit * e * N_a
    sigma_0 = np.interp(x = T_zero, xp = T, fp = 1/rho)

    b = 1/(1 - sigma_e/sigma_0)
    n = N_a/(b**2 - 1)
    
    
    plt.scatter(T[field > 0], R_ABDC[field > 0], s = 2, c = 'orange')
    plt.scatter(T[field < 0], R_ABDC[field < 0], s = 2, c = 'blue')

    zero_table = data.where(~nonzero_field).dropna()
    V_DC_zero = zero_table['Voltage DC']
    I_AB_zero = zero_table['sample I AB']
    temp_zero = zero_table['Temperature (K)']

    plt.scatter(temp_zero, V_DC_zero/I_AB_zero, s = 2, c = 'green')
    plt.title('$R_{AB, DC}$ vs. Temperature at 30uA')
    plt.xlabel('Temperature [K]')
    plt.ylabel('$R_{AB, DC}$')
    plt.legend(['Field > 0', 'Field < 0', 'Field = 0'])
    # plt.savefig(fname = f'../writeup/images/{filename}-resistance.png', bbox_inches = "tight")
    plt.close()
    
    R_ACBD = V_BD/I_AC

    plt.scatter(T[field > 0], R_ACBD[field > 0], s = 2, c = 'orange')
    plt.scatter(T[field < 0], R_ACBD[field < 0], s = 2, c = 'blue')

    V_BD_zero = zero_table['Voltage BD']
    I_AC_zero = zero_table['sample I AC']
    temp_zero = zero_table['Temperature (K)']

    plt.scatter(temp_zero, V_BD_zero/I_AC_zero, s = 2, c = 'green')
    plt.title('$R_{AC, BD}$ vs. Temperature at 30uA')
    plt.xlabel('Temperature [K]')
    plt.ylabel('$R_{AC, BD}$')
    plt.legend(['Field > 0', 'Field < 0', 'Field = 0'])
    # plt.savefig(fname = f'../writeup/images/{filename}-trans-resistance.png', bbox_inches = "tight")
    plt.close()
    
    return alpha_fit, alpha_err, N_a, n

# path = os.getcwd()
p_vals = []
n_vals = []
alpha_fit1 = []
alpha_err1 = []
for file in glob.glob("*.csv"):
    alpha_fit, alpha_err, p, n = analyze(file[:-4])
    print(file, p, n[0])
    p_vals.append(p)
    n_vals.append(n[0])
    alpha_fit1.append(alpha_fit)
    alpha_err1.append(alpha_err)
print(f"p_vals: {p_vals}")
print(f"n_vals: {n_vals}")
print(f"n + p: {np.array(n_vals) + np.array(p_vals)}")
print(f"")

print(np.mean(alpha_fit1), np.sqrt(np.sum((alpha_err/len(alpha_fit))**2)))
    