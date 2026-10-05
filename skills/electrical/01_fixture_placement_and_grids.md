# SKILL-LGT-01: Fixture Placement & Symmetrical Grid Engineering

> **Domain:** Electrical Lighting Engineering  
> **Level:** Professional / Consultant Standards (SBC 401, IEC 60364, IESNA)  
> **Automation Target:** AutoCAD 2027 via ActiveX COM (Python `win32com.client`)

---

## 1. Engineering Philosophy & Objectives

In high-end architectural lighting design, downlights and wall luminaires must never be placed blindly or purely mathematically without respect to architectural symmetry, human visual comfort, and furniture orientation.

This skill governs:
1. **Symmetrical Grid Alignment:** Ensuring downlight rows share identical vertical and horizontal axes ($X_{\text{top}} = X_{\text{bottom}}$).
2. **Glare Avoidance & Visual Comfort:** Keeping direct downlights away from headboards and sleeping zones (Unified Glare Rating $UGR < 19$).
3. **Wall Fixture Snapping:** Fastening wall sconces (`Wall_Light`) flush to the inner plaster face of the wall directly centered over nightstands.
4. **Architectural Clearances:** Enforcing mandatory setbacks from wardrobes ($60\text{--}80\text{ cm}$) and curtain pockets ($25\text{--}30\text{ cm}$).

---

## 2. Fundamental Design Principles (Code & Standards)

### 2.1 Spacing-to-Mounting-Height Ratio ($S/MH$)
According to **CIBSE SLL** and **IESNA Lighting Handbook**:
$$\frac{S}{MH} \le 1.2 \text{ to } 1.5$$
Where:
- $S$: Center-to-center distance between adjacent luminaires.
- $MH$: Mounting height above the working plane ($H_{\text{ceiling}} - 0.75\text{ m}$).
- For a typical residential ceiling height of $3.0\text{ m}$, $MH \approx 2.25\text{ m}$, meaning maximum spot-to-spot spacing $S \le 2.7\text{ m}$ (ideal spacing: $1.2\text{ m} \text{ to } 1.8\text{ m}$).

> **UNITS WARNING (measured 2026-09, project `SampleProject`)**
> The consultant DWG `sample_building_electrical.dwg` has **unconfirmed
> drawing units** (`$INSUNITS` was never verified). The metre figures above are
> therefore a *code-derived target*, **not** a measurement of this drawing.
> The measured values below are in **raw drawing units** and must be converted
> only after `$INSUNITS` is confirmed:
>
> | Class of luminaire | Measured pitch (drawing units) | Measured rows |
> | :--- | :--- | :--- |
> | General downlights (`LED 10W Ceiling Spot`) | **2.2 – 2.8** | 5 |
> | Decorative spots (`LED spot 6W Decorative`) | **0.83 – 1.15** | 22 |
>
> **Rule:** apply the $S/MH$ ratio to *design* work, and use the measured table
> only as a *sanity band* to detect a unit-scale mistake (e.g. a room drawn in
> millimetres instead of metres). Never hard-code the raw numbers into a
> generator.

### 2.2 Wall Setback Rule
To prevent scallops and shadows while maintaining uniform vertical illuminance:
$$\text{Distance from Wall} = \frac{1}{2} S \approx 0.6\text{ m to } 0.9\text{ m}$$

---

## 3. Reference Consultant Induction (Heuristics from Real Plans)

From deep induction of consultant drawings (e.g., Senior MEP Engineering Consultancy / Standard Project Suite):

### 3.1 The Master Bedroom 5-Spot Perimeter Grid
In a master bedroom with a central King bed ($1.8\text{ m} \times 2.0\text{ m}$ or $2.0\text{ m} \times 2.0\text{ m}$):
- **Top Row (Bed Zone):** Exactly **2 downlights**:
  - One to the left of the bed ($X_{\text{left}}$), centered between the left bed edge and the west cove/wall.
  - One to the right of the bed ($X_{\text{right}}$), centered between the right bed edge and the east cove/wall.
  - **Zero spots** directly above the bed pillows.
