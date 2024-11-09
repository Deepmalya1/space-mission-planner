import matplotlib.pyplot as plt
import numpy as np

def plot_mission_timeline(phase_times, phase_labels):

    # Create the timeline plot
    fig, ax = plt.subplots(figsize=(10, 6))
    
    ax.plot(phase_times, np.zeros_like(phase_times), 'ro')  
    for i, label in enumerate(phase_labels):
        ax.text(phase_times[i], 0.1, label, ha='center', va='bottom', fontsize=12)
    
    ax.set_ylim(-0.5, 0.5)  
    ax.set_xlabel('Mission Time (Days)')
    ax.set_yticks([])  
    ax.set_title('Space Mission Phases')
    
    plt.grid(True)
    plt.show()

# Example usage
phase_times = [0, 100, 200, 300, 400]  
phase_labels = ['Launch', 'Periapsis', 'Apoapsis', 'Orbital Insertion', 'Arrival']
plot_mission_timeline(phase_times, phase_labels)
