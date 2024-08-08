import numpy as np
from tqdm import tqdm
import pandas as pd
from matplotlib import pyplot as plt
from scipy.signal import find_peaks


def PID(Kp=1, Ti=1, Td=1, t_initial=0, u_bar=0, control_type='pid'):
    """Basic PID controller

    args:
    - Kp (int or float) default: 1 = proportional gain
    - Ti (int or float) default: 1 = integral period
    - Td (int or float) default: 1 = derivative period
    - t_initial (int or float) default: 0 = initial time
    - u_bar (int or float) default: 0 = base line for control signal
    - control_type (str) default: 'pid' = choose control type, i.e. either 'p' (proportional only), 'pi' (proportional and integral), 'pd' (proportional and derivative), or 'pid' (full PID)
    yield:
    - u (float) = control signal
    generator send():
    - t, feedback, ref (list-like type) = time, feedback (output from model), and reference
    """
    # check if control_type inputted correctly
    if not (control_type == 'p' or control_type == 'pi' or control_type == 'pd' or control_type == 'pid'):
        raise ValueError("'control_type' arg only accepts either 'p', 'pi', 'pd', or 'pid'")

    # initialize stored data
    e_prev = 0
    t_prev = t_initial
    I = 0

    # initial control
    u = u_bar

    while True:
        # yield MV, wait for new t, PV, SP
        t, feedback, ref = yield u

        # calculate error, delta error, and delta time
        e = ref - feedback
        de = e - e_prev
        dt = t - t_prev

        # define variables for PID
        P = Kp * e
        I = I + e * dt
        D = de / dt

        # calculate u based on control_type selected
        if control_type == 'p':
            u = u_bar + P
        elif control_type == 'pi':
            u = u_bar + Kp * (e + (1 / Ti) * I)
        elif control_type == 'pd':
            u = u_bar + Kp * (e + Td * D)
        else:
            u = u_bar + Kp * (e + (1 / Ti) * I + Td * D)

        # update stored data for next iteration
        e_prev = e
        t_prev = t


def car_dynamics(b, v_in, u, m, dt):
    """Vehicle dynamics model

    args:
    - a (int or float) = acceleration (m/s^2)
    - b (int or float) = friction constant (Nm/s)
    - v_in (int or float) = input/initial speed (m/s)
    - u (int or float) = control signal (N)
    - m (int or float) = vehicle mass (kg)
    - dt (int or float) = difference of time (s)
    return:
    v_out (float) = output/final speed (m/s)
    """
    a = (-b * v_in + u) / m
    v_out = a * dt + v_in #vout = at + vin
    return v_out


# define constants
Kp = 500
Ti = 0.5
Td = 0.1
control_type = 'pid'
mass = 1000  # kg
frict = 50  # Nm/s

# declare PID controller
controller = PID(Kp=Kp, Ti=Ti, Td=Td, control_type=control_type)
controller.send(None)  # initialize controller

# set speed reference
ref = np.ones(shape=50) * 5
# define useful array variables
feedback = np.zeros(shape=ref.shape)
times = np.arange(start=1, stop=len(ref), step=1)
u = np.zeros(shape=ref.shape)
error = np.zeros(shape=ref.shape)
t_prev = 0  # buffer to store previous time

# loop through each time t
for t in tqdm(times):
    error[t] = ref[t - 1] - feedback[t - 1]  # get error at time t
    u[t] = controller.send([t, feedback[t - 1], ref[t - 1]])  # calculate PID
    feedback[t] = car_dynamics(b=frict, v_in=feedback[t - 1], u=u[t], m=mass, dt=t - t_prev)  # calculate model output
    t_prev = t  # store for next iteration


'''
Control type 'p':
Kp = 975.0
Ti = _
Td = _

Control type 'pi':
Kp = 877.5
Ti = 1.6
Td = _

Control type 'pd':
Kp = 1560.0
Ti = _
Td = 0.25

Control type 'classic_pid':
Kp = 1170.0
Ti = 1.0
Td = 0.25

Control type 'pessen_integral_rule':
Kp = 1365.0
Ti = 0.8
Td = 0.3

Control type 'some_overshoot':
Kp = 643.5
Ti = 1.0
Td = 0.66

Control type 'no_overshoot':
Kp = 390.0
Ti = 1.0
Td = 0.66



'''

# load necessary libraries


