"""
Cable Sizing & Voltage Drop Calculator CLI
Compliant with IEC 60364-5-52 and National Electric Codes (SBC 401 / NEC).

Usage:
    python cable_sizer.py --load 15.5 --voltage 400 --pf 0.85 --length 45 --system 3ph
"""
import argparse
import math

def calculate_cable(load_kw: float, voltage: float, pf: float, length_m: float, system: str, max_vd_percent: float = 3.0):
    if system == "3ph":
        ib = (load_kw * 1000) / (math.sqrt(3) * voltage * pf)
    else:
        ib = (load_kw * 1000) / (voltage * pf)
        
    in_rating = math.ceil(ib / 5.0) * 5.0
    if in_rating < 16:
        in_rating = 16.0
        
    # Standard copper XLPE/PVC cable sizes and ampacities (air/tray 30C)
    ratings = [
        (1.5, 18.0, 24.0),
        (2.5, 25.0, 14.5),
        (4.0, 34.0, 9.1),
        (6.0, 44.0, 6.0),
        (10.0, 61.0, 3.6),
        (16.0, 82.0, 2.3),
        (25.0, 109.0, 1.45),
        (35.0, 135.0, 1.05),
        (50.0, 168.0, 0.77),
        (70.0, 213.0, 0.54),
        (95.0, 258.0, 0.39),
        (120.0, 299.0, 0.31),
        (150.0, 344.0, 0.25),
        (185.0, 392.0, 0.20),
        (240.0, 461.0, 0.16),
        (300.0, 530.0, 0.13),
    ]
    
    selected_size = None
    actual_vd = None
    actual_vd_pct = None
    
    for size, iz, mv_a_m in ratings:
        if iz >= in_rating:
            # Calculate voltage drop: (mV/A/m * Ib * L) / 1000
            if system == "3ph":
                vd = (mv_a_m * ib * length_m) / 1000.0
            else:
                vd = (2.0 * mv_a_m * ib * length_m) / 1000.0
                
            vd_pct = (vd / voltage) * 100.0
            if vd_pct <= max_vd_percent:
                selected_size = size
                actual_vd = vd
                actual_vd_pct = vd_pct
                break
                
    if not selected_size:
        size, iz, mv_a_m = ratings[-1]
        selected_size = size
        actual_vd = (mv_a_m * ib * length_m) / 1000.0
        actual_vd_pct = (actual_vd / voltage) * 100.0
        
    return {
        "design_current_A": round(ib, 2),
        "breaker_rating_A": round(in_rating, 2),
        "recommended_cable_mm2": selected_size,
        "voltage_drop_V": round(actual_vd, 2),
        "voltage_drop_percent": round(actual_vd_pct, 2),
        "max_allowed_percent": max_vd_percent,
        "compliant": actual_vd_pct <= max_vd_percent
    }

def main():
    parser = argparse.ArgumentParser(description="Engineering Cable Sizing & Voltage Drop Calculator")
    parser.add_argument("--load", type=float, required=True, help="Connected Load in kW")
    parser.add_argument("--voltage", type=float, default=400.0, help="Line voltage (e.g. 400 or 230)")
    parser.add_argument("--pf", type=float, default=0.85, help="Power factor (default 0.85)")
    parser.add_argument("--length", type=float, required=True, help="Cable run length in meters")
    parser.add_argument("--system", choices=["3ph", "1ph"], default="3ph", help="System phase type")
    parser.add_argument("--max-vd", type=float, default=3.0, help="Maximum allowable voltage drop percentage")
    
    args = parser.parse_args()
    res = calculate_cable(args.load, args.voltage, args.pf, args.length, args.system, args.max_vd)
    
    print("=" * 60)
    print(" CABLE SIZING & VOLTAGE DROP VERIFICATION REPORT")
    print("=" * 60)
    print(f" Design Current (Ib)     : {res['design_current_A']} A")
    print(f" Recommended Breaker (In): {res['breaker_rating_A']} A")
    print(f" Recommended Copper Cable: {res['recommended_cable_mm2']} mm²")
    print(f" Calculated Voltage Drop : {res['voltage_drop_V']} V ({res['voltage_drop_percent']}%)")
    print(f" Allowable Limit         : {res['max_allowed_percent']}%")
    print(f" Verification Status     : {'[PASSED] COMPLIANT' if res['compliant'] else '[FAILED] EXCEEDS LIMIT'}")
    print("=" * 60)

if __name__ == "__main__":
    main()
