# --- Begin $MAIN$ program. ---------------
#

# Use Atomic Data Collection from the National Institute of Standards and Technology (NIST)
# Atomic Spectra Database, the CHIANTI atomic database, and some improved atomic data from
# Cloudy v13.04 and pyNeb v1.0
import atomneb
import numpy as np
import os

# Locate datasets
base_dir = os.getcwd()
data_dir = os.path.join('..','atomic-data', 'collection')
atom_elj_file = os.path.join(base_dir,data_dir, 'AtomElj.fits')
atom_omij_file = os.path.join(base_dir,data_dir, 'AtomOmij.fits')
atom_aij_file = os.path.join(base_dir,data_dir, 'AtomAij.fits')


# read Energy Levels (Ej) list
elj_data_list = atomneb.read_elj_list(atom_elj_file)
# read Collision Strengths (Omegaij) list
omij_data_list = atomneb.read_omij_list(atom_omij_file)
# read Transition Probabilities (Aij) list
aij_data_list = atomneb.read_aij_list(atom_aij_file)

# read Energy Levels (Ej) references
elj_data_reference = atomneb.read_elj_references(atom_elj_file)
# read Collision Strengths (Omegaij) references
omij_data_reference = atomneb.read_omij_references(atom_omij_file)
# read Transition Probabilities (Aij) references
aij_data_reference = atomneb.read_aij_references(atom_aij_file)

atom = 'o'
ion = 'iii'
# read Energy Levels (Ej) of O III upto level number 6
oiii_elj_data = atomneb.read_elj(atom_elj_file, atom, ion, level_num=6)
# print Levels of O III
print(oiii_elj_data['j_v'])
# print Energy Levels (cm-1) of O III
print(oiii_elj_data['ej'])

# get citations for Energy Levels (Ej) Reference L7288
citation = atomneb.get_elj_reference_citation(atom_elj_file, 'L7288')
# print citations for Energy Levels (Ej) Reference L7288
print(citation)

atom = 'o'
ion = 'iii'
reference = 'SSB14'
# read Collision Strengths (Omegaij) of O III from Reference SSB14
oiii_omij_data = atomneb.read_omij(atom_omij_file, atom, ion, reference=reference)
# print Level 1 of Collision Strengths (Omegaij) of O III
print(oiii_omij_data['level1'])
# print Level 2 of Collision Strengths (Omegaij) of O III
print(oiii_omij_data['level2'])
# print Strength[1] of Collision Strengths (Omegaij) of O III
print(oiii_omij_data['strength'][0])

atom = 'o'
ion = 'iii'
# list all Collision Strengths (Omegaij) data for O III
list_oiii_omij_data = atomneb.search_omij(atom_omij_file, atom, ion)
# print all Collision Strengths (Omegaij) of O III
print(list_oiii_omij_data)

atom = 'o'
ion = 'iii'
# list all Collision Strengths (Omegaij) references for O III
list_oiii_omij_reference = atomneb.list_omij_references(atom_omij_file, atom, ion)
# print all Collision Strengths (Omegaij) References for O III
print(list_oiii_omij_reference)

atom = 'o'
ion = 'iii'
reference = 'SSB14'
# get citations for Collision Strengths (Omegaij) of O III with reference SSB14
citation = atomneb.get_omij_reference_citation(atom_omij_file, atom, ion, reference)
# print citations for Collision Strengths (Omegaij) of O III with reference SSB14
print(citation)

atom = 'o'
ion = 'iii'
reference = 'FFT04'
# read Transition Probabilities (Aij) of O III with reference FFT04
oiii_aij_data = atomneb.read_aij(atom_aij_file, atom, ion, reference)
# print Transition Probabilities (Aij) of O III with reference FFT04
print(oiii_aij_data['aij'][0])

atom = 'o'
ion = 'iii'
reference = 'FFT04'
# get citations for Transition Probabilities (Aij) of O III with reference FFT04
citation = atomneb.get_aij_reference_citation(atom_aij_file, atom, ion, reference)
# print citations for Transition Probabilities (Aij) of O III with reference FFT04
print(citation)

atom = 'o'
ion = 'iii'
# list all Transition Probabilities (Aij) data for O III
list_oiii_aij_data = atomneb.search_aij(atom_aij_file, atom, ion)
# print all Transition Probabilities (Aij) data for O III
print(list_oiii_aij_data)

atom = 'o'
ion = 'iii'
# list all Transition Probabilities (Aij) references for O III
list_oiii_aij_reference = atomneb.list_aij_references(atom_aij_file, atom, ion)
# print all Transition Probabilities (Aij) references for O III
print(list_oiii_aij_reference)

