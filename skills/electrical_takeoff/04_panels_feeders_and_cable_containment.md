# SKILL-ELE-QTO-04: Distribution Boards, Main Feeders & Cable Trays Takeoff ⚡🏗️

> **Engineering guide for quantifying distribution boards (DB/SMDB/MDB), armored sub-feeders, voltage drop verification, cable trays/ladders, and containment accessories.**

---

## 1. Distribution Boards (DBs) Sizing & Classification

Panels must be quantified based on **Enclosure Rating, Incomer Rating, and Number of Ways (SPN / TPN)**:

```
Distribution Boards Hierarchy:
├── Main Distribution Board (MDB)     -> Ground/Basement floor electrical room (e.g. 800A - 1600A Form 4b)
├── Sub-Main Distribution Board (SMDB) -> Distribution per building wing / floor (e.g. 160A - 250A Form 2b)
├── Apartment Final DB (Consumer Unit) -> Inside each apartment (12, 18, 24, 30, 36 Ways TPN IP40)
├── Services & Public Area DB (SDB)   -> Common staircases, lifts, corridors, facade lighting
└── Rooftop Pumps & Mechanical DB     -> IP65 weatherproof enclosure for booster & drainage pumps
```

### Essential Incomer Components in Final DBs:
1. **Main Disconnect:** 60A / 100A 4-Pole Isolator or MCCB.
2. **Earth Leakage Protection (RCD / ELCB):**
   * **30 mA sensitivity:** For all socket outlets, water heaters, and wet area circuits (Life safety protection).
   * **100 mA / 300 mA sensitivity:** For main lighting feeds, general AC units, and mechanical equipment (Fire protection).
3. **Surge Protection Device (SPD):** Type 2 SPD integrated into the main incomer compartment.

---

## 2. Main Sub-Feeder Cables Takeoff (MDB to DBs)

Main feeders typically use **Copper Core, XLPE Insulated, Steel Wire Armored, PVC Sheathed Cables (Cu/XLPE/SWA/PVC 600/1000V)**:

### A. Cable Sizing & Ampacity Matrix (in Tray/Air 40°C):
| Sub-Feeder Designation | Connected Load (kW) | Incomer Breaker | Recommended Armored Cable | Separate Earth Conductor (ECC) |
| :--- | :---: | :---: | :---: | :---: |
| **Apartment DB (Small 2-Bed)** | 18 kW | 40A 3P | $4 \times 16.0 \text{ mm}^2 \text{ SWA}$ | $1 \times 16.0 \text{ mm}^2 \text{ Cu/PVC (G/Y)}$ |
| **Apartment DB (Medium 3-Bed)**| 28 kW | 60A 3P | $4 \times 25.0 \text{ mm}^2 \text{ SWA}$ | $1 \times 16.0 \text{ mm}^2 \text{ Cu/PVC (G/Y)}$ |
| **Luxury Penthouse / Villa** | 45 kW | 80A 3P | $4 \times 35.0 \text{ mm}^2 \text{ SWA}$ | $1 \times 25.0 \text{ mm}^2 \text{ Cu/PVC (G/Y)}$ |
| **Services & Public Areas DB** | 35 kW | 70A 3P | $4 \times 35.0 \text{ mm}^2 \text{ SWA}$ | $1 \times 25.0 \text{ mm}^2 \text{ Cu/PVC (G/Y)}$ |
| **Rooftop Booster Pumps DB** | 22 kW | 50A 3P | $4 \times 16.0 \text{ mm}^2 \text{ SWA}$ | $1 \times 16.0 \text{ mm}^2 \text{ Cu/PVC (G/Y)}$ |

### B. True Length Derivation (Including Vertical Shaft):
$$L_{\text{feeder}} = \left( L_{\text{horizontal\_basement}} + H_{\text{riser\_shaft}} + L_{\text{horizontal\_floor\_run}} + \text{Panel Terminations (3.0m)} \right) \times 1.05$$
* **Panel Termination Allowance:** Add **1.5 meters at MDB end** and **1.5 meters at DB end** for cable glanding, bending radius, and internal busbar routing.
* **Cable Glands & Lugs:** Each SWA cable requires:
  * 2x Brass Indoor/Outdoor Compression Glands (BW / CW type).
  * 2x Earth Tags and PVC Shrouds.
  * 8x Heavy-duty tin-plated copper crimping lugs.

---

## 3. Cable Trays, Ladders & Support Containment

### A. Containment Selection by Area:
* **Heavy Cable Ladder (Galvanized Steel 1.5mm - 2.0mm):** Used in electrical shafts (risers) and main basement spine routes ($W = 300\text{mm}, 450\text{mm}, 600\text{mm}$, depth 100mm).
* **Perforated Cable Tray with Cover:** Used for horizontal corridor branches ($W = 150\text{mm}, 200\text{mm}, 300\text{mm}$, depth 50mm).
* **Wire Mesh (Basket) Tray:** Commonly used in IT/Server rooms and telecom shafts for Cat6A cables.

### B. Trapeze Support Calculation Rule:
* Trays must be supported at a maximum spacing of **1.20 to 1.50 meters**:
  $$\text{Number of Trapeze Hangers} = \frac{L_{\text{tray\_meters}}}{1.20} + 1$$
* **Each Trapeze Support Assembly Consists of:**
  1. 1x Slotted Unistrut Channel (41x41mm or 41x21mm HDG).
  2. 2x M10 or M12 Threaded Steel Rods (length $0.50\text{m} - 1.20\text{m}$).
  3. 2x Heavy-duty concrete drop-in ceiling anchors (wedge anchors).
  4. 8x M10/M12 nuts, flat washers, and spring channel nuts (Zebedee).

---

## 4. Passive Fire Protection (Firestop Seals)

Whenever cable trays or armored cables penetrate floor slabs or fire-rated walls (electrical shafts):
* **Firestop Mortar / Intumescent Coated Batts (2-Hour Fire Rating):** Measured in square meters ($m^2$) of shaft opening area.
* **Intumescent Firestop Sealant (Mastic):** 1 tube (310 ml) for every 3 cable bundle penetrations.
