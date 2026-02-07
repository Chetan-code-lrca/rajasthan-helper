import os

# Create tests directory
tests_dir = r'C:\Users\cheta\rajasthan-helper\tests'
os.makedirs(tests_dir, exist_ok=True)

# Create __init__.py file
init_file = os.path.join(tests_dir, '__init__.py')
with open(init_file, 'w') as f:
    f.write('')

# Verify and print results
if os.path.exists(tests_dir) and os.path.exists(init_file):
    import os.path
    print(f"✓ Directory created: {tests_dir}")
    print(f"  - Exists: {os.path.isdir(tests_dir)}")
    print(f"✓ File created: {init_file}")
    print(f"  - Exists: {os.path.isfile(init_file)}")
    print(f"  - Size: {os.path.getsize(init_file)} bytes")
    print("\nDirectory contents:")
    for item in os.listdir(tests_dir):
        print(f"  - {item}")
else:
    print("✗ Failed to create directory or file")
