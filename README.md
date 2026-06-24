# physics-sandbox

A personal physics simulation lab. Each simulation lives in its own folder
with isolated parameters, logic, and charts.

## Structure
```
physics-sandbox/
├── simulations/
│   └── <simulation_name>/
│       ├── config.py
│       ├── sim.py
│       ├── plotter.py
│       └── README.md
├── core/
├── data/
├── outputs/
├── requirements.txt
└── README.md
```

## Setup

```bash
pip install -r requirements.txt
```

## Running a simulation

Navigate into the simulation folder and run:

```bash
cd simulations/<simulation_name>
python sim.py
```

## Simulations

| # | Name | Status |
|---|---|---|
| 01 | Projectile Motion | Done |
| 02 | Pendulum | Done |

## Author

[Engr. Kirk Alyn Santos](https://github.com/kirkalyn13)

## License

[MIT](https://choosealicense.com/licenses/mit/)