# SKILL-LGT-02: Switching & Control Topology Engineering

> **Domain:** Electrical Control & Switching Architecture  
> **Level:** Professional / Consultant Standards (SBC 401, IEC 60364)  
> **Automation Target:** AutoCAD 2027 via ActiveX COM (Python `win32com.client`)

---

## 1. Engineering Philosophy & Objectives

Switching ergonomics dictate the comfort and intuitive safety of a residential space. A resident entering a dark room must naturally reach the switch without stumbling, and a resident in bed must effortlessly control lighting without standing up.

This skill governs:
1. **Strike-Side Snapping:** Fastening entrance switches on the handle side of the door ($15\text{--}20\text{ cm}$ from the frame jamb).
2. **Bedside Symmetrical Mirroring:** Ensuring left and right 2-way bedside switches exhibit precise mirrored geometric symmetry.
3. **Wall Flush Attachment:** Aligning the switch base strictly to the finished interior plaster face.
4. **Logical Gang Allocation:** Structuring switch circuits according to functional priority (General, Accent, Cove).

---

## 2. Fundamental Design Principles (Code & Standards)

### 2.1 Door Strike-Side Rule (SBC 401 & IEC 60364)
- **Position:** Switches must be located adjacent to the latch/handle edge of the door, never behind the door swing (hinge side).
- **Clearance:** Distance from the finished door casing to the centerline of the switch box must be between $15\text{ cm}$ and $20\text{ cm}$.
- **Mounting Height:** Standard residential installation height is $+1.10\text{ m}$ to $+1.20\text{ m}$ above Finished Floor Level (FFL).

### 2.2 Two-Way (Multi-Way) Switching Requirements
For hotel-grade residential master bedrooms:
- Lighting must be controllable from **both** the room entrance and **both** sides of the bed without interruption.
- Master entrance switch provides multi-way control for the main downlight ring and cove, while bedside switches offer localized two-way control.

---

## 3. Reference Consultant Induction (Heuristics from Real Plans)

From deep induction of consultant drawings (Standard Project Suite / Senior Consultant):

### 3.1 Bedside 2-Way Switch Mirrored Symmetry (The Mirror Rule)
- **Left Bedside Switch:**
  - Located on the North headboard wall immediately adjacent to the mattress edge ($X \approx X_{\text{bed\_left}} - 0.05\text{ m}$, $Y = Y_{\text{headboard}}$).
  - Terminal circle sits on the wall; switch arm angles inward towards the bed.
- **Right Bedside Switch:**
  - Located on the North headboard wall immediately adjacent to the mattress edge ($X \approx X_{\text{bed\_right}} + 0.05\text{ m}$, $Y = Y_{\text{headboard}}$).
  - Terminal circle sits on the wall; switch arm must angle inward towards the bed, creating **a direct mirror reflection** of the left switch.
- **AutoCAD Implementation:**
  To guarantee exact geometric reflection:
  $$\text{Right Switch Rotation} = 180^\circ - \text{Left Switch Rotation}$$
  Or insert with $X_{\text{scale}} = -1.0$ (Mirrored Block).

### 3.2 Master Bedroom Entrance 3-Gang Switch
- **Location:** On the South wall bordering the entrance opening, strictly flush to the wall surface ($Y = Y_{\text{south\_wall}}$).
- **Gang Structure:**
  - **Gang 1 (Switch Line 1):** Controls the 5-downlight ceiling ring.
  - **Gang 2 (Switch Line 2):** Controls the perimeter Cove Lighting polyline (`E-LITE-COVE`).
  - **Gang 3 (Switch Line 3):** Controls the bedside sconces (`Wall_Light`) in 2-way coordination with bedside switches.

### 3.3 Bathroom 2-Gang Water-Proof Switch (`2G W.P.`)
- Located outside or immediately inside the bathroom entrance door on the latch side.
- Must keep clear of structural concrete columns.
- **Gang 1:** General ceiling spots (`Type_P`) + Vanity mirror light (`Type_FG`).
- **Gang 2:** Dedicated exhaust fan (`FAN`).

---

## 4. CAD Entities, Blocks & Attributes

| Switch Type | Approved Block Name | Target Layer | Insertion Scale | Elevation ($Z$) |
| :--- | :--- | :--- | :--- | :--- |
| 1-Gang 1-Way Switch | `Switch 1 Gang` | `Lighting-Switches` | `1.0` | $0.0$ |
| 2-Gang 1-Way Switch | `Switch 2 Gang` | `Lighting-Switches` | `1.0` | $0.0$ |
| 3-Gang 1-Way Switch | `One way 3 Gang switch` | `Lighting-Switches` | `1.0` | $0.0$ |
| 2-Way 2-Gang Bedside Switch | `2W2G Switch` | `Lighting-Switches` | `1.0` (or `[-1, 1, 1]` for mirror) | $0.0$ |
| Water-Proof Suffix Text | Text `"W.P"` (Height: $0.15\text{ m}$, Color: Red) | `Lighting-Switches` | N/A | $0.0$ |

---

## 5. Mathematical Formulations for Automated Switch Placement

```python
def calculate_bedside_switches(bed_box, wall_y):
    """
    Computes coordinates and mirrored rotation angles for bedside switches.
    """
    b_xmin, b_ymin, b_xmax, b_ymax = bed_box
    
    # Left bedside switch (adjacent to left mattress edge)
    left_switch = {
        "x": b_xmin - 0.08,
        "y": wall_y,
        "rotation_deg": 45.0,
        "x_scale": 1.0
    }
    
    # Right bedside switch (adjacent to right mattress edge - Mirrored!)
    right_switch = {
        "x": b_xmax + 0.08,
        "y": wall_y,
        "rotation_deg": 135.0, # Or 45.0 with x_scale = -1.0
        "x_scale": -1.0
    }
    return left_switch, right_switch
```

---

## 6. Anti-Patterns & Prohibitions (Zero Tolerance)

1. ❌ **Floating Switches:** Switches placed in the middle of a hallway or doorway without touching a wall line.
2. ❌ **Hinge-Side Mounting:** Placing switches behind the door swing where opening the door obscures the switch.
3. ❌ **Asymmetrical Bedside Angles:** Left switch angled at $45^\circ$ while right switch is angled at $45^\circ$ unmirrored, making them face in identical absolute directions rather than pointing symmetrically toward the bed.
4. ❌ **Combined Fan/Light Switch in Bath:** Tying the bathroom exhaust fan to the same gang as the mirror or ceiling light without an independent switch gang.
