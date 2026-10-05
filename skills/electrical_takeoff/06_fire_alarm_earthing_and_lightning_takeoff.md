# SKILL-ELE-QTO-06: Fire Alarm, Earthing & Lightning Protection Takeoff 🚨⚡🛡️

> **Engineering guide for quantifying addressable fire alarm systems, fire-rated cabling, earthing electrodes, equipotential bonding, and lightning protection systems.**

---

## 1. Fire Alarm System (Addressable NFPA 72 / SBC 801 Standard)

Every modern building requires an **Analogue Addressable Fire Alarm System**:

### A. Initiating & Notification Field Devices:
1. **Optical Smoke Detectors:** 
   * Coverage radius $R = 7.5\text{ m}$ (max area $\approx 80\text{ m}^2$ per detector).
   * Located in bedrooms, corridors, lobbies, and electrical rooms.
2. **Heat Detectors (Rate of Rise / Fixed Temp 58°C):**
   * Located in kitchens, boiler rooms, and generator rooms (to avoid false alarms from cooking steam).
3. **Manual Call Points (MCP / Break Glass):**
   * Located adjacent to all emergency exit doors, staircase entries, and corridor exits at $+1.20$ m to $+1.40$ m above FFL. Max walking distance $\le 30$ meters.
4. **Electronic Sounder & Visual Strobe (Horn/Strobe):**
   * Multi-tone 90-105 dB(A) sounder with high-intensity flashing LED xenon strobe. Installed at $+2.20$ m above FFL in corridors and public spaces.
5. **Duct Smoke Detectors:** Installed in supply/return HVAC ducts $> 2000 \text{ CFM}$ with sampling tubes to trip AC units upon smoke ingress.
6. **Interface Modules:**
   * **Control Modules:** Interfaced to trip elevators down to ground floor, shut off fresh air fans, release magnetic fire doors, and start smoke extraction fans.
   * **Monitor Modules:** Interfaced to sprinkler flow switches and tamper valves.

### B. Fire-Rated Cabling Takeoff (FP200 / PH120 Standard):
* **Cable Specification:** 2-Core $1.5 \text{ mm}^2$ Shielded Twisted Pair, Silicone Rubber insulated with LSZH outer sheath (tested to BS 6387 CWZ / EN 50200 for 120-minute fire survival).
* **Loop Calculation:**
  $$L_{\text{loop\_meters}} = \left( \sum \text{Distance between sequential detectors} + \text{Riser between floors} + \text{Return to FACP} \right) \times 1.10$$
* Maximum allowable loop length is **1,500 meters** (or max 128 to 250 addressable devices per loop).

---

## 2. Earthing & Grounding System (IEC 60364 / SBC 401 Standard)

The overall target earthing resistance must be **$R_{\text{earth}} \le 1.0\text{ to }5.0\text{ }\Omega$**:

### A. Earth Electrodes & Pits Takeoff:
1. **Copper Bonded Steel Earth Rods:**
   * Diameter: Ø 5/8" (16 mm) or Ø 3/4" (19 mm), length $3.0\text{ m}$ (or coupled $2 \times 3\text{m} = 6\text{m}$).
   * Minimum copper molecular bonding thickness: **254 microns**.
2. **Inspection Earth Pits:**
   * Heavy-duty precast concrete inspection pit ($300 \times 300\text{ mm}$ or circular heavy-duty polymer) with load-rated cast iron cover bearing the earth symbol.
3. **Earth Enhancing Compound:** Bentonite clay or carbon-based conductive cement (25 kg bag per rod pit) to achieve low resistance in sandy/rocky soils.

### B. Earth Conductor Network & Main Earth Bar (MEB):
* **Main Grounding Conductor:** Bare copper stranded cable ($1 \times 70\text{ mm}^2$ or $1 \times 95\text{ mm}^2$) or Bare Copper Tape ($25 \times 3\text{ mm}$).
* **Main Earth Bar (MEB) with Disconnecting Link:** High-conductivity hard-drawn copper bar ($50 \times 6\text{ mm} \times 400\text{ mm}$) mounted on insulated standoff brackets in the main electrical substation / switchgear room.
* **Equipotential Bonding Conductors:**
  * Metallic water supply main pipe: $1 \times 16\text{ mm}^2$ or $25\text{ mm}^2$ Green/Yellow.
  * Structural steel columns: $1 \times 25\text{ mm}^2$ Bare Copper.
  * Cable tray network: $1 \times 16\text{ mm}^2$ Green/Yellow bonding jumper across every expansion joint.

---

## 3. Lightning Protection System (LPS - IEC 62305 / NFPA 780)

### A. Air Termination Network (Rooftop):
* **Air Terminals (Franklin Rods):** Solid copper or stainless steel pointed rods (Ø 16mm x 500mm or 1000mm length) installed at roof perimeter and highest parapet corners.
* **Mesh Network (Faraday Cage):** Bare copper tape ($25 \times 3\text{ mm}$) fixed on roof slab/parapet in a grid of **$10\text{m} \times 10\text{m}$ (Class I)** or **$20\text{m} \times 20\text{m}$ (Class III/IV)**.
* **Tape Clamps & DC Clips:** Non-metallic or brass DC clips spaced every **1.0 meter** along flat runs and 0.5m on vertical parapets.

### B. Down Conductors & Test Links:
* **Down Conductors:** Spaced around building perimeter every 10 to 20 meters.
  - $25 \times 3\text{ mm}$ bare/PVC-sheathed copper tape or $1 \times 50\text{ mm}^2$ stranded bare copper conductor run inside dedicated heavy-duty PVC conduit embedded in exterior columns.
* **Test Clamp / Disconnecting Box:** Installed at $+1.50$ m above external ground level to isolate the roof network during annual resistance testing.
* **Dedicated Lightning Earth Pits:** Each down conductor terminates into an independent earth rod pit and is bonded to the main ring earth below ground.
