from matplotlib import pyplot as plt

def plot_graphs(j_pos, j_vel, j_suction, ef_pos):
    '''Reveives joint position and joint velocity in array format'''
    figure = plt.figure(figsize=[15, 4.5])
    figure.subplots_adjust(left=0.05, bottom=0.11, right=0.97, top=0.9, wspace=0.4, hspace=0.55)

# Still need to optimize ylim of all graphs

    ax_joint_pos = figure.add_subplot(241)
    ax_joint_pos.set_title("Joint Position")
    ax_joint_pos.plot(t, j_pos[0], '-o', lw=2, label='Joint 1')
    ax_joint_pos.plot(t, j_pos[1], '-g', lw=2, label='Joint 2')
    ax_joint_pos.plot(t, j_pos[2], '-r', lw=2, label='Joint 3')
    ax_joint_pos.plot(t, j_pos[3], '-b', lw=2, label='Joint 4')  # Not sure if we should include the 4th joint in this?
    ax_joint_pos.set_ylim(-2., 2.)
    ax_joint_pos.legend()

    ax_joint_vel = figure.add_subplot(242)
    ax_joint_vel.set_title("Joint Velocity")
    ax_joint_vel.plot(t, j_vel[0], '-o', lw=2, label='Joint 1')
    ax_joint_vel.plot(t, j_vel[1], '-g', lw=2, label='Joint 2')
    ax_joint_vel.plot(t, j_vel[2], '-r', lw=2, label='Joint 3')
    ax_joint_vel.plot(t, j_vel[3], '-b', lw=2, label='Joint 4')
    ax_joint_vel.set_ylim(-2., 2.)
    ax_joint_vel.legend()


    ax_sucky = figure.add_subplot(243)
    ax_sucky.set_title("Suction Status")
    ax_sucky.plot(t, suction, '-b', lw=3, label='EF Suction')
    ax_sucky.set_ylim(-2., 2.)
    ax_sucky.legend()

    # EF joint poisition
    ax_adj_j4 = figure.add_subplot(244)
    ax_adj_j4.set_title("theta 4 Position")
    ax_adj_j4.plot(t, j_pos(4), '-b', lw=3, label='EF Position')
    ax_adj_j4.set_ylim(-2., 2.)
    ax_adj_j4.legend()

    # Ef position (pos vs t)
    ax_ef_pos = figure.add_subplot(245)
    ax_ef_pos.set_title("EF Position")
    ax_ef_pos.plot(t, ef_pos[0], '--r', lw=4, label='X')
    ax_ef_pos.plot(t, ef_pos[1], '--r', lw=4, label='Y')
    ax_ef_pos.plot(t, ef_pos[2], '--r', lw=4, label='Z')
    ax_ef_pos.set_ylim(-10., 10.)
    ax_ef_pos.legend()


    # EF Position(3d)
    ax_3d_pos = figure.add_subplot(246, projection='3d')
    ax_3d_pos.set_title("EF Position 3D")
    ax_3d_pos.plot(ef_pos[0], ef_pos[1], ef_pos[2], lw=2, label='t')
    ax_3d_pos.legend()

    plt.show()

def mk8CSV(time, x, y, z):
    import pandas as pd
    from pathlib import Path

    df = pd.DataFrame({'time': time,
                      'x': x, 
                      'y': y,
                      'z': z})

    df.to_csv('./derp.csv', index=True)
    