# define constants
Kp = 1950
mass = 1000  # kg
frict = 50  # Nm/s

##################################################
#### STEP 1: USE PROPORTIONAL ONLY ####
#### REPEAT THIS 1ST STEP UNTIL GETTING CONTINUOUS OSCILLATIONS ####

# declare PID controller
controller = PID(Kp=Kp, control_type='p')
controller.send(None)  # initialize controller

# set speed reference
ref = np.ones(shape=50) * 5

# define useful array variables
feedback = np.zeros(shape=ref.shape)
times = np.arange(start=1, stop=len(ref), step=1)
u = np.zeros(shape=ref.shape)
error = np.zeros(shape=ref.shape)

t_prev = 0  # buffer to store previous time

# loop through each time t
for t in tqdm(times):
    error[t] = ref[t - 1] - feedback[t - 1]  # get error at time t
    u[t] = controller.send([t, feedback[t - 1], ref[t - 1]])  # calculate PID
    feedback[t] = car_dynamics(b=frict, v_in=feedback[t - 1], u=u[t], m=mass, dt=t - t_prev)  # calculate model output
    t_prev = t  # store for next iteration





##################################################
#### STEP 2: GET Ku & Tu AND CALCULATE Kp, Ti, Td ####

# find peaks in feedback signal
peaks, _ = find_peaks(feedback)  # get idx of peaks
print('peaks:', feedback[peaks])

# get Ku and Tu
Tu = np.mean(np.diff(peaks))
Ku = Kp
print('Ku =', Ku)
print('Tu =', Tu)
print()

print(f"aku adalah J{Ku}")
# calculate Kp, Ti, Td using different control type
pid_control_type = {'p': [0.5 * Ku, 0, 0],
                    'pi': [0.45 * Ku, 0.8 * Tu, 0],
                    'pd': [0.8 * Ku, 0, 0.125 * Tu],
                    'pid': [0.6 * Ku, 0.5 * Tu, 0.125 * Tu]}


##################################################
#### STEP 3: RUN ALL CONTROLLER TYPES USING CONSTANTS JUST OBTAINED ####

# buffer
ref_list = []
feedback_list = []
MSE_list = []
MAE_list = []
RMSE_list = []

# loop each control_type
for key, value in pid_control_type.items():
    # get constants
    Kp = value[0]
    Ti = value[1]
    Td = value[2]

    # set control_type arg for PID function
    if key == 'p' or key == 'pi' or key == 'pd':
        control_type = key
    else:
        control_type = 'pid'



    # declare PID controller
    controller = PID(Kp=Kp, Ti=Ti, Td=Td, control_type=control_type)
    controller.send(None)  # initialize controller

    # set speed reference
    ref = np.concatenate((np.ones(shape=50) * 2, np.ones(shape=50) * 10))

    # define useful array variables
    feedback = np.zeros(shape=ref.shape)
    times = np.arange(start=1, stop=len(ref), step=1)
    u = np.zeros(shape=ref.shape)
    error = np.zeros(shape=ref.shape)

    t_prev = 0  # buffer to store previous time

    # loop through each time t
    for t in times:
        error[t] = ref[t - 1] - feedback[t - 1]  # get error at time t
        u[t] = controller.send([t, feedback[t - 1], ref[t - 1]])  # calculate PID
        feedback[t] = car_dynamics(b=frict, v_in=feedback[t - 1], u=u[t], m=mass,
                                   dt=t - t_prev)  # calculate model output
        t_prev = t  # store for next iteration

    # store ref and feedback
    ref_list.append(ref)
    feedback_list.append(feedback)

    # MSE
    print('==================================================')
    print(f"Control type: {key}")
    print('==================================================')
    mse = np.mean(np.square(error))
    print(f"Mean squared error: {round(mse, 3)}")
    MSE_list.append(mse)

    # MAE
    mae = np.mean(np.absolute(error))
    print(f"Mean absolute error: {round(mae, 3)}")
    MAE_list.append(mae)

    # RMSE
    rmse = np.sqrt(np.mean(np.square(error)))
    print(f"Root mean square error: {round(rmse, 3)}")
    RMSE_list.append(rmse)

##################################################
#### PLOT ALL 7 CONTROLLERS RESULTS ####
##################################################
#### CREATE DATAFRAME FOR MSE, MAE, RMSE ####

