"""
tkinter
"""

import argparse
# ArgumentParser 객체 생성
parser = argparse.ArgumentParser(description='Process some parameters.')

parser.add_argument('--output_index', type=int, default=1, help='use multiprocessing')

# 11개 파라미터에 대한 인자 전달
parser.add_argument('--beta_lower', type=float, default=0.275, help='Lower bound for beta')
parser.add_argument('--beta_upper', type=float, default=0.4, help='Upper bound for beta')

parser.add_argument('--alphamin_lower', type=float, default=3.3, help='Lower bound for alpha_min')
parser.add_argument('--alphamin_upper', type=float, default=5.0, help='Upper bound for alpha_min')

parser.add_argument('--alphamax_lower', type=float, default=0.3, help='Lower bound for alpha_max')
parser.add_argument('--alphamax_upper', type=float, default=40.0, help='Upper bound for alpha_max')

parser.add_argument('--rsmax_lower', type=float, default=256, help='Lower bound for Rs_max')
parser.add_argument('--rsmax_upper', type=float, default=256, help='Upper bound for Rs_max')

parser.add_argument('--rsmin_lower', type=float, default=117, help='Lower bound for Rs_min')
parser.add_argument('--rsmin_upper', type=float, default=117, help='Upper bound for Rs_min')

parser.add_argument('--imax_lower', type=float, default=1.23E-03, help='Lower bound for I_max')
parser.add_argument('--imax_upper', type=float, default=1.23E-03, help='Upper bound for I_max')

parser.add_argument('--imin_lower', type=float, default=1.80E-06, help='Lower bound for I_min')
parser.add_argument('--imin_upper', type=float, default=1.80E-06, help='Upper bound for I_min')

parser.add_argument('--v0s_lower', type=float, default=0.05, help='Lower bound for V_0s')
parser.add_argument('--v0s_upper', type=float, default=0.35, help='Upper bound for V_0s')

parser.add_argument('--v0r_lower', type=float, default=0.05, help='Lower bound for V_0r')
parser.add_argument('--v0r_upper', type=float, default=0.3, help='Upper bound for V_0r')

parser.add_argument('--t0s_lower', type=float, default=80, help='Lower bound for T_0s')
parser.add_argument('--t0s_upper', type=float, default=8.00E+06, help='Upper bound for T_0s')

parser.add_argument('--t0r_lower', type=float, default=10, help='Lower bound for T_0r')
parser.add_argument('--t0r_upper', type=float, default=2200, help='Upper bound for T_0r')

# 인자 파싱
args = parser.parse_args()

import time

# 파싱된 인자 사용
for arg, value in vars(args).items():
    print(f'{arg}: {value}')
    time.sleep(1)
