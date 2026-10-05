# SKILL-ELE-QTO-02: Small Power & Dedicated Loads Takeoff 🔌

> **Engineering guide for quantifying switched socket outlets, weatherproof accessories, kitchen appliances, floor boxes, and high-power dedicated feeds.**

---

## 1. Socket Outlet Categories & Specification Standards

### A. General Purpose Sockets (BS 1363 Standard):
* **Twin (Duplex) 13A Switched Socket:** Standard for bedrooms, living rooms, majlis, and corridors. Installed at $+0.30$ m or $+0.45$ m above FFL.
* **Single 13A Switched Socket:** Storage rooms, dedicated appliance alcoves.
* **USB Charging Sockets:** 13A Twin Socket integrated with Type-A and Type-C USB charging ports (3.0A / 18W PD). Standard behind bedside tables and work desks.

### B. Specialized & Heavy-Duty Outlets:
* **Weatherproof IP55 / IP65 Sockets:** Outdoor balconies, roofs, mechanical rooms, garden perimeter, and driver room external wash areas. Must have spring-loaded protective flap cover and rubber seal.
* **Kitchen Worktop Sockets:** Installed at $+1.10$ m to $+1.20$ m above FFL (minimum 15 cm above kitchen counter backsplash). Must be kept **at least 30 cm away from sink edge**.
* **Floor Pop-Up Boxes:** Cast bronze or brushed stainless steel floor box (IP44 when closed) housing 2x Power + 2x RJ45 Data ports. Standard in center of majlis and executive open-plan offices.

---

## 2. Dedicated Appliances & Isolator Takeoff Matrix

Never lump specialized loads with general sockets. Each high-power appliance must have a dedicated circuit and proper isolation switch:

| Equipment / Appliance | Typical Load (VA) | Circuit Breaker (MCB) | Conductor Sizing ($N \times \text{mm}^2$) | Local Isolation Switch / Faceplate |
| :--- | :---: | :---: | :---: | :--- |
| **Electric Water Heater (30L - 80L)** | 1,500 - 2,500 | 20A 1P / 2P | $3 \times 4.0 \text{ mm}^2$ | 20A DP Switch with Neon Indicator + Flex Outlet ($+1.80$m) |
| **Electric Oven (Wall Built-in)** | 3,000 - 4,500 | 32A 1P / 2P | $3 \times 6.0 \text{ mm}^2$ | 45A DP Cooker Switch + Connection Plate ($+0.45$m) |
| **Electric Hob (Induction / Ceramic)**| 5,500 - 7,200 | 40A / 45A 1P | $3 \times 10.0 \text{ mm}^2$ | 45A Cooker Control Unit ($+1.20$m) + Terminal Box ($+0.45$m) |
| **Dishwasher** | 2,200 | 20A 1P | $3 \times 4.0 \text{ mm}^2$ | 20A DP Switch above counter + Unswitched socket below ($+0.30$m) |
| **Washing Machine & Dryer** | 2,500 | 20A 1P | $3 \times 4.0 \text{ mm}^2$ | 20A DP Switch above counter + Unswitched socket below |
| **Microwave & Refrigerator** | 1,200 - 1,800 | 20A 1P | $3 \times 4.0 \text{ mm}^2$ | 13A Switched Socket on dedicated radial circuit |
| **Water Booster Pump (DWP-02)** | 3,500 | 20A 3P | $5 \times 4.0 \text{ mm}^2$ | IP65 Rotary Isolator 4P 32A + Motor Control Box |

---

## 3. The 3D True Conduit & Wire Derivation Model (Small Power)

### A. Radial vs. Ring Circuits:
* **Radial Circuit (Common in Saudi Arabia / SEC):** Maximum 4 to 6 twin sockets per circuit with 20A breaker and $3 \times 4.0 \text{ mm}^2$ conductors in Ø25mm PVC conduit.
* **Ring Circuit:** Max 100 m² floor area with 32A breaker and loop return ($2 \times 3 \times 2.5 \text{ mm}^2$).

### B. Vertical Rise / Drop Calculation:
1. **From Floor Slab to Standard Sockets ($H = +0.30$ m):**
   $$\text{Rise from floor embedment} = 0.30 \text{ m} + 0.10 \text{ m (screed embedment)} = 0.40 \text{ m}$$
2. **From Ceiling Slab ($H = +3.00$ m) down to Sockets (if fed from suspended ceiling):**
   $$\text{Drop from ceiling} = 3.00 - 0.30 = 2.70 \text{ m}$$
3. **From Ceiling down to Kitchen Counter ($H = +1.15$ m):**
   $$\text{Drop from ceiling} = 3.00 - 1.15 = 1.85 \text{ m}$$

### C. Conductor Length Multiplier:
* Every 1.0 meter of power conduit contains:
  * 1.0 m Phase wire ($1 \times 4.0 \text{ mm}^2$ Cu/PVC Red/Yellow/Blue).
  * 1.0 m Neutral wire ($1 \times 4.0 \text{ mm}^2$ Cu/PVC Black).
  * 1.0 m Protective Conductor ($1 \times 2.5 \text{ mm}^2$ or $4.0 \text{ mm}^2$ Cu/PVC Green/Yellow).
  * Total wire length $= \text{Conduit Length} \times 3.0 \times 1.10 \text{ (Slack & Loops in backboxes)}$.

---

## 4. Backbox & Accessory Hardware Takeoff

* **Single Gang Metal Box (75x75x35mm):** For single sockets, 20A DP switches, and flex outlets.
* **Double Gang Metal Box (135x75x35mm or 47mm deep):** For twin 13A sockets and 45A cooker control units.
* **Floor Embedment Conduits:** Heavy Gauge Class 4 PVC Conduits (Rigid) with high compression strength ($> 1250 \text{ N}$) to withstand concrete slab casting without crushing.
