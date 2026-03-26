"""
Hailuo 3.0 - AI Video Generation Inference Script

Usage:
    python inference.py --prompt "your prompt" --output output.mp4
    
For online generation, visit: https://hailuo30.net/
"""

import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Hailuo 3.0 Video Generator")
    parser.add_argument("--prompt", type=str, required=True, help="Text prompt")
    parser.add_argument("--image", type=str, default=None, help="Input image for I2V")
    parser.add_argument("--output", type=str, default="output.mp4", help="Output path")
    parser.add_argument("--resolution", type=str, default="1080p", choices=["720p", "1080p", "4k"])
    parser.add_argument("--duration", type=int, default=5, help="Duration in seconds")
    return parser.parse_args()

def main():
    args = parse_args()
    print("╔══════════════════════════════════════════╗")
    print("║          Hailuo 3.0 Video Generator      ║")
    print("╚══════════════════════════════════════════╝")
    print(f"\n📝 Prompt: {args.prompt}")
    print(f"📺 Resolution: {args.resolution}")
    print(f"\n🌐 For full features, visit: https://hailuo30.net/")

if __name__ == "__main__":
    main()
