
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
        
    
