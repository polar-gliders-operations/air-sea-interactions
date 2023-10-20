Paper:

## 1. **Introduction**
- Surface heat and momentum fluxes impact Earth's climate system, influencing atmospheric circulation, wind patterns, and ocean circulation.
- Quantifying these fluxes relies on empirical parameterizations (bulk formulae) using easily measured variables like wind speed and temperatures.
- These variables come from in situ measurements, satellite observations, or reanalysis models.
- Parameterizations use transfer coefficients or surface roughness lengths, often derived from direct but uncertain turbulent flux measurements.
- Accuracy limitations in direct measurements lead to differences in estimated turbulent surface fluxes, especially in high or low wind speeds or stable conditions.
- Climate applications require heat fluxes <10 Wm−2 and momentum fluxes <0.01 Nm−2 on global or basin scales.
- Net heat flux has components: turbulent sensible and latent heat fluxes, net shortwave, and net longwave radiation.
- Uncertainty in each component should ideally be <5 Wm−2, but correlated errors exist.
- Large variations in transfer coefficients, implementation choices, and input uncertainties contribute to turbulent heat flux uncertainty.
- Comparison of bulk flux parameterizations shows discrepancies in derived fluxes due to implementation choices.
- An open-source software package called "AirSeaFluxCode" in Python is introduced, offering ten parameterizations and the ability to compare implementation choices.

## 2. **Methods**

2.1. **Summary of air-sea interaction theory**
- AirSeaFluxCode calculates Turbulent Surface Fluxes (TSF) using bulk measurements of surface state variables (SSV), including near-surface wind speed, air temperature, humidity, and sea surface temperature.
- Parameterizations vary in functions for atmospheric stability, transfer coefficients, roughness lengths, treatment of convective gustiness, required surface water temperature variables, and thermodynamic variables.
- TSF, including wind stress (τ), sensible heat flux (shf), and latent heat flux (lhf), are computed using bulk formulae specific to input measurement heights.
- Transfer coefficients depend on input heights, and Monin-Obukhov Length (L) can be calculated using different methods (Ltsrv or LRb).
- **SSV can be adjusted to a different height (zout) either "bottom-up" using roughness lengths and stability functions or "top-down" using scaling parameters and stability functions.**
- Scalar TSF under low wind speeds may be influenced by convective gusts, accounted for with a gustiness term (ug) in some algorithms.
- Users can choose to remove the effects of gustiness from TSF and wind speeds, with different options available.
- The choice of sea surface temperature measure (bulk or "cool skin") should match the parameterization's requirements.
- Some parameterizations use earth-relative winds, implicitly accounting for surface currents, while others assume surface-relative winds, introducing uncertainties in regions with non-aligned surface currents.

### 2.2. **AirSeaFluxCode calculation methodology**

- Transfer coefficients in AirSeaFluxCode can be specified either at 10 meters in neutral atmospheric conditions or by specifying roughness lengths (z0m for momentum, z0t for temperature, and z0q for moisture). Transfer coefficients can be calculated from the roughness lengths and vice versa.
- A significant source of uncertainty in Turbulent Surface Fluxes (TSF) estimation arises from the wide range of values assigned to transfer coefficients or roughness lengths, particularly at high and low wind speeds.
- Some parameterizations define separate heat transfer coefficients for unstable and stable conditions, introducing further complexity.
- Drag coefficients and heat transfer coefficients in some parameterizations vary with wind speed, requiring extrapolation at high wind speeds to apply them universally.
- AirSeaFluxCode maintains a consistent calculation approach across all parameterizations and quantifies the effects of differences between the code and published descriptions or developer-provided code.
- The code estimates transfer coefficients at measurement heights and stability-dependent flux profiles using an iterative method.
- The user can specify an output height (zout), which may differ from the reference height of 10 meters. The code calculates values at the output and reference heights top-down.
- The code initializes the flux calculation by approximating neutral values of Surface State Variables (SSV) and calculates specific humidity from relative humidity or dew point temperature.
- An iterative process updates various parameters, such as friction velocity (u*), stability functions (Ψx), and transfer coefficients, following an established flowchart.
- Convergence is tested using default tolerance limits for SSV adjusted to 10 meters and neutral stability and calculated TSF. Users can modify tolerance values and choose to test convergence using only TSF or SSV.
- After convergence, the code calculates height-adjusted values of wind speed, temperature, and specific humidity at the user-defined output height (zout).
- If convective gustiness is activated, its effects can be removed from the output TSF and wind speeds as chosen by the user.
- The code records the number of iterations before convergence and flags unphysical values of adjusted SSV.

