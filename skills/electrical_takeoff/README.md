# Electrical Quantity Takeoff & Cost Estimation Master Suite ⚡📊

> **The Definitive Engineering Knowledge Base for Electrical BOQ Takeoff, 3D Conduit/Cable Derivations, and Cost Engineering.**

---

## 🌟 Philosophy: The "True 3D & Complete System" Principle

In electrical design, **2D drafting creates dangerous estimation blindspots**:
1. **The Vertical Drop Blindspot:** Sockets, switches, and panels sit between $+0.30$ m and $+1.80$ m from finished floor level, while slabs sit at $+3.00$ m to $+3.80$ m. A pure horizontal 2D measurement ignores **over 35% of all conduit and wiring**!
2. **The Hidden Infrastructure Blindspot:** A socket is not just a plastic faceplate; it requires a galvanized deep backbox, flexible/rigid conduit, fixing screws, earthing fly-lead, and cable connections.
3. **The Phase Multiplier:** A single-line homerun in CAD represents 3 distinct conductors (Phase, Neutral, Protective Earth) for single-phase circuits, or 5 conductors ($3\text{P} + \text{N} + \text{E}$) for three-phase circuits.

---

## 📁 Architecture of the Electrical Takeoff Suite

| Skill File | Focus Discipline | Key Formulas & Engineering Derivations |
| :--- | :--- | :--- |
| **[`01_lighting_and_control_takeoff.md`](01_lighting_and_control_takeoff.md)** | Lighting & Controls | Spotlights, LED Cove Strips, Appliques, Chandeliers, 1-to-4 Gang Switches, Two-Way, Sensors, 3D Drop Rules |
| **[`02_small_power_and_special_loads_takeoff.md`](02_small_power_and_special_loads_takeoff.md)** | Small Power & Sockets | 13A Twin Sockets, Weatherproof IP65, Floor Boxes, Clean UPS Power, 20A/45A Isolators, Dedicated Feeds |
| **[`03_hvac_and_motors_power_takeoff.md`](03_hvac_and_motors_power_takeoff.md)** | HVAC & Mechanical Power | Split Units, Concealed FCUs, Rooftop ODU Isolators, Water Pump Control Panels, Water Heaters |
| **[`04_panels_feeders_and_cable_containment.md`](04_panels_feeders_and_cable_containment.md)** | Boards, Trays & Risers | Final DBs, SMDBs, MDB, Armored Cables (XLPE/SWA), Perforated Trays, Unistrut Trapeze Hangers, Firestops |
| **[`05_low_current_systems_takeoff.md`](05_low_current_systems_takeoff.md)** | Low Current & ICT | Cat6A Data/Voice, CCTV IP Cameras, SMATV Coaxial, Intercom Video Stations, Public Address Speakers, Racks |
| **[`06_fire_alarm_earthing_and_lightning_takeoff.md`](06_fire_alarm_earthing_and_lightning_takeoff.md)** | Life Safety & Protection | Addressable Smoke/Heat, FP200 Fire Cable, Earth Pits, Copper Tape, Equipotential Bonding, Air Terminals |
| **[`07_electrical_boq_structure_and_pricing_rules.md`](07_electrical_boq_structure_and_pricing_rules.md)** | BOQ Templates & Pricing | 5-Tab Dynamic Architecture, Fitting Derivation Matrices, Hidden Backbox Multipliers, 2026 Saudi Benchmarks |

---

## 🎯 Verification Gate (Audit Protocol)

Before issuing any Electrical BOQ:
1. **Cross-Discipline Check:** Reconcile architectural ceiling layouts (RCP) with structural beams to prevent conduit clashing.
2. **Panel Balance Check:** Verify that the sum of connected VA across phases satisfies $\text{Unbalance} < 5\%$.
3. **Voltage Drop Audit:** Verify that sub-main feeders do not exceed $2.0\%$ drop and final branches do not exceed $3.0\%$ (Total $< 5.0\%$).
