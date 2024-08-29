
from scipy.constants import c

def addONA(process, λstart,λend,np,ports, x, y):

    """
    Parameters:
        process(ModuleType): Lumerical API used.
        λstart(float): Inital wavelength value.
        λstop(float): Final wavelength value.
        np(int): Number of simulation points.
        ports(int): Number of output ports.
        x(int): Ona x Position
        y(int): Ona y Position
    """

    process.addelement('Optical Network Analyzer')
    process.set('input parameter','start and stop')
    process.set({'number of points'     : np,
                 'number of input ports': ports,
                 'start frequency'      : c/λstart, 
                 'stop frequency'       : c/λend,
                 'x position'           : x,
                 'y position'           : y})

def ConnectONA(process, ONA, component, connections):

    """
    Parameters:
        process(ModuleType): Lumerical API used.
        ONA(string): Name of the ONA.
        component(string): Name of the component.
        connections(int): array with connection orders.
    """
    process.connect(ONA,'output', component,'port '+ str(connections[0]))

    for i in range(1,(len(connections))):
        process.connect(ONA,'input '+str(i), component,'port '+str(connections[i]))
        
    
def Connectcomponents(process, component1, connections1, component2, connections2):

    """
    Parameters:
        process(ModuleType): Lumerical API used.
        component1(string): Name of the component 1.
        component2(string): Name of the component 2.
        connections1(int): array with the connection ports of the component 1.
        connections2(int): array with the connection ports of the component 2.
    """
    if (len(connections1)!=len(connections2)):
        print('invalid connection, component 1 has', len(connections1), 'connections and component 2 has', len(connections2), 'connections')
        return 0;

    for i in range(len(connections1)):
        process.connect(component1,'port '+str(connections1[i]), component2,'port '+str(connections2[i]))
        
    
def GenerateHexMZI(Loss: float, process: str, theta_matrix: list[list[float]]):
    """
    GenerateHexMZI is a function that simulates a hexagonal MZI (Mach-Zehnder Interferometer) setup.
    
    Parameters:
    - Loss (float): A floating-point number representing the loss on each MZI.
    - process (ModuleType): Lumerical API used.
    - theta_matrix (list[list[float]]): A 2D list (6x2 matrix) where each row contains two floating-point numbers representing thetaA and thetaB in radians.
    
    Returns:
    None
    """
    
    process.addelement('MZI_HEX')
    process.set('Loss',Loss)

    # Set the phase of the MZIs
    for i, (thetaA, thetaB) in enumerate(theta_matrix):
        process.set('Theta'+str(i+1)+'_A', thetaA)
        process.set('Theta'+str(i+1)+'_B', thetaB)
    
    
    
