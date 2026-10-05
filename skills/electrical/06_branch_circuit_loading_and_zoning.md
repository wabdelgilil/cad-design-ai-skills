# SKILL-LGT-06: Branch Circuit Load Calculation, Grouping & Protection

> **Domain:** Electrical Load Scheduling & Circuit Sizing  
> **Level:** Professional Standards (SBC 401, IEC 60364, NEC / NFPA 70, SBC 601)  
> **Automation Target:** Panel Balancer & Load Calculation Engine (`core/electrical_engine/`)

---

## 1. Engineering Philosophy & Objectives

In modern electrical design, lighting branch circuiting is governed by **functional reliability, phase balance, and safety zoning**, not merely raw wattage aggregation. 

With LED technology consuming only $10\text{--}15\%$ of legacy incandescent loads, sizing circuits solely by ampacity leads to dangerous oversized circuits where a single trip plunges an entire residence into darkness.

This skill governs:
1. **Functional Zoning & Continuity of Supply:** Isolating wet services, reception, circulation, and sleeping quarters onto independent branch circuits.
2. **Three-Phase Balancing:** Alternating circuit phases ($L1 \to L2 \to L3$) sequentially across odd-numbered poles ($01, 03, 05, 07\dots$).
3. **LED Inrush Current & Breaker Curves:** Accounting for electronic driver inrush current ($20\text{--}50 \times I_n$) using Type C MCBs.
4. **Code Compliance:** Enforcing SBC 401 voltage drop limits ($<3\%$ branch, $<5\%$ total) and 80% continuous load limits.

---

## 2. Fundamental Engineering Standards (International & Saudi Codes)

### 2.1 The 80% Continuous Loading Rule (NEC Art. 210.20 / SBC 401)
Lighting loads in commercial and luxury residential projects are classified as **continuous loads** (operating for $\ge 3$ consecutive hours).
$$I_{\text{design}} \le 0.80 \times I_n$$
For standard branch circuit protective devices at $230\text{V}$:
- **$10\text{A}$ MCB:** Max continuous load $= 8.0\text{A} \times 230\text{V} = 1840\text{ VA}$ (Consultant limit: $1000\text{--}1200\text{ VA}$).
- **$15\text{A} / 16\text{A}$ MCB:** Max continuous load $= 12.0\text{A} \times 230\text{V} = 2760\text{ VA}$ (Consultant limit: $1500\text{--}1800\text{ VA}$).

### 2.2 Maximum Points per Circuit Rule
Under standard British/IEC practice widely enforced by Saudi consultants:
- **Maximum points per lighting circuit:** $\le 10 \text{ to } 12 \text{ luminaires/outlets}$.
- This limits fault exposure and maintains circuit maintainability.

### 2.3 LED Inrush Current & Breaker Selection (IEC 60898-1)
LED electronic drivers draw high momentary inrush currents ($I_{\text{peak}} \approx 20\text{--}50 \times I_{\text{nominal}}$ for $100\text{--}500\ \mu\text{s}$) due to input capacitor charging.
- **Breaker Curve:** **Type C MCB** (magnetic trip threshold $5\text{--}10 \times I_n$) is recommended over Type B to prevent nuisance tripping when switching on large arrays of downlights or cove drivers.
- **Power Factor ($PF$):** All drivers must comply with SASO / SEC requirements ($PF \ge 0.90$).

---

## 3. Standard Functional Zoning Framework (Residential)

For any self-contained residential apartment or villa floor, lighting loads **must be partitioned into a minimum of 4 distinct functional circuits**:

```
                       ┌──────────────────────────────────────────────┐
                       │     Main Distribution Board (MDB / DB)       │
                       │             400V / 230V, 3-Phase             │
                       └──────────────────────┬───────────────────────┘
                                              │
         ┌───────────────────┬────────────────┴───────────────────┬───────────────────┐
         ▼                   ▼                                    ▼                   ▼
 ┌───────────────┐   ┌───────────────┐                    ┌───────────────┐   ┌───────────────┐
 │ Circuit CKT 01│   │ Circuit CKT 03│                    │ Circuit CKT 05│   │ Circuit CKT 07│
 │  Phase R (L1) │   │  Phase Y (L2) │                    │  Phase B (L3) │   │  Phase R (L1) │
 ├───────────────┤   ├───────────────┤                    ├───────────────┤   ├───────────────┤
 │ Wet & Services│   │  Hospitality  │                    │  Circulation  │   │ Private Suite │
 │ • Kitchen     │   │ • Majles      │                    │ • Hallways    │   │ • Master Bed  │
 │ • Guest WC    │   │ • Dining Area │                    │ • Living Room │   │ • Walk-in Clos│
 │ • Exhaust Fans│   │ • Chandeliers │                    │ • Lobby Sensor│   │ • Master Bath │
 │ • Laundry     │   │ • Accent Cove │                    │ • Maid Room   │   │ • Bed Sconces │
 └───────────────┘   └───────────────┘                    └───────────────┘   └───────────────┘
```

