from cdo import Cdo
cdo = Cdo()

gridfile        = 'cdo_config/icon_eu_grid2.txt' # Textovy subor, ktory popisuje rozlisenie gridu
weightfile      = 'cdo_config/weights_icogl2world_0125_EUAU2.nc' # Subor vygenerovany pomocou CDO vyuzitim textoveho suboru a dalsich suborov od ECMWF


input_file      = 'data/icon_global_icosahedral_pressure-level_2020021200_000_1000_RELHUM.grib2' # vstupny grib2 subor (to su tie stiahnute odzipovane)
output_file     = 'skuska.grib' # vystupny subor, ktory bude dalej vstupovat do Python scriptu

# Premapovanie raw suborov do gridu specifikovaneho subormi vyssie
cdo.remap(gridfile,weightfile,input = input_file, output = output_file) #python
