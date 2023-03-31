'''
Suffering.py 
Python file containing the calculation part of the project
Built with Blood, Tear, Sanity and large amount of Caffeine
Coded by Pruek Suwankosai  6301023620118
     and Napat Vacharayoo 6301023620053

พ้มขอโต้ดกั๊บปี้ จะไม่ทำอีกแล้วกั๊บปี๊
'''
import numpy as np
import math as m

global L1,L2,L3,L4

L1 = 0.088
L2 = 0.135
L3 = 0.2067
L4 = 0.0815
 

def DHmodpain(alpha,a,d,theta): # matrix which modified DH parameters will be filled in
    return np.matrix(([np.cos(theta)              , -np.sin(theta)             , 0             , a               ],
                      [np.sin(theta)*np.cos(alpha), np.cos(theta)*np.cos(alpha), -np.sin(alpha), -d*np.sin(alpha)],
                      [np.sin(theta)*np.sin(alpha), np.cos(theta)*np.sin(alpha), np.cos(alpha) , d*np.cos(alpha) ],
                      [0                          , 0                          , 0             , 1               ]))
    
    
def fwdkinec(t1,t2,t3): # forward kinamatics
    print("UwU")
    t4 = -(t2+t3)
    t5 = -t1
    
    DHparam = np.array(((0  , 0     , L1     , t1         ),
                        (-90, 0     , 0      , t2-90      ),
                        (0  , L2    , 0      , t3+90-t2   ),
                        (0  , L3    , 0      , -t3        ),
                        (90 , 0     , 0      , -t1        ),
                        (0  , 0     , -L4    , 0          )))
    
    T01 = DHmodpain(np.radians(DHparam[0][0]), DHparam[0][1], DHparam[0][2], np.radians(DHparam[0][3]))
    T12 = DHmodpain(np.radians(DHparam[1][0]), DHparam[1][1], DHparam[1][2], np.radians(DHparam[1][3]))
    T23 = DHmodpain(np.radians(DHparam[2][0]), DHparam[2][1], DHparam[2][2], np.radians(DHparam[2][3]))
    T34 = DHmodpain(np.radians(DHparam[3][0]), DHparam[3][1], DHparam[3][2], np.radians(DHparam[3][3]))
    T45 = DHmodpain(np.radians(DHparam[4][0]), DHparam[4][1], DHparam[4][2], np.radians(DHparam[4][3]))
    T56 = DHmodpain(np.radians(DHparam[5][0]), DHparam[5][1], DHparam[5][2], np.radians(DHparam[5][3]))
    
    T06 = T01*T12*T23*T34*T45*T56
    T06 = np.round(T06,5)
    T06[T06 == -0] = 0
    return T06


def globaltoFrame(x,y,z):
    print("Aligning...")
    P = np.matrix(([x],[y],[z],[1]))
    TG0 = np.matrix(([ 0,  1, 0, 1.5  ],
                     [-1,  0, 0, 0    ],
                     [ 0,  0, 1, -0.05 ],
                     [ 0,  0, 0, 1    ]))
    P_ref_0 = TG0*P
    P_ref_0 = np.round(P_ref_0,5)
    P_ref_0[P_ref_0 == -0] = 0
    return P_ref_0

def frametoGlobal(x,y,z):
    print("Aligning...")
    P = np.matrix(([x],[y],[z],[1]))
    TG0 = np.matrix(([ 0, -1, 0, 0    ],
                     [ 1,  0, 0, -1.5 ],
                     [ 0,  0, 1, 0.05 ],
                     [ 0,  0, 0, 1    ]))
    P_ref_0 = TG0*P
    P_ref_0 = np.round(P_ref_0,5)
    P_ref_0[P_ref_0 == -0] = 0
    return P_ref_0


def invkinec(x,y,z):
    print("OwO")
    theta1 = m.atan2(y,x)
    r1 = m.sqrt(x**2+y**2)
    
    r3 = (z+L4)-L1
    r2 = m.sqrt(r1**2+r3**2)
    alpha = m.atan2(r3,r1)
    cosbeta = (L2**2+r2**2-L3**2)/(2*L2*r2)
    sinbeta = m.sqrt(1-cosbeta**2)
    beta = m.atan2(sinbeta,cosbeta)
    theta2 = np.radians(90)-(alpha+beta)
    
    gamma = np.radians(180) - np.radians(90) - theta2
    cosdelta = (L2**2+L3**2-r2**2)/(2*L2*L3)          
    sindelta = m.sqrt(1-cosdelta**2)
    delta = m.atan2(sindelta,cosdelta)
    theta3 = np.radians(180) - (gamma+delta)
    bruh = np.matrix(([np.round(np.degrees(theta1),0),np.round(np.degrees(theta2),0),np.round(np.degrees(theta3),0)]))
    bruh[bruh == -0] = 0
    return bruh