### 2.3. **AirSeaFluxCode: input parameters, assumptions, user options, and outputs**

- AirSeaFluxCode can be used with various sources of Surface State Variables (SSV), including in-situ data, satellite retrievals, and model output (e.g., atmospheric reanalyses).
- Parameterizations are typically derived from direct flux measurements with sample periods around 30 minutes. Using data averaged over significantly longer or shorter periods can introduce more uncertainty.
- Parameterizations differ in complexity, some requiring additional input parameters (e.g., downwelling radiation) and including extra terms in calculations (e.g., convective gustiness) to better represent air-sea exchange physics.
- Minimum required input SSV for momentum and sensible heat flux calculations include wind speed, near-surface air temperature, and sea surface temperature. Near-surface humidity is needed for latent heat flux calculations, and an estimate of atmospheric pressure may improve accuracy.
- Additional parameters like radiation are needed for cool skin or warm layer adjustments when input parameters differ from the parameterization's expectations.
- AirSeaFluxCode provides flexibility in the selection of input data sources, assuming the necessary adjustments are made to ensure compatibility.
- User options include choosing the saturation vapor pressure function, enabling/disabling convective gustiness, selecting the Monin-Obukhov length calculation method, enabling cool skin and warm layer adjustments, specifying a desired output height, and defining tolerances for convergence criteria.
- Outputs include turbulent surface fluxes (momentum, sensible and latent heat), adjusted SSV at the user-defined output height, adjusted SSV at 10 meters and neutral atmospheric conditions, transfer coefficients, scaling parameters, stability functions, roughness lengths, Monin-Obukhov length, bulk Richardson number, potential temperature, gustiness-related parameters, cool skin/warm layer-related parameters, and quality control flags.
- Users can customize the set of output variables according to their specific needs.
- A comprehensive list of output variables is available in the AirSeaFluxCode documentation.

## 3. **Results**

- AirSeaFluxCode has been tested using two different test datasets: one from observations collected by the Shipboard Automated Meteorological and Oceanographic System (SAMOS) and another from global hourly ERA5 data.
- The ERA5 dataset, which offers global coverage and various conditions, was used for the results discussed in the paper.
- Results are classified into different categories (e.g., no effect, negligible effect, significant effect) based on predefined criteria (Table 8). These categories help evaluate differences in the outputs.
- The paper compares AirSeaFluxCode with four publicly available algorithms: UA, COARE 3.5 (C35), NCAR, and ECMWF.
- Some differences exist between AirSeaFluxCode and the developer code of these algorithms, which are detailed in Sections S7.1 to S7.5 of the Supplementary Material.
- Notably, AirSeaFluxCode uses bulk sea surface temperature as input, and cool skin/warm layer adjustments are switched off, focusing on core flux calculations.
- Gustiness terms are included in the UA, C35, and ECMWF algorithms following the approach of Fairall et al. (2003) to remove the effect of gustiness from certain parameters.
- Relative humidity, calculated from dew point temperature, is used for UA and C35, leading to systematic differences in specific humidity and latent heat flux when compared to NCAR and ECMWF algorithms.
- Significant or major differences in heat fluxes and SSV are observed between AirSeaFluxCode and NCAR due to treatment of thermodynamic variables, methodological differences, and roughness length limits.
- The ECMWF comparison reveals differences related to wind speeds above 17 m/s and constraints on roughness lengths.
- Adopting the approach of the developers for the ECMWF parameterization in AirSeaFluxCode removes significant differences in most cases.
- These comparisons provide valuable insights into the performance and differences of AirSeaFluxCode relative to existing software.

- 3.2.1 **Constant Thermodynamic Variables**: The choice of the form of Г had no impact. However, using a constant air density had serious impacts, causing a systematic increase in heat loss in the tropics and a decrease in higher latitudes, emphasizing that the constant approximation for air density should never be used.

