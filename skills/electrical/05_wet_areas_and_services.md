# SKILL-LGT-05: Wet Areas & Service Space Engineering

> **Domain:** Bathrooms, Kitchens, & Utility Room Electrical Design  
> **Level:** Professional / Consultant Standards (SBC 401 Sec 701, IEC 60364-7-701)  
> **Automation Target:** AutoCAD 2027 via ActiveX COM (Python `win32com.client`)

---

## 1. Engineering Philosophy & Objectives

Wet and service areas present strict safety hazards (water/steam proximity) alongside specialized functional tasks (shaving, grooming, ventilation, cooking).

This skill governs:
1. **Functional Exhaust Fan Placement:** Centering the exhaust fan (`FAN`) **strictly above the toilet bowl** or shower ceiling—never randomly on an arbitrary wall.
2. **Vanity Task Illumination:** Orienting and snapping mirror lights (`Type_FG`) parallel to the basin counter and mirror face.
3. **Water-Proof Ingress Protection (IP Zones):** Enforcing IP44/IP65 ratings in compliance with SBC 401 Section 701.
4. **Independent Ventilation Control:** Dedicated switch gang for exhaust ventilation separate from ambient lighting.

---

## 2. Fundamental Design Principles (Code & Standards)

### 2.1 Bathroom Moisture Zones (SBC 401 / IEC 60364-7-701)
- **Zone 0 (Inside bathtub or shower basin):** Only SELV ($\le 12\text{V AC}$) with minimum IPX7.
- **Zone 1 (Directly above shower/bath up to $2.25\text{ m}$):** Minimum **IPX4** (or **IPX5** where water jets occur).
- **Zone 2 (Within $0.60\text{ m}$ of Zone 1 edge):** Minimum **IPX4**.
- **Outside Zones:** General luminaires allowed, but IP44 recommended for all residential bathroom ceiling spots.

### 2.2 Ventilation Standards (Saudi Mechanical Code / SBC 501)
- Minimum intermittent bathroom exhaust rate: $25\text{ L/s}$ ($50\text{ CFM}$).
- Exhaust intake location: Directly above the primary odor/moisture generation point (the toilet bowl or shower enclosure).

---

## 3. Reference Consultant Induction (Heuristics from Real Plans)

From deep induction of original drawings (`Standard Project...ELE.dwg`):

### 3.1 Bathroom Layout Triad
In a typical master bathroom with 3 fixtures (Shower, Toilet, Vanity Sink):
1. **Ceiling Spots (`Type_P` - Water-Proof 10W):**
   - Exactly **3 spots** arranged to cover the functional triangle:
     - Spot 1: Inside/adjacent to the Shower zone.
     - Spot 2: In the circulation walkway opposite the entrance door.
     - Spot 3: Centered in front of the Toilet area.
2. **Vanity Light (`Type_FG` - 3x6W Mirror Light):**
   - Centered strictly above the vanity washbasin counter.
   - Rotated parallel to the counter/mirror wall (length aligned with the counter width).
3. **Exhaust Fan (`Fan_Outlet` / `FAN`):**
   - Located on the ceiling/wall directly centered on the vertical axis of the toilet bowl.
   - Drawn as a clean, standardized red rectangle labeled `FAN` (avoiding oversized mechanical symbols).

### 3.2 Bathroom Control Wiring
- **Switch:** Double-pole or 2-gang water-proof switch (`2G W.P.`) mounted at the entrance.
- **Circuit 1 (Red Polyline):** Connects the 3 ceiling downlights and the vanity mirror light.
- **Circuit 2 (Magenta Polyline):** Dedicated line from Switch Gang 2 directly to the `FAN` outlet.

---

## 4. CAD Entities, Blocks & Attributes

| Element | Approved Block Name | Layer Name | Color / Scale | Note |
| :--- | :--- | :--- | :--- | :--- |
| Water-Proof Spot | `LED 10w wp` / `Type_P` | `Lighting-Fixtures` | Blue (5) / Scale: `1.0` | IP44/IP65 rated |
| Mirror / Vanity Light | `3X6W Mirror light` / `Type_FG` | `Lighting-Fixtures` | Cyan (4) / Scale: `1.0` | Centered over sink |
| Exhaust Fan Outlet | `Fan_Outlet` | `Lighting-Fixtures` | Red (1) / Scale: `1.0` | Over toilet bowl |
| WP Switch Annotation | Text `"W.P"` | `Lighting-Switches` | Red (1) / Height: $0.15\text{ m}$ | Next to switch block |

---

## 5. Algorithmic Formulation for Auto-Bathroom Layout

```python
def calculate_bathroom_fixtures(toilet_center, sink_box, shower_box, walk_center):
    """
    Computes exact positions for bathroom fixtures based on architectural elements.
    """
    # 1. Fan strictly over toilet
    fan_pos = {
        "x": toilet_center[0],
        "y": toilet_center[1] + 0.15, # Ceiling intake right above bowl
        "block": "Fan_Outlet"
    }
    
    # 2. Mirror light centered on sink counter, aligned with wall
    sink_xmin, sink_ymin, sink_xmax, sink_ymax = sink_box
    sink_cx = (sink_xmin + sink_xmax) / 2.0
    sink_cy = (sink_ymin + sink_ymax) / 2.0
    mirror_pos = {
        "x": sink_cx,
        "y": sink_cy,
        "rotation_deg": 90.0 if (sink_ymax - sink_ymin) > (sink_xmax - sink_xmin) else 0.0,
        "block": "3X6W Mirror light"
    }
    
    # 3. Downlights covering shower, toilet zone, and walkway
    spots = [
        {"x": (shower_box[0] + shower_box[2]) / 2.0, "y": (shower_box[1] + shower_box[3]) / 2.0, "type": "shower"},
        {"x": walk_center[0], "y": walk_center[1], "type": "walkway"},
        {"x": toilet_center[0], "y": walk_center[1], "type": "toilet_ambient"}
    ]
    return fan_pos, mirror_pos, spots
```

---

## 6. Anti-Patterns & Prohibitions (Zero Tolerance)

1. ❌ **Arbitrary Fan Placement:** Putting the exhaust fan in the shower stall or on an empty corner wall away from the toilet.
2. ❌ **Misaligned Mirror Light:** Mirror light rotated $90^\circ$ perpendicular to the counter, cutting through the mirror.
3. ❌ **Overcrowding Downlights:** Stuffing 6 spots in a $1.8\text{ m} \times 2.4\text{ m}$ bathroom alongside a mirror light.
4. ❌ **Single Switch for Light & Fan:** Forcing the resident to run the noisy exhaust fan every time they turn on the mirror light to wash hands.
