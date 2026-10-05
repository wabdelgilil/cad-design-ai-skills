"""
Lumen Method Room Lighting Calculator CLI
Calculates luminaire quantity and orthogonal grid distribution (Nx, Ny).

Usage:
    python lumen_calculator.py --width 4.0 --length 6.0 --height 3.0 --target-lux 300 --lumens 1200
"""
import argparse
import math

def calculate_lighting(length: float, width: float, height: float, target_lux: float, fixture_lumens: float,
                       cu: float = 0.65, mf: float = 0.80):
    area = length * width
    # Total required luminous flux = (E * A) / (CU * MF)
    required_flux = (target_lux * area) / (cu * mf)
    exact_fixtures = required_flux / fixture_lumens
    net_fixtures = max(1, math.ceil(exact_fixtures))
    
    # Calculate optimal grid (Nx along length, Ny along width)
    aspect_ratio = length / width
    ny = max(1, round(math.sqrt(net_fixtures / aspect_ratio)))
    nx = max(1, math.ceil(net_fixtures / ny))
    final_count = nx * ny
    
    achieved_lux = (final_count * fixture_lumens * cu * mf) / area
    
    # Spacing
    sx = length / nx
    sy = width / ny
    margin_x = sx / 2.0
    margin_y = sy / 2.0
    
    return {
        "room_area_m2": round(area, 2),
        "target_lux": target_lux,
        "achieved_lux": round(achieved_lux, 1),
        "total_fixtures": final_count,
        "grid_layout": f"{nx} fixtures along Length x {ny} fixtures along Width",
        "spacing_x_m": round(sx, 2),
        "spacing_y_m": round(sy, 2),
        "wall_margin_x_m": round(margin_x, 2),
        "wall_margin_y_m": round(margin_y, 2),
    }

def main():
    parser = argparse.ArgumentParser(description="Lumen Method Lighting & Grid Calculator")
    parser.add_argument("--length", type=float, required=True, help="Room length in meters")
    parser.add_argument("--width", type=float, required=True, help="Room width in meters")
    parser.add_argument("--height", type=float, default=2.8, help="Ceiling height in meters")
    parser.add_argument("--target-lux", type=float, default=300.0, help="Required lux level (e.g. 300 for office/bedroom, 500 for kitchen)")
    parser.add_argument("--lumens", type=float, default=1000.0, help="Rated output of single luminaire (lumens)")
    parser.add_argument("--cu", type=float, default=0.65, help="Coefficient of Utilization (default 0.65)")
    parser.add_argument("--mf", type=float, default=0.80, help="Maintenance Factor (default 0.80)")
    
    args = parser.parse_args()
    res = calculate_lighting(args.length, args.width, args.height, args.target_lux, args.lumens, args.cu, args.mf)
    
    print("=" * 60)
    print(" LUMEN METHOD LIGHTING DESIGN & GRID DISTRIBUTION")
    print("=" * 60)
    print(f" Room Area            : {res['room_area_m2']} m² ({args.length}m x {args.width}m)")
    print(f" Target Illumination  : {res['target_lux']} Lux")
    print(f" Achieved Illumination: {res['achieved_lux']} Lux")
    print(f" Total Luminaires     : {res['total_fixtures']} units")
    print(f" Orthogonal Grid      : {res['grid_layout']}")
    print(f" Spacing (Between)    : X = {res['spacing_x_m']} m, Y = {res['spacing_y_m']} m")
    print(f" Spacing (From Wall)  : X = {res['wall_margin_x_m']} m, Y = {res['wall_margin_y_m']} m")
    print("=" * 60)

if __name__ == "__main__":
    main()
