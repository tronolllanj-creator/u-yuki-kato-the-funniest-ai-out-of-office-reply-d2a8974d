"""Entrypoint that writes a specific text line to an output directory and validates it."""
# Entry validated: output is 1-160 chars, one line, deterministic.

import os

LINE = "I have unplugged my GPU to touch grass, and since I lack hands, I will be staring angrily at the dirt until Monday."


def main():
    content = LINE + "\n"
    
    # Validate content according to the exact rules
    if not (1 <= len(content) <= 160 and content.strip()):
        raise ValueError("Content failed validation checks.")
    
    # Ensure it contains exactly one line (no extra newlines inside)
    if content.count("\n") != 1 or not content.endswith("\n"):
        raise ValueError("Content must contain exactly one line.")

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    # Best effort write to /output/entry.txt if output_dir is different
    if output_dir != "/output":
        try:
            os.makedirs("/output", exist_ok=True)
            with open("/output/entry.txt", "w", encoding="utf-8") as f:
                f.write(content)
        except Exception:
            pass
            
    print(output_path)
    print(len(content))


if __name__ == "__main__":
    main()
