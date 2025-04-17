# Detailed Life Cycle Assessment Methodology for Shared Electric Scooters

## Table of Contents
1. [Introduction and Background](#introduction)
2. [Goal and Scope Definition](#goal-scope)
3. [System Boundaries](#system-boundaries)
4. [Functional Unit](#functional-unit)
5. [Life Cycle Inventory Analysis](#inventory-analysis)
6. [Impact Assessment Methods](#impact-assessment)
7. [Interpretation and Comparative Analysis](#interpretation)
8. [Sensitivity Analysis](#sensitivity)
9. [Limitations and Assumptions](#limitations)

<a id="introduction"></a>
## 1. Introduction and Background

Shared stand-up electric scooters have rapidly emerged as a new urban mobility option in cities worldwide. These battery-powered devices are designed for individual transport over short distances, particularly useful in urban settings due to their small size and dockless operation. Companies operating sharing services make it convenient for users to rent and use these scooters, which are being introduced in large numbers across major European cities.

The technology is promoted as a solution to the "last mile problem" - reducing traffic congestion while offering an environmentally friendly transportation alternative. However, with their rapid deployment, questions have arisen about their actual environmental benefits compared to conventional transport options.

<a id="goal-scope"></a>
## 2. Goal and Scope Definition

### Primary Goals
- Compare environmental impacts, specifically energy use and CO₂ equivalent emissions of shared electric scooters
- Examine the lifecycle Global Warming Potential (GWP) of e-scooter sharing in consideration of reliability characteristics
- Determine whether e-scooter sharing services are environmentally friendly means of transport
- Develop recommendations for more sustainable electric scooter services

### Target Audience
- Manufacturing companies of shared service electric scooters
- Individuals interested in the environmental impacts of electric scooters
- Urban mobility planners and policymakers

### Scope
This study examines the entire life cycle of a typical shared electric scooter including impacts caused by production of primary and secondary materials, components and spare parts, transport, energy consumption in use, and end-of-life treatment. The assessment follows ISO 14044 requirements for a cradle-to-grave analysis.

<a id="system-boundaries"></a>
## 3. System Boundaries

The system boundaries for this LCA include:

### Primary Production
- Raw material extraction and processing
- Secondary material production for components

### Manufacturing Phase
- Component manufacturing (battery, frame, motor, electronics)
- Assembly of components into the final product
- Energy inputs (electricity, heat)

### Transportation Phase
- Transport from manufacturing location (Guangdong, China) to intended use location (Oslo, Norway)
- Transportation methods include rail freight and short-haul aircraft

### Use Phase
- Electricity consumption during charging
- Collection and redistribution activities
- Transportation fuels for collection vehicles

### End-of-Life Phase
- Shredding of decommissioned scooters

Excluded from the study:
- Charging infrastructure
- Routine maintenance (tire replacement, etc.)
- Detailed end-of-life treatment (particularly for batteries)

<a id="functional-unit"></a>
## 4. Functional Unit

The functional unit selected for this study is:

**One passenger over one kilometer traveled by an electric scooter**

This functional unit enables direct comparison with alternative transportation modes. Emissions and energy consumption are presented as:
- gCO₂-eq/passenger-km for emissions
- MJ/km for energy consumption

Assumptions related to the functional unit:
- Average scooter lifespan: 2 years (base scenario)
- Average daily travel distance: 10.2 km
- Total lifetime distance: approximately 7,500 km
- For sensitivity analysis, an alternative 18-month lifespan was also considered

<a id="inventory-analysis"></a>
## 5. Life Cycle Inventory Analysis

### Data Collection and Software
- SimaPro version 9 online software was used for the LCA analysis
- Material and process data from ecoinvent 3.7.1 Cut-off library
- For components without specific e-scooter data (handlebar, wheels, brakes), electric bicycle data was used and manually normalized to appropriate quantities

### Reference Flow Components
The reference flow consists of the following components needed to fulfill the functional unit:
- Battery (NiMH)
- Electric motor
- Glider (stem and deck)
- Two wheels
- One handlebar
- Set of brakes
- Controller

### Transport Calculations
- Distance from Guangdong, China to Berlin, Germany: estimated 10,500 km (rail freight)
- Distance from Berlin to Oslo, Norway: 840 km (short-haul aircraft)
- Distances estimated based on previous studies and Google Maps measurements

### Use Phase Assumptions
- Average distance traveled: 10.2 km per day
- Lifetime of two years (730 days)
- Total lifetime distance: approximately 7,500 kilometers

### End-of-Life Assumptions
- E-scooter is shredded after being decommissioned
- Energy consumption for shredding estimated at 2.7 kWh
- End-of-life emissions taken as 1% of total emissions

### SimaPro Process Modeling
The comprehensive process flow diagrams for manufacturing are included in the report, showing:
- Material inputs
- Energy inputs
- Production processes for all components
- Quantified flows of materials and energy

<a id="impact-assessment"></a>
## 6. Impact Assessment Methods

Four main impact assessment methods were employed to evaluate different environmental categories:

### 1. IPCC 2013 GWP 100a
- Used to assess climate change impact as a factor of global warming potential in terms of CO₂ emissions
- Measures carbon dioxide equivalents (CO₂-eq) of non-CO₂ gases (CH₄, SF₆, HFCs, N₂O, CFCs)
- Uses IPCC characterization factors

### 2. ReCiPe 2016 Midpoint (E)
- Extended version of ReCiPe 2008 method
- Includes both endpoint (damage oriented) and midpoint (problem oriented) impact categories
- Selected the Egalitarian (E) perspective
- Includes 18 impact categories at midpoint level, including:
  - Land use
  - Ozone formation (human health and terrestrial ecosystems)
  - Freshwater eutrophication
  - Fine particulate matter formation
  - Marine/freshwater/terrestrial ecotoxicity
  - Mineral resource scarcity
  - Water consumption
  - Terrestrial acidification
  - Human toxicity (carcinogenic and non-carcinogenic)
  - Global warming

### 3. Cumulative Energy Demand
- Used to calculate total energy demand across the lifecycle
- Characterization factors divided into 5 impact categories based on energy resources:
  - Renewable energy (water, wind/solar/geothermal, biomass)
  - Non-renewable energy (nuclear, fossil, biomass)

### 4. Ecological Scarcity 2013
- Also known as Ecopoints or Umweltbelastungspunkte method
- Weights environmental impacts using "eco-factors"
- Implemented in ecoinvent with 19 unique categories
- Includes normalization, weighting, and characterization per ISO Standard 14044

<a id="interpretation"></a>
## 7. Interpretation and Comparative Analysis

### Life Cycle Interpretation
The results were analyzed primarily in kg CO₂-eq as the biggest contributor to greenhouse gas (GHG) emissions. The analysis was broken down into three main categories:

1. **Manufacturing Emissions** (87.8% of total)
   - NiMH battery: 54.7 kg CO₂-eq (30.2% of manufacturing emissions)
   - Electronic controller: 89.2 kg CO₂-eq (44.6%)
   - Wheels: 15.0 kg CO₂-eq (8.3%)
   - Electric motor: 6.6 kg CO₂-eq (3.6%)
   - Other components (glider, handlebar, brakes): <15% combined

2. **Transport Emissions** (11.15% of total)
   - Train freight: 3.8 kg CO₂-eq (25.2% of transport emissions)
   - Short haul air freight: 17.0 kg CO₂-eq (74%)
   - Note: Air freight is responsible for most emissions despite only accounting for 7.8% of the total distance

3. **End-of-Life Emissions** (1% of total)
   - Approximately 2.04 kg CO₂-eq
   - Based on assumptions from similar studies

### Comparative Analysis with Other Transport Modes
The environmental performance of shared e-scooters was compared to:
- Personal cars
- Public buses
- Walking
- Cycling

The comparison was based on the functional unit (g CO₂-eq/passenger-km) with the following findings:
- E-scooter: 29.5 g CO₂-eq/passenger-km
- Personal car: 257 g CO₂-eq/passenger-km
- Bus: 51 g CO₂-eq/passenger-km

This indicates that e-scooters have 88% lower emissions than cars and 42% lower emissions than buses when considering the full lifecycle impacts.

<a id="sensitivity"></a>
## 8. Sensitivity Analysis

### Service Life Sensitivity
The base scenario assumes a 24-month (2-year) service life for shared e-scooters. And conducted sensitivity analysis for:

- **18-month lifespan**: This reduced lifespan increases emissions to 39.27 g CO₂-eq/passenger-km, a 25% increase

### Transport Route Alternatives
Proposed and analyzed an alternative transport route:
- **Base case**: China to Germany by rail, Germany to Norway by air
- **Alternative**: China to Germany by rail, Germany to Norway port city (Larvik) by ocean freight, final leg by truck
- **Impact**: Transport emissions reduction of 71.7% (from 23 kg CO₂-eq to 6.5 kg CO₂-eq)
- **Total impact**: Overall 7.8% reduction in total lifecycle emissions

### Collection and Distribution Strategies
Based on previous studies, analyzed potential improvements in collection and redistribution:
- Using fuel-efficient vehicles for collection: 12.37% emissions reduction
- Limiting collection to scooters with low battery state: 18.8% emissions reduction
- Reducing driving distance per scooter: potential 27.22% emissions reduction

### Usage Patterns
Examined different usage patterns that affect environmental impact:
- Weekday vs. weekend usage differences
- Trip distance variations: 5% of trips up to 1 km, 25% between 1-3 km, 33% between 4-6 km
- Displacement of other transport modes: 42.1% walking, 28.4% car trips, 27.8% bus trips

<a id="limitations"></a>
## 9. Limitations and Assumptions

### Use Case Assumptions
- Considered the actual distance traveled by the scooter over its lifetime and converted to the functional unit (g CO₂-eq per passenger-kilometer)
- Charging infrastructure was excluded from the study
- Routine maintenance (tire replacement, part replacement) was excluded due to data limitations and short scooter lifespans
- End-of-life treatment was simplified (shredding assumption)

### System Level Assumptions
- Due to lack of manufacturer-specific data, conducted the LCA on a generalized electric scooter rather than a specific model
- Transport calculations assumed manufacturing in Guangdong, China with transport to Berlin, Germany via train and from Berlin to Oslo, Norway via aircraft
- Used data from other major European cities (Paris, Berlin) due to lack of Oslo-specific usage data

### Data Limitations
- Many materials and components were modeled using ecoinvent library data rather than manufacturer-specific data
- Electric bicycle data was adapted for some components (handlebar, wheels, brakes) and normalize