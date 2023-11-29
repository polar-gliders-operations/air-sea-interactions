## Investigation on the effect of a change of vapour pressure function formulation on the humidity and latent heat flux output for the COARE 3.5 parameterization.

## Context

- There are 13 formulations for the vapour pressure function (hereinafter referred to as $es$) in AirSeaFluxCode. The default formualtion is Buck2.
- In the AirSeaFluxCode reference paper (Biri et al. 2023) they report the impact of the 12 alternative formulations for $es$ in comparison to the default one for the S88 parameterization. Some significant effect are reported.
- Given that the COARE 3.5 (C35) parameterization is the one widely use in our flux focus group, we focus on this parameterization and investigate if we also observe some significant effect in relation to the change of $e_s$ formulation.
- The data use to conduct the investigation are ship data from the TARSAN cruise which took place in 2022.

## Method

We follow the same method as the one in the AirSeaFluxCode reference paper for the S88 parameterization, but for the C35 parameterization.
In particular, we classify the importance of the change (major, significant, insignificant, negligible, no effect) by using the same threshold as in the paper.

## Results

For all the output studied (the latent heat flux, the specific humidity at sea surface, the specific humidity of air and the 10m neutral specific humidity) there is no significant or major effect caused by a change of saturation vapour pressure function for the C35 parameterization. 