if __name__ == '__main__':
    
    death = fwdkinec(0,20,0)
    print(death)
    purgatory = globaltoFrame(0,-1.2698,0.1894)
    print(purgatory)
    rebirth = invkinec(0.25287,0, 0.13336)
    print (rebirth)
    
#=====================CODE ABYSS========================
#====================DO NOT ENTER=======================

#This is from when we try to accompany matlab in the code. Didn't end well. Unreadable. 

# def fwdkinec (t1,t2,t3,t4):
#     return np.matrix(([m.cos((m.pi*t4)/180)*(m.cos((m.pi*t1)/180)*m.cos((m.pi*(t2 - 90))/180)*m.cos((m.pi*(t3 + 90))/180) - m.cos((m.pi*t1)/180)*m.sin((m.pi*(t2 - 90))/180)*m.sin((m.pi*(t3 + 90))/180)) - m.sin((m.pi*t1)/180)*m.sin((m.pi*t4)/180), - m.cos((m.pi*t4)/180)*m.sin((m.pi*t1)/180) - m.sin((m.pi*t4)/180)*(m.cos((m.pi*t1)/180)*m.cos((m.pi*(t2 - 90))/180)*m.cos((m.pi*(t3 + 90))/180) - m.cos((m.pi*t1)/180)*m.sin((m.pi*(t2 - 90))/180)*m.sin((m.pi*(t3 + 90))/180)), m.cos((m.pi*t1)/180)*m.cos((m.pi*(t2 - 90))/180)*m.sin((m.pi*(t3 + 90))/180) + m.cos((m.pi*t1)/180)*m.cos((m.pi*(t3 + 90))/180)*m.sin((m.pi*(t2 - 90))/180), (27*m.cos((m.pi*t1)/180)*m.cos((m.pi*(t2 - 90))/180))/200 + (2067*m.cos((m.pi*t1)/180)*m.cos((m.pi*(t2 - 90))/180)*m.cos((m.pi*(t3 + 90))/180))/10000 - (163*m.cos((m.pi*t1)/180)*m.cos((m.pi*(t2 - 90))/180)*m.sin((m.pi*(t3 + 90))/180))/2000 - (163*m.cos((m.pi*t1)/180)*m.cos((m.pi*(t3 + 90))/180)*m.sin((m.pi*(t2 - 90))/180))/2000 - (2067*m.cos((m.pi*t1)/180)*m.sin((m.pi*(t2 - 90))/180)*m.sin((m.pi*(t3 + 90))/180))/10000],
# [m.cos((m.pi*t1)/180)*m.sin((m.pi*t4)/180) + m.cos((m.pi*t4)/180)*(m.sin((m.pi*t1)/180)*m.cos((m.pi*(t2 - 90))/180)*m.cos((m.pi*(t3 + 90))/180) - m.sin((m.pi*t1)/180)*m.sin((m.pi*(t2 - 90))/180)*m.sin((m.pi*(t3 + 90))/180)),   m.cos((m.pi*t1)/180)*m.cos((m.pi*t4)/180) - m.sin((m.pi*t4)/180)*(m.sin((m.pi*t1)/180)*m.cos((m.pi*(t2 - 90))/180)*m.cos((m.pi*(t3 + 90))/180) - m.sin((m.pi*t1)/180)*m.sin((m.pi*(t2 - 90))/180)*m.sin((m.pi*(t3 + 90))/180)), m.sin((m.pi*t1)/180)*m.cos((m.pi*(t2 - 90))/180)*m.sin((m.pi*(t3 + 90))/180) + m.sin((m.pi*t1)/180)*m.cos((m.pi*(t3 + 90))/180)*m.sin((m.pi*(t2 - 90))/180), (27*m.sin((m.pi*t1)/180)*m.cos((m.pi*(t2 - 90))/180))/200 + (2067*m.sin((m.pi*t1)/180)*m.cos((m.pi*(t2 - 90))/180)*m.cos((m.pi*(t3 + 90))/180))/10000 - (163*m.sin((m.pi*t1)/180)*m.cos((m.pi*(t2 - 90))/180)*m.sin((m.pi*(t3 + 90))/180))/2000 - (163*m.sin((m.pi*t1)/180)*m.cos((m.pi*(t3 + 90))/180)*m.sin((m.pi*(t2 - 90))/180))/2000 - (2067*m.sin((m.pi*t1)/180)*m.sin((m.pi*(t2 - 90))/180)*m.sin((m.pi*(t3 + 90))/180))/10000],
# [                                                                     -m.cos((m.pi*t4)/180)*(m.cos((m.pi*(t2 - 90))/180)*m.sin((m.pi*(t3 + 90))/180) + m.cos((m.pi*(t3 + 90))/180)*m.sin((m.pi*(t2 - 90))/180)),                                                                         m.sin((m.pi*t4)/180)*(m.cos((m.pi*(t2 - 90))/180)*m.sin((m.pi*(t3 + 90))/180) + m.cos((m.pi*(t3 + 90))/180)*m.sin((m.pi*(t2 - 90))/180)),                                   m.cos((m.pi*(t2 - 90))/180)*m.cos((m.pi*(t3 + 90))/180) - m.sin((m.pi*(t2 - 90))/180)*m.sin((m.pi*(t3 + 90))/180),                                                                             (163*m.sin((m.pi*(t2 - 90))/180)*m.sin((m.pi*(t3 + 90))/180))/2000 - (163*m.cos((m.pi*(t2 - 90))/180)*m.cos((m.pi*(t3 + 90))/180))/2000 - (2067*m.cos((m.pi*(t2 - 90))/180)*m.sin((m.pi*(t3 + 90))/180))/10000 - (2067*m.cos((m.pi*(t3 + 90))/180)*m.sin((m.pi*(t2 - 90))/180))/10000 - (27*m.sin((m.pi*(t2 - 90))/180))/200 + 11/125],
# [                                                                                                                                                                                         0,                                                                                                                                                                                            0,                                                                                                                                   0,                                                                                                                                                                                                                                                                                                                                                                             1]))