1. **CKT 01 (Wet & Services):** Isolated because moisture, steam, and motor loads (fans) have the highest probability of insulation breakdown or nuisance RCD tripping.
2. **CKT 03 (Reception / Hospitality):** High aesthetic priority; controls chandeliers, mood coves, and dimmers without interference from appliance switching.
3. **CKT 05 (Circulation / Escape Routes):** Ensures primary exit pathways, corridor lighting, and staircases remain illuminated during local room faults (SBC 201 Life Safety).
4. **CKT 07 (Private Quarters):** Dedicates supply to the master suite for user autonomy and night comfort.

---

## 4. Phase Balancing & Mathematical Optimization

In a 3-phase panel board ($R, Y, B$), the total connected and demand loads on each phase must be balanced to minimize neutral conductor current ($I_N$) and prevent transformer phase unbalance:
$$I_N = \sqrt{I_R^2 + I_Y^2 + I_B^2 - (I_R I_Y + I_Y I_B + I_R I_B)}$$
- **Code Threshold (SBC 401 / SEC):** Maximum phase unbalance $\le 5\% \text{ to } 10\%$.
- **Circuit Numbering Mapping:**
  - **Pole 1 (CKT 01):** Phase $R$ (L1)
  - **Pole 3 (CKT 03):** Phase $Y$ (L2)
  - **Pole 5 (CKT 05):** Phase $B$ (L3)
  - **Pole 7 (CKT 07):** Phase $R$ (L1)
  - **Pole 9 (CKT 09):** Phase $Y$ (L2)

---

## 5. Conductor Sizing & Voltage Drop Verification (SBC 401 Sec 525)

### 5.1 Cable Sizing Criteria
Conductors must satisfy the triple inequality:
$$I_z \ge I_n \ge I_b$$
Where:
- $I_b$: Design operating current ($\frac{P}{V \times PF}$).
- $I_n$: Nominal rating of the circuit breaker ($15\text{A}$ or $16\text{A}$).
- $I_z$: Current-carrying capacity of the cable under installation conditions ($I_z = I_0 \times C_a \times C_g$).

### 5.2 Minimum Conductor Specifications
- **Phase & Neutral:** $2.5\text{ mm}^2$ Cu/XLPE/PVC (or Cu/PVC).
- **Protective Earth (PE):** $2.5\text{ mm}^2$ Cu continuous green/yellow grounding wire run to **every** luminaire and metal backbox (SBC 401 Clause 411.3.1.1).
- **Conduit:** $20\text{ mm}$ Rigid PVC minimum.

### 5.3 Voltage Drop Formulation
$$\Delta V = \frac{\sqrt{3} \times I_b \times L \times (R \cos \phi + X \sin \phi)}{1000} \quad \text{(3-Phase)}$$
$$\Delta V = \frac{2 \times I_b \times L \times (R \cos \phi + X \sin \phi)}{1000} \quad \text{(1-Phase)}$$
- Permissible limit: $\Delta V_{\%} \le 3.0\%$ for final branch lighting circuits.

---

## 6. Algorithmic Formulation for Auto-Circuit Allocation

```python
def assign_lighting_circuits(fixtures, apartment_id, panel_id):
    """
    Groups fixtures into the 4 standard functional circuits and assigns phases.
    """
    circuits = {
        f"{panel_id}-01": {"zone": "WET_SERVICES", "phase": "R", "breaker": "16A 1P", "cable": "3x2.5mm2", "items": []},
        f"{panel_id}-03": {"zone": "HOSPITALITY",  "phase": "Y", "breaker": "16A 1P", "cable": "3x2.5mm2", "items": []},
        f"{panel_id}-05": {"zone": "CIRCULATION",  "phase": "B", "breaker": "16A 1P", "cable": "3x2.5mm2", "items": []},
        f"{panel_id}-07": {"zone": "MASTER_SUITE", "phase": "R", "breaker": "16A 1P", "cable": "3x2.5mm2", "items": []},
    }
    
    for f in fixtures:
        space = f.get("space_type", "").upper()
        if space in ("KITCHEN", "BATH_GUEST", "WC", "LAUNDRY"):
            circuits[f"{panel_id}-01"]["items"].append(f)
        elif space in ("MAJLES", "DINING", "SALON"):
            circuits[f"{panel_id}-03"]["items"].append(f)
        elif space in ("CORRIDOR", "LOBBY", "LIVING", "MAID"):
            circuits[f"{panel_id}-05"]["items"].append(f)
        elif space in ("MASTER_BED", "MASTER_BATH", "WIC"):
            circuits[f"{panel_id}-07"]["items"].append(f)
            
    return circuits
```

---

## 7. Anti-Patterns & Prohibitions (Zero Tolerance)

1. ❌ **Monolithic Lighting Circuit:** Aggregating an entire multi-room apartment onto 1 single circuit because total wattage is $<1000\text{W}$.
2. ❌ **Mixing Damp Areas with Living Rooms:** Sharing a circuit between a bathroom exhaust fan and living room chandeliers.
3. ❌ **Ignoring Protective Earth:** Omitting the ground wire ($2.5\text{ mm}^2$ PE) from plastic/LED fixtures. Code mandates ground to every outlet box.
4. ❌ **Single-Phase Panel Overloading:** Placing all lighting on Phase R and all sockets on Phase Y, inducing massive neutral currents and phase unbalance.
