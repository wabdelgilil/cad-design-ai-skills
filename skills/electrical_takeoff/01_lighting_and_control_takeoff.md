# SKILL-ELE-QTO-01: Lighting System & Control Takeoff 💡

> **Engineering guide for quantifying luminaires, linear LED coves, control switches, and deriving true 3D conduit and wiring lengths.**

---

## 1. Luminaire Taxonomy & Classification Rules

Every luminaire must be quantified with its full electrical and mounting profile:

### A. Point Luminaires (Spotlights & Downlights):
* **Recessed Spotlights (Dry Areas):** LED 7W / 10W / 15W, CRI $\ge 80$, CCT 3000K/4000K, IP20 with deep baffle to suppress glare (UGR $< 19$).
* **Waterproof Spotlights (Wet Areas):** Bathrooms (Zone 1 & 2), Kitchens, Balconies, and Exterior Canopies must be **IP44 / IP65 rated with silicone gasket**.
* **Inground / Exterior Uplights:** Die-cast aluminum IP67 with tempered glass for tree/facade illumination.

### B. Linear & Decorative Luminaires:
* **Linear Cove LED Strips (حصر بالمتر الطولي L.M):**
  - High-density strip (120 or 240 LEDs/m), 10W to 14.4W per linear meter, 24V DC.
  - **The Driver Multiplier:** 1 LED Electronic Driver (100W / 150W IP20 or IP67) for every **7 to 10 linear meters** of continuous cove.
  - **The Profile Rule:** Every 1.0 m of LED strip requires **1.0 m of anodized aluminum extrusion channel with frosted PMMA diffuser** to dissipate heat and prevent LED burnout.
* **Wall Appliques (أبليكات):** Fixed at $+1.80$ m to $+2.10$ m above FFL or $+0.30$ m above bedside nightstands.
* **Chandeliers & Heavy Pendants:** Quantified with dedicated ceiling reinforcement hook and safety steel wire loop.

---

## 2. Control & Switching Hardware Rules

Switches must be counted by **gang count, way count, and IP rating**:

```
Switch Takeoff Matrix:
├── 1-Gang 1-Way (10A / 16A)    -> Small storage, single isolated toilet, single light
├── 2-Gang 1-Way (10A / 16A)    -> Standard bedrooms (spots circuit + perimeter spots)
├── 3-Gang 1-Way (10A / 16A)    -> Living rooms, master suites (spots + cove + chandelier)
├── 2-Way Switches (Two-Way)     -> Corridors, staircases, and bedside controls (طرف سلم)
├── Intermediate Switch          -> 3+ control points (long hotel corridors)
├── Rotary / Push Dimmer (300W)  -> Dining rooms, majlis, master bedroom coves
└── PIR Motion Sensor (360°)     -> Corridors, public toilets, parking areas
```

* **Flush Galvanized Metal Box:** Every single switch faceplate requires **one 75x75x35mm galvanized steel backbox** (or 75x75x47mm deep box if 3-gang or dimmer).

---

## 3. The 3D True Conduit & Wire Derivation Model

Never measure only 2D polyline distances on CAD. Use the **Orthogonal 3D Derivation Formula**:

$$L_{\text{total\_wire}} = \left( L_{\text{horizontal\_CAD}} + L_{\text{vertical\_drops}} + L_{\text{homerun\_to\_DB}} \right) \times 1.10 \times N_{\text{conductors}}$$

### A. Vertical Drop Heights ($L_{\text{vertical\_drops}}$):
1. **Drop from ceiling slab ($H = +3.00$ m) to wall switch ($H = +1.20$ m):**
   $$\text{Drop per switch} = 3.00 - 1.20 = 1.80 \text{ m}$$
2. **Drop from ceiling slab ($H = +3.00$ m) to cove driver box ($H = +2.65$ m):**
   $$\text{Drop per cove feed} = 3.00 - 2.65 = 0.35 \text{ m}$$
3. **Drop from ceiling slab ($H = +3.00$ m) to bedside switch ($H = +0.70$ m):**
   $$\text{Drop per bedside switch} = 3.00 - 0.70 = 2.30 \text{ m}$$

### B. Number of Conductors ($N_{\text{conductors}}$):
* Standard branch lighting conduit carries **3 wires**:
  1. Phase ($1 \times 2.5 \text{ mm}^2$ Cu/PVC - Red/Yellow/Blue)
  2. Neutral ($1 \times 2.5 \text{ mm}^2$ Cu/PVC - Black)
  3. Circuit Protective Conductor ($1 \times 2.5 \text{ mm}^2$ Cu/PVC - Green/Yellow Earth)
* Switch drop conduit carries:
  * 1-Gang: 2 wires (Live supply + 1 Switch wire)
  * 2-Gang: 3 wires (Live supply + 2 Switch wires)
  * 3-Gang: 4 wires (Live supply + 3 Switch wires)
  * Two-Way: 3 wires (Two strappers + Common)

---

## 4. Derived Consumables & Fixing Hardware

For every **100 meters of lighting conduit**:
* **Conduit Couplings:** 35 pcs (standard pipe length is 3.0 m).
* **Conduit Solvent Cement:** 1 can (250 ml) per 50 m.
* **Galvanized Ceiling Saddles / Clips:** 1 clamp every **0.80 meters** ($100 / 0.80 = 125$ clamps per 100 m).
* **Circular Junction Boxes (BESA boxes) with covers:** 1 box for every ceiling luminaire connection point.
