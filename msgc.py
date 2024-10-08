# -*- coding: utf-8 -*-
"""MSGC.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pzj5yu9jDR0fi4OU93l-QInxizsmC6iq

# **Molecule Structure Generation from Compound Name Using Python**
"""

!pip install rdkit

!pip install pubchempy

# Import necessary libraries
import pubchempy as pcp
from rdkit import Chem
from rdkit.Chem import Draw

def get_smiles_from_name(compound_name):
    """
    Get SMILES string from the compound name using PubChemPy.
    Args:
    compound_name (str): The name of the compound.

    Returns:
    str: The SMILES string of the compound.
    """
    try:
        # Search for the compound in PubChem
        compound = pcp.get_compounds(compound_name, 'name')

        if not compound:
            print("Compound not found.")
            return None

        # Get SMILES string of the first result
        smiles = compound[0].isomeric_smiles
        return smiles
    except Exception as e:
        print(f"Error: {e}")
        return None

def draw_molecule(smiles, output_image="molecule.png"):
    """
    Generate and save a 2D structure of the molecule from SMILES.
    Args:
    smiles (str): SMILES string representing the molecule.
    output_image (str): Output image file name (PNG).
    """
    if smiles:
        # Convert SMILES string to RDKit molecule object
        mol = Chem.MolFromSmiles(smiles)

        # Generate 2D image of the molecule
        img = Draw.MolToImage(mol, size=(300, 300))

        # Save image to file
        img.save(output_image)
        print(f"Structure saved as {output_image}")
    else:
        print("Invalid SMILES string. Cannot draw molecule.")

if __name__ == "__main__":
    # Input: compound name from user
    compound_name = input("Enter the name of the compound: ")

    # Get SMILES string from compound name
    smiles = get_smiles_from_name(compound_name)

    if smiles:
        print(f"SMILES: {smiles}")
        # Draw and save the molecule structure
        draw_molecule(smiles)
    else:
        print("Could not generate structure.")

