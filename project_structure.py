import os

def generate_project_structure(root_dir, exclude_dirs=None, exclude_files=None):
    # Helper function to format directory structure
    def format_structure(root, level=0):
        indent = '│   ' * level
        result = []
        
        # Separate directories and files
        directories = [name for name in sorted(os.listdir(root)) if os.path.isdir(os.path.join(root, name))]
        files = [name for name in sorted(os.listdir(root)) if os.path.isfile(os.path.join(root, name))]
        
        # Ensure 'src' and 'Test-Output' are prioritized, '.xml' files last
        directories.sort(key=lambda d: (d != 'src', d != 'Test-Output', d))  # 'src' and 'Test-Output' come first
        files.sort(key=lambda f: (not f.endswith('.xml'), f))  # '.xml' files come last

        # Process directories first
        for name in directories:
            path = os.path.join(root, name)
            if name in exclude_dirs: 
                continue
            result.append(f"{indent}├── {name}")
            result.extend(format_structure(path, level + 1))
        
        # Process files next
        for name in files:
            if name in exclude_files:
                continue
            result.append(f"{indent}└── {name}")
        
        return result

    # Print formatted project structure
    if os.path.exists(root_dir):
        project_name = os.path.basename(root_dir)
        print(f"{project_name}")  # Print the top-level project name
        structure = format_structure(root_dir)
        for line in structure:
            print(line)
    else:
        print(f"Error: The path '{root_dir}' does not exist.")

if __name__ == '__main__':
    # Input the Maven project path
    project_path = input("Enter the path to the Maven test automation project: ").strip()
    # Define directories and files to exclude
    exclude_dirs = ['.git', 'node_modules', 'target']  # Add any other directories to exclude
    exclude_files = ['.gitattributes', '.gitignore']  # Exclude specific files
    generate_project_structure(project_path, exclude_dirs=exclude_dirs, exclude_files=exclude_files)