# def fwdkinec (t1,t2,t3,t4):
#     return np.matrix(([m.m.cos((m.m.pi*t4)/180)*(m.m.cos((m.m.pi*t1)/180)*m.m.cos((m.m.pi*(t2 - 90))/180)*m.m.cos((m.m.pi*(t3 - 90))/180) + m.m.cos((m.m.pi*t1)/180)*m.m.sin((m.m.pi*(t2 - 90))/180)*m.m.sin((m.m.pi*(t3 - 90))/180)) - m.m.sin((m.m.pi*t1)/180)*m.m.sin((m.m.pi*t4)/180), - m.m.cos((m.m.pi*t4)/180)*m.m.sin((m.m.pi*t1)/180) - m.m.sin((m.m.pi*t4)/180)*(m.m.cos((m.m.pi*t1)/180)*m.m.cos((m.m.pi*(t2 - 90))/180)*m.m.cos((m.m.pi*(t3 - 90))/180) + m.m.cos((m.m.pi*t1)/180)*m.m.sin((m.m.pi*(t2 - 90))/180)*m.m.sin((m.m.pi*(t3 - 90))/180)), m.m.cos((m.m.pi*t1)/180)*m.m.cos((m.m.pi*(t3 - 90))/180)*m.m.sin((m.m.pi*(t2 - 90))/180) - m.m.cos((m.m.pi*t1)/180)*m.m.cos((m.m.pi*(t2 - 90))/180)*m.m.sin((m.m.pi*(t3 - 90))/180), (27*m.m.cos((m.m.pi*t1)/180)*m.m.cos((m.m.pi*(t2 - 90))/180))/200 + (4017*m.m.cos((m.m.pi*t1)/180)*m.m.cos((m.m.pi*(t2 - 90))/180)*m.m.cos((m.m.pi*(t3 - 90))/180))/20000 + (3*m.m.cos((m.m.pi*t1)/180)*m.m.cos((m.m.pi*(t2 - 90))/180)*m.m.sin((m.m.pi*(t3 - 90))/180))/100 - (3*m.m.cos((m.m.pi*t1)/180)*m.m.cos((m.m.pi*(t3 - 90))/180)*m.m.sin((m.m.pi*(t2 - 90))/180))/100 + (4017*m.m.cos((m.m.pi*t1)/180)*m.m.sin((m.m.pi*(t2 - 90))/180)*m.m.sin((m.m.pi*(t3 - 90))/180))/20000],
#                      [m.m.cos((m.m.pi*t1)/180)*m.m.sin((m.m.pi*t4)/180) + m.m.cos((m.m.pi*t4)/180)*(m.m.sin((m.m.pi*t1)/180)*m.m.cos((m.m.pi*(t2 - 90))/180)*m.m.cos((m.m.pi*(t3 - 90))/180) + m.m.sin((m.m.pi*t1)/180)*m.m.sin((m.m.pi*(t2 - 90))/180)*m.m.sin((m.m.pi*(t3 - 90))/180)),   m.m.cos((m.m.pi*t1)/180)*m.m.cos((m.m.pi*t4)/180) - m.m.sin((m.m.pi*t4)/180)*(m.m.sin((m.m.pi*t1)/180)*m.m.cos((m.m.pi*(t2 - 90))/180)*m.m.cos((m.m.pi*(t3 - 90))/180) + m.m.sin((m.m.pi*t1)/180)*m.m.sin((m.m.pi*(t2 - 90))/180)*m.m.sin((m.m.pi*(t3 - 90))/180)), m.m.sin((m.m.pi*t1)/180)*m.m.cos((m.m.pi*(t3 - 90))/180)*m.m.sin((m.m.pi*(t2 - 90))/180) - m.m.sin((m.m.pi*t1)/180)*m.m.cos((m.m.pi*(t2 - 90))/180)*m.m.sin((m.m.pi*(t3 - 90))/180), (27*m.m.sin((m.m.pi*t1)/180)*m.m.cos((m.m.pi*(t2 - 90))/180))/200 + (4017*m.m.sin((m.m.pi*t1)/180)*m.m.cos((m.m.pi*(t2 - 90))/180)*m.m.cos((m.m.pi*(t3 - 90))/180))/20000 + (3*m.m.sin((m.m.pi*t1)/180)*m.m.cos((m.m.pi*(t2 - 90))/180)*m.m.sin((m.m.pi*(t3 - 90))/180))/100 - (3*m.m.sin((m.m.pi*t1)/180)*m.m.cos((m.m.pi*(t3 - 90))/180)*m.m.sin((m.m.pi*(t2 - 90))/180))/100 + (4017*m.m.sin((m.m.pi*t1)/180)*m.m.sin((m.m.pi*(t2 - 90))/180)*m.m.sin((m.m.pi*(t3 - 90))/180))/20000],
#                      [                                                                      m.m.cos((m.m.pi*t4)/180)*(m.m.cos((m.m.pi*(t2 - 90))/180)*m.m.sin((m.m.pi*(t3 - 90))/180) - m.m.cos((m.m.pi*(t3 - 90))/180)*m.m.sin((m.m.pi*(t2 - 90))/180)),                                                                        -m.m.sin((m.m.pi*t4)/180)*(m.m.cos((m.m.pi*(t2 - 90))/180)*m.m.sin((m.m.pi*(t3 - 90))/180) - m.m.cos((m.m.pi*(t3 - 90))/180)*m.m.sin((m.m.pi*(t2 - 90))/180)),                                   m.m.cos((m.m.pi*(t2 - 90))/180)*m.m.cos((m.m.pi*(t3 - 90))/180) + m.m.sin((m.m.pi*(t2 - 90))/180)*m.m.sin((m.m.pi*(t3 - 90))/180),                                                                             (4017*m.m.cos((m.m.pi*(t2 - 90))/180)*m.m.sin((m.m.pi*(t3 - 90))/180))/20000 - (3*m.m.cos((m.m.pi*(t2 - 90))/180)*m.m.cos((m.m.pi*(t3 - 90))/180))/100 - (27*m.m.sin((m.m.pi*(t2 - 90))/180))/200 - (4017*m.m.cos((m.m.pi*(t3 - 90))/180)*m.m.sin((m.m.pi*(t2 - 90))/180))/20000 - (3*m.m.sin((m.m.pi*(t2 - 90))/180)*m.m.sin((m.m.pi*(t3 - 90))/180))/100 + 11/125],
#                      [                                                                                                                                                                                         0,                                                                                                                                                                                            0,                                                                                                                                   0,                                                                                                                                                                                                                                                                                                                                                                       1]))

# def invkinec (x,y,z): # First iteration if invkinec. Cursed beyond believe
    
#     zp = (z+L4-L1)
#     r1 = m.sqrt((x**2 + y**2))
#     r2 = m.sqrt(r1**2 + zp**2)
#     theta1 = m.atan2(y,x)
#     alpha = m.atan2(zp,r1)
#     cosbeta = ((L2**2)+(r2**2)-(L3**2))/(2*L2*r2)
#     betapos =  m.atan2(m.sqrt(1-cosbeta**2),cosbeta)
#     betaneg =  m.atan2(-m.sqrt(1-cosbeta**2),cosbeta)
#     theta2_pos = (m.pi/2) - (alpha + betapos) 
#     theta2_neg = (m.pi/2) - (alpha + betaneg) 
#     sint3 = (L2**2 + L3**2 - r2**2) / (2*L2*L3)
#     theta3_pos = m.atan2(sint3,m.sqrt(1-sint3**2))
#     theta3_neg = m.atan2(sint3,-m.sqrt(1-sint3**2))
#     theta4 = -theta1
#     print(zp)
#     # print((180/m.pi)*alpha)
#     # print((180/m.pi)*betaneg)
#     # jumble = np.array([theta1,theta2_pos,theta3_pos,theta4])
#     jumble = np.array(([theta1,theta2_pos,theta3_pos,theta4],
#                     [theta1,theta3_pos,theta3_neg,theta4],
#                     [theta1,theta2_neg,theta3_pos,theta4],
#                     [theta1,theta2_neg,theta3_neg,theta4]))
#     return np.round(((180/m.pi)*jumble),2)