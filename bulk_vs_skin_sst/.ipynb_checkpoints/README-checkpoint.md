# Air-Sea Flux Analysis: Setting bulk temperature as skin

For most of out platforms, we only measure bulk SST, while C3.5 requires the input to be skin SST, unless we supply SW and LW observations as well. From the paper (Bire et al., 2023) it's clear that setting the cool skin off will have a significant to major effect on turbulent heat flux. What does this look like for our data?

Could/should we use ERA5 data to complement our observations that lack SW/LW? Should we use something other than COARE 3.5? 


Note:
    From ERA5: ´This parameter is a mean over a particular time period (the processing period) which depends on the data extracted. For the reanalysis, the processing period is over the 1 hour ending at the validity date and time.´  


## Methodology

Compare our ship data for C35 when setting bulk SST as skin SST without cool skin adjustment, and with and without warm layer on.

## Results

![Air-Sea Flux Analysis Results](bulk_vs_skin_analysis.png)

