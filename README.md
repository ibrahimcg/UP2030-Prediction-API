# UP2030-Prediction-API

This is a Python client for the UP2030 Prediction API. It allows you to easily make your predictions using our service.

## API Reference
`PredictionAPI(api_url, api_token) `

`api_url`: URL of the prediction API.

`api_token`: Your API token for authentication.

`predict(targets, target_year, data)`

`targets`: List of target features to predict. Possible targets are "Qheating", "iod" and "Qcooling"

`target_year`: The year for which to make predictions.

`data`: List of dictionaries containing input features.

## Required Features

Use the feature names in your inputs as defined here. Order of the input features does not matter, but keep the order consistent per request.

List of required features to make heating predictions: `[ 'verticalPos',
    'formFactor', 'T_heating', 'PPL', 'LPD', 'EPD', 'uWall', 'uWindow',
    'uGroundFloor', 'uRoof', 'SHGC', 'Infiltration', 'n_boiler', 'WWR_N', 'WWR_E', 'WWR_S', 'WWR_W', 'SE_N', 'SE_E', 'SE_S', 'SE_W',
]`

List of required features to make iod predictions: `['verticalPos',
    "formFactor", "UnitID", "WWR_N", "WWR_W", "WWR_S", "WWR_E", "SE_N", "SE_W", "SE_S", "SE_E",
    "T_heating", "PPL", "LPD", "EPD", "uWall", "uWindow", "uRoof", "uGroundFloor", "SHGC",
    "Infiltration", "n_boiler"
]`

List of required features to make qcooling predictions: `['verticalPos',
    'formFactor', 'T_heating', 'PPL', 'LPD', 'EPD', 'uWall', 'uWindow',
    'uGroundFloor', 'uRoof', 'SHGC', 'Infiltration', 'n_boiler', 'WWR_N',
    'WWR_E', 'WWR_S', 'WWR_W', 'SE_N', 'SE_E', 'SE_S', 'SE_W'
]`

## List of Input Features and Their Descriptions

| Abbreviation | Unit | Source | Description | Min | Max |
|--------------|------|--------|-------------|-----|-----|
| **Zone and building level input features** |
| verticalPosition | - | 3D Model | The categorical value that shows floor of each unit (1= for single zone, 2=base, 3=middle, 4=roof) | 1 | 4 |
| formFactor | m2/m3 | 3D Model | The value that indicates the ratio between the external surface area and total volume | 0.014 | 0.939 |
| Uwall | W/m2K | EPC | Thermal conductivity of the wall | 0.15 | 4.2 |
| Uroof | W/m2K | EPC | Thermal conductivity of roof | 0.15 | 3.52 |
| Uground | W/m2K | EPC | Thermal conductivity of ground floor | 0.15 | 3.42 |
| Uwindow | W/m2K | EPC | Thermal conductivity of window | 0.85 | 5.7 |
| WWR | - | EPC | Window to wall ratio from each direction (total 4 direction, north,east,…) | 0 | 100 |
| SE | - | 3D Model | Visible sky ratio from each direction (total 4 direction, north,east,…) | 0 | 100 |
| PPL | people/m2 | Literature | Number of people per square meter | 0.0014 | 0.692 |
| n_boiler | - | Literature | The efficiency of the boiler | 0.8 | 0.95 |
| COP_cooling | - | Literature | The efficiency of cooling | 3 | 5 |
| Infiltration | m3/s-m2 | Literature | - | 0.000285 | 0.0005 |
| SHGC | - | Literature | Solar heat gain coefficient of the window | 0.3 | 0.85 |
| LPD | W/m2 | Literature | Lighting power density | 2.5 | 28 |
| EPD | W/m2 | Literature | Equipment power density | 1.75 | 20 |
| T_heating | °C | Literature | Heating set point | 20 | 23 |
| T_cooling* | °C | Literature | Cooling set point | 25.5 | 28 |
| **Output features** |
| Qheating | kWh/m2 | Simulation | Heating Energy Consumption | - | - |
| Qcooling | kWh/m2 | Simulation | Cooling Energy Consumption | - | - |
| IOD(°C) | °C | Simulation | Indoor Overheating Degree | - | - |

\* If T_cooling == 100, then Qcooling is not calculated in that case. Iod is calculated instead. If T_cooling != 100, then Qcooling is calculated and iod is not.
## Installation

```bash
pip install git+https://github.com/ibrahimcg/UP2030-Prediction-API.git