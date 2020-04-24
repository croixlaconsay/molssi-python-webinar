"""
This modcule has functions associated with analyzing the geometry of a molecule.

It can be run as a script with an xyz file.
"""

# Let's put all of this code into one box

import os
import numpy as np
import argparse

def open_xyz(xyz_filename):
    """
    This function will open the xyz file
    Input: xyz file
    Return: symbols, coordinates (2 things!)
    """
    # let's open and read in the file
    xyz_file = np.genfromtxt(fname=xyz_filename, skip_header=2, delimiter='', dtype='unicode')
    # now let's read in the symbols and coordinates
    symbols = xyz_file[:,0]
    coordinates = xyz_file[:,1:]
    coordinates = coordinates.astype(np.float)
    return symbols, coordinates

def calculate_distance(atom1_coord, atom2_coord):
    """
    Calculates the distance between two points in 3D space.
    Inputs: coordinates of two atoms
    Return: distance between the atoms
    """
    x_distance = atom1_coord[0] - atom2_coord[0]
    y_distance = atom1_coord[1] - atom2_coord[1]
    z_distance = atom1_coord[2] - atom2_coord[2]
    atom_distance = np.sqrt(x_distance**2 + y_distance**2 + z_distance**2)
    return atom_distance

def bond_check(distance, minimum_length=0, maximum_length=1.5):
    """
    This function checks the bond length output and
    sees if it's between 0 an 1.5 Angstrom
    """
    if distance > minimum_length and distance <= maximum_length:
        return True
    else:
        return False
    
# How to tell python this is the start of the code (always after functions portion)

if __name__ == "__main__":
    
    # Here's we'll call in argparse ArgumentParser
    # argparse allows the user to specify what xyz file to analyze
    parser = argparse.ArgumentParser(description='This script analyzes a user given xyz file and outputs the length of the bonds.')

    # ask user what file they want to read in
    parser.add_argument('xyz_file', help="The file path for the xyz file to analyze.")

    # parse_args() saves the users input variables into args
    args = parser.parse_args()


    xyzfilename = args.xyz_file


    # open_xyz function returns two things, so we need to define them
    symbols, coordinates = open_xyz(xyzfilename)
    num_atoms = len(symbols)
    for num1 in range(0,num_atoms):
        for num2 in range(0,num_atoms):
            if num1<num2:
                atom_distance = calculate_distance(coordinates[num1], coordinates[num2])
                if bond_check(atom_distance) is True:
                    print(F' {symbols[num1]} to {symbols[num2]} : {atom_distance: .3f} Angstroms ')