# SKILL-ELE-QTO-03: HVAC Power & Mechanical Motors Takeoff ❄️⚙️

> **Engineering guide for quantifying HVAC electrical feeds, outdoor condensing unit isolators, water pumps, elevator motors, and motor control circuits.**

---

## 1. HVAC Power Architecture

HVAC systems require dual-point electrical interfaces:
1. **Indoor Air Handling Unit / Fan Coil Unit (IDU / FCU):** Usually located above the false ceiling in corridors or service areas.
2. **Outdoor Condensing Unit (ODU):** Located on the building roof or exterior wall ledges.

```
HVAC Electrical Circuit Topology:
[Main/Floor DB] ──(Armored Cable / Conduit)──> [Local Weatherproof Isolator] ──(Flexible Conduit)──> [Outdoor Unit (ODU)]
                                                                                                        │
                                                                                 (Multi-Core Control Wire)
                                                                                                        ▼
[Thermostat / Controller] <──(Low Voltage Cable)── [Indoor Concealed Unit (FCU)] <──────────────────────┘
```

---

## 2. Load & Isolator Sizing Matrix

| AC Capacity / System | Phase / Voltage | Full Load Amps (FLA) | Recommended Breaker | Cable Sizing ($N \times \text{mm}^2$) | Local Isolator Rating |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Split Unit 1.5 Ton (18,000 BTU)** | 1-Phase / 230V | 8.5 A | 20A 1P / 2P | $3 \times 4.0 \text{ mm}^2$ | 20A DP IP65 Rotary Isolator |
| **Split Unit 2.0 Ton (24,000 BTU)** | 1-Phase / 230V | 12.0 A | 25A / 30A 1P | $3 \times 4.0 \text{ mm}^2$ | 32A DP IP65 Rotary Isolator |
| **Concealed Ducted 3.0 Ton (36k BTU)**| 1-Phase / 230V | 18.0 A | 32A 1P / 2P | $3 \times 6.0 \text{ mm}^2$ | 40A DP IP65 Rotary Isolator |
| **Concealed Ducted 4.0 - 5.0 Ton** | 3-Phase / 400V | 11.5 A | 20A 3P | $5 \times 4.0 \text{ mm}^2$ | 32A 4P IP65 Rotary Isolator |
| **Package Unit 10.0 Ton** | 3-Phase / 400V | 24.0 A | 40A 3P | $5 \times 10.0 \text{ mm}^2$ | 63A 4P IP65 Rotary Isolator |
| **Domestic Water Lifting Pump (3 kW)**| 3-Phase / 400V | 6.8 A | 16A 3P | $5 \times 2.5 \text{ mm}^2$ | 20A 4P IP65 Isolator + Control Box |
| **Passenger Elevator Motor (11 kW)** | 3-Phase / 400V | 25.0 A | 40A 3P | $5 \times 10.0 \text{ mm}^2$ | 63A 4P Lockable Isolator in Machine Room |

---

## 3. The 3D True Takeoff Derivations for HVAC

### A. The Rooftop Riser Blindspot:
* Outdoor condensing units are often clustered on the roof slab.
* **Vertical Riser Run:**
  $$L_{\text{riser}} = (N_{\text{floors\_to\_roof}}) \times H_{\text{floor\_height}} \approx 3.20 \text{ m per floor}$$
* For an apartment on Floor 1 with ODU on the Roof (Floor 4):
  $$\text{Vertical Riser} = (4 - 1) \times 3.20 = 9.60 \text{ m vertical drop}$$
* **Homerun Conduit:** Heavy-duty rigid UV-resistant PVC or GI conduit in electrical riser shaft + unistrut clamps every 1.5 meters.

### B. Flexible Conduit Connection:
* Rigid conduit must never connect directly to vibrating motors or compressors.
* **Liquid-tight Flexible Metal Conduit (LFMC):** Every motor or outdoor AC unit requires **1.0 to 1.5 meters of PVC-coated flexible galvanized steel conduit** (Ø25mm or Ø32mm) with liquid-tight brass glands.

### C. Control & Thermostat Cabling:
* For each ducted concealed unit:
  * **Thermostat Cable:** $5 \times 1.0 \text{ mm}^2$ or $7 \times 1.0 \text{ mm}^2$ shielded control cable from indoor unit to wall thermostat ($H = +1.50$ m above FFL).
  * **Inter-unit Communication Cable:** $3 \times 1.5 \text{ mm}^2$ screened twisted pair from indoor FCU to rooftop ODU.