- **Bottom Row (Aisle & Desk Zone):** Exactly **3 downlights**:
  - Left spot placed at identical $X$ as the top-left spot ($X_{\text{bottom-left}} = X_{\text{top-left}}$).
  - Right spot placed at identical $X$ as the top-right spot ($X_{\text{bottom-right}} = X_{\text{top-right}}$).
  - Center spot placed exactly on the architectural centerline of the vanity/desk chair ($X_{\text{center}}$).
- **Result:** A perfectly symmetrical, visually harmonic rectangular lighting ring.

### 3.2 Bedside Sconces (`Wall_Light`)
- **Base Point:** Must snap strictly to the interior face of the North headboard wall ($Y_{\text{base}} = Y_{\text{wall\_face}}$).
- **Centering:** Must align with the exact center of each nightstand ($X = X_{\text{nightstand\_center}}$).
- **Orientation (Rotation Angle):**
  - North Wall: $180^\circ$ (pointing down into the room).
  - South Wall: $0^\circ$ (pointing up into the room).
  - East Wall: $90^\circ$ (pointing west).
  - West Wall: $270^\circ$ (pointing east).

---

## 4. CAD Entities, Blocks & Attributes

| Luminaire Type | Approved Block Name | Target Layer | Insertion Scale | Elevation ($Z$) |
| :--- | :--- | :--- | :--- | :--- |
| General Recessed Downlight | `LED 10W Ceiling Spot` | `Lighting-Fixtures` | `1.0` | $0.0$ (Plan View) |
| Decorative Accent Spot | `LED spot 6W Decorative` | `Lighting-Fixtures` | `1.0` | $0.0$ |
| Bedside Sconce | `Wall Light` | `Lighting-Fixtures` | `1.0` | $0.0$ |
| Master Chandelier | `Chandelier` | `Lighting-Fixtures` | `1.0` | $0.0$ |

---

## 5. Mathematical Formulations for Auto-Placement

```python
def calculate_bedroom_symmetrical_grid(room_box, bed_box, desk_box):
    """
    Computes exact coordinates for the 5-downlight symmetrical ring.
    room_box: (xmin, ymin, xmax, ymax)
    bed_box: (b_xmin, b_ymin, b_xmax, b_ymax)
    desk_box: (d_xmin, d_ymin, d_xmax, d_ymax)
    """
    # 1. Vertical axes for outer spots
    x_left = (room_box[0] + bed_box[0]) / 2.0
    x_right = (bed_box[2] + room_box[2]) / 2.0
    x_center = (desk_box[0] + desk_box[2]) / 2.0 if desk_box else (room_box[0] + room_box[2]) / 2.0
    
    # 2. Horizontal axes
    y_top = (bed_box[1] + bed_box[3]) / 2.0        # Mid-bed level
    y_bottom = (room_box[1] + bed_box[1]) / 2.0     # Lower aisle level
    
    spots = [
        {"name": "top_left",     "x": x_left,   "y": y_top},
        {"name": "top_right",    "x": x_right,  "y": y_top},
        {"name": "bottom_left",  "x": x_left,   "y": y_bottom},
        {"name": "bottom_mid",   "x": x_center, "y": y_bottom},
        {"name": "bottom_right", "x": x_right,  "y": y_bottom},
    ]
    return spots
```

---

## 6. Anti-Patterns & Prohibitions (Zero Tolerance)

1. ❌ **Asymmetrical Offsets:** Placing the top-left spot at $X=266.8$ and the bottom-left at $X=266.5$. The vertical axis must be identical ($X_{\text{top}} \equiv X_{\text{bottom}}$).
2. ❌ **Floating Wall Sconces:** Placing `Wall_Light` with a gap from the wall polyline. It must sit exactly on the wall boundary line.
3. ❌ **Headboard Glare:** Placing ceiling downlights directly above pillows ($Y > Y_{\text{headboard}} - 0.5\text{ m}$).
4. ❌ **Blind Clumping:** Stacking downlights solely in the aisle while leaving the surrounding bed area in total darkness.