- 3.2.2 **Monin-Obukhov Length Formulation**: Comparing Ltsrv (default) with LRb showed differences in lhf output, especially in cases of low wind speed and extreme stability. LRb enabled data convergence in near-neutral, high wind speed conditions for LP82 and NCAR parameterizations, addressing convergence issues associated with Ltsrv.

- 3.2.3 **Saturation Vapour Pressure Formulations (es)**: Various formulations for es showed no significant differences in most cases, but there was a systematic change in lhf of about 0.2 Wm⁻² in the mean.

- 3.2.4 **Salinity-Related Reduction in q0**: Neglecting the 2% reduction in q to account for seawater salinity had a dramatic impact on lhf. Although not common practice, the choice of reduction percentage can affect results, with changes occurring in about 50% of lhf data for some values.

- 3.2.5 **Cool Skin and Warm Layer Adjustments**: Applying these adjustments had a dramatic effect on heat fluxes. About 50% or more of data showed significant changes in shf and lhf. Parameterization choice should consider available input data (bulk or skin temperature measurements).

- 3.2.6 **Gustiness Term**: The gustiness term impacted all fluxes across different wind speeds. While its effects are typically removed from τ and u10n, some significant differences remained. Applying the gustiness term increased heat fluxes, with the greatest impacts at low wind speeds. Failure rates slightly decreased in most cases, except for S88 and LP82.

- 3.2.7 **Failure Rates**: Combining results from the tests, "failure" rates in AirSeaFluxCode were examined, defined as non-physical u10n, T10n, or q10n results and lack of convergence after 30 iterations. Failure rates were generally small (less than about 0.5%) and increased under low wind speeds and large |10/L| values. Choosing LRb reduced failure rates for LP82 and NCAR parameterizations.


## Recommendations

**Summary of Key Recommendations**

Here are the key recommendations and findings from the analysis conducted in Section 3.2:

### 1. Use Functional Forms for Thermodynamic Variables 
Utilize functional forms for air density, latent heat of evaporation, and specific heat capacity, as approximating these variables with constant values can introduce significant errors.

### 2. Select Parameterizations Based on Input Data 
Choose parameterizations and implementation options that align with the characteristics of your input data. Using inappropriate parameterizations or variables can lead to unintended errors and uncertainties in calculated fluxes.

### 3. Careful Iteration Management 
Set the maximum iteration limit with consideration. Convergence is typically rapid in open ocean conditions but may require more iterations under extreme stability or instability. Be aware that convergence may not always be achievable in extreme conditions.

### 4. Avoid Discontinuities 
Ensure that the underlying functions used in parameterizations do not have discontinuities. Discontinuities can impact convergence and lead to errors in flux calculations.

### 5. Salinity-Related Reduction 
Better constrain and establish the uncertainty of the reduction factor for saturation vapor pressure due to salinity. Include the effects of salinity when calculating saturation vapor pressure, as small changes in the reduction factor can significantly affect latent heat fluxes.

### 6. Evaluate Ad Hoc Constraints 
Carefully assess the impact of ad hoc constraints often used in developer codes. While these constraints may prevent unphysical outputs in extreme conditions, they can also influence fluxes and related meteorological parameters.

### 7. Evaluate Gustiness Inclusion 
Thoroughly evaluate the inclusion of convective gustiness in parameterizations. While gustiness is justified to produce non-zero heat fluxes at low wind speeds, it can significantly impact fluxes at moderate and high wind speeds and introduce inconsistencies in output parameters.

### 8. Consider Computational Demands 
Be aware that the code may have higher computational demands due to strict tolerance criteria for convergence testing. Users can adjust tolerance criteria or iteration limits to trade off computational requirements with result uncertainty.

### 9. Output Options 
Users can choose between different output options, such as flagging data that have not converged or outputting all data, depending on the specific application's requirements.

### 10. Future Developments 
The code will be regularly expanded and updated to include new parameterizations, extend calculations to incorporate sea state effects, and develop uncertainty estimates. Collaboration, bug reports, corrections, and comments from the community are welcomed.

These recommendations emphasize the importance of selecting appropriate parameterizations and options, understanding the impact of choices on flux calculations, and maintaining careful iteration management and consideration of variables to ensure accurate and meaningful results in air-sea flux calculations.
