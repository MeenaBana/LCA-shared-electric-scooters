# Life Cycle Assessment of Shared Electric Scooters
This repository contains a comprehensive life cycle assessment (LCA) of shared electric scooters, examining their environmental impacts through a cradle-to-grave analysis.

## 📋 Project Overview
This project was conducted as part of the "Adapting Technology to the Circular Economy" course in the Master in Green Energy Technology program at Østfold University College. The study investigated the environmental footprint of shared electric scooters through detailed life cycle assessment by analyzing:

- Raw material extraction and processing
- Manufacturing of components (battery, frame, motor, electronics)
- Transportation and distribution impacts
- Use phase emissions
- End-of-life considerations

The assessment was carried out using SimaPro 9 with the ecoinvent 3.7.1 Cut-off library for material and process data.

## 🔍 Key Research Questions

- Are shared e-scooters an environmentally friendly alternative to conventional transportation methods?
- What are the environmental impacts across the entire lifecycle of shared e-scooters?
- How do shared e-scooters compare to other urban mobility options in terms of emissions?
- Which lifecycle phases contribute most significantly to the overall environmental impact?
- How can the environmental footprint of shared e-scooter services be reduced?

## 📊 Methodology

### Functional Unit and Scope
The functional unit defined in the study was one passenger over one kilometer traveled by an electric scooter, with emissions and energy consumption presented as gCO2-eq/km and MJ/km respectively.

The system boundaries include impacts from:

- Production of primary and secondary materials
- Component manufacturing (battery, motor, glider, wheels, etc.)
- Transportation from manufacturing location to use location
- Use phase energy consumption
- End-of-life treatment

### Life Cycle Inventory
The assessment followed ISO 14044 requirements, using:

- Manufacturing data from ecoinvent 3.7.1 Cut-off library
- Transportation data based on estimated routes (China to Europe)
- Average lifetime of two years (7,500 km total distance)
- Average daily travel distance of 10.2 km

### Impact Assessment Methods
Four primary impact assessment methods were employed:

- IPCC 2013 GWP 100a: Climate change impact as CO₂ equivalents
- ReCiPe 2016 Midpoint (E): Multiple impact categories including land use, toxicity, acidification
- Cumulative Energy Demand: Energy resource consumption across different energy types
- Ecological Scarcity 2013: Environmental impacts weighted using eco-factors

## 🔬 Key Findings

1. **Total Emissions:** The analysis found that a shared electric scooter produces approximately 29.5 g CO₂-eq/passenger-km, which is:
    - 88% less emissions compared to passenger cars (257 g CO₂-eq/passenger-km)
    - 42% less emissions compared to buses (51 g CO₂-eq/passenger-km)

2. **Manufacturing Dominance:** The manufacturing phase accounts for 87.8% of total lifecycle emissions:
    - NiMH battery production contributes 54.7 kg CO₂-eq (30.2% of manufacturing emissions)
    - Electronic controller contributes 44.6 kg CO₂-eq (24.6%)
    - Wheels and electric motor contribute 15.0 and 6.6 kg CO₂-eq respectively

3. **Transport Impact:** Transportation contributes 11.15% of total emissions:
    - Air freight, while only 7.8% of the transport distance, is responsible for 74% of transport emissions
    - Train freight accounts for 25.2% of transport emissions

4. **Lifespan Sensitivity:** Scooter lifespan significantly affects environmental performance:
    - Reducing lifespan from 24 to 18 months increases emissions by 25% (to 39.27 g CO₂-eq/passenger-km)
    - Longer lifespans and more durable construction are critical for sustainability

5. **Urban Transport Behavior:** Shared e-scooters are replacing several transport modes:
    - 42.1% replacing walking trips over 500m
    - 28.4% replacing car trips
    - 27.8% replacing bus trips

## 📝 Recommendations
Based on the analysis, the following recommendations are suggested to help reduce the environmental impact of shared e-scooter services:

### Optimizing Operational Scenarios

1. **Reducing collection and distribution distances** for charging
2. **Using more efficient vehicles** for collection activities (can reduce emissions by 12.37%)
3. **Implementing selective collection strategies** - only collecting scooters with low battery (can reduce emissions by 18.8%)
4. **Reducing driving distance per scooter** (potential 27.22% emissions reduction)

### Alternative Transport Routes
An alternative transport route that reduces transport emissions by 71.7%:
- Maintain rail freight from China to Hamburg
- Use ocean freight from Hamburg to Larvik
- Use truck transport for the final leg to Oslo

### Manufacturing Improvements
- Pursue more robust builds with longer service lives
- Develop better battery recycling and end-of-life management

## 📈 Future Work

- Include charging infrastructure in the assessment
- Expand analysis of routine maintenance impacts
- Conduct more detailed end-of-life scenarios for batteries
- Investigate potential for renewable energy charging
- Analyze policy interventions to improve shared mobility sustainability