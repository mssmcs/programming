#!/usr/bin/env python3
import os
import json
from pathlib import Path

def explore_repository(repo_path):
    """
    Explore the structure of a GitHub repository and generate a comprehensive summary.
    
    :param repo_path: Path to the local repository
    :return: Dictionary containing repository structure and details
    """
    repo_info = {
        "repository_root": repo_path,
        "directory_tree": {},
        "file_types": {},
        "summary": {
            "total_files": 0,
            "total_directories": 0,
            "file_type_breakdown": {}
        },
        "github_workflows": [],
        "index_files": []
    }
    
    # Special configuration tracking
    special_configs = {
        'frameworks': [],
        'package_managers': [],
        'development_configs': [],
        'ci_cd_configs': []
    }
    
    # Predefined lists of configuration files and directories to track
    framework_indicators = {
        'react': ['react-config.js', 'next.config.js', '.reactrc'],
        'vue': ['vue.config.js', '.vuerc'],
        'angular': ['angular.json', '.angular-cli.json'],
        'svelte': ['svelte.config.js'],
        'django': ['manage.py', 'settings.py'],
        'flask': ['app.py', 'config.py'],
        'express': ['app.js', 'server.js'],
        'fastapi': ['main.py'],
        'spring_boot': ['pom.xml', 'mvnw', 'mvnw.cmd', 'build.gradle']
    }
    
    package_manager_indicators = {
        'npm': ['package.json', 'package-lock.json'],
        'yarn': ['yarn.lock'],
        'pip': ['requirements.txt', 'Pipfile'],
        'poetry': ['pyproject.toml'],
        'maven': ['pom.xml'],
        'gradle': ['build.gradle', 'gradle.properties']
    }
    
    development_config_indicators = {
        'docker': ['Dockerfile', 'docker-compose.yml'],
        'kubernetes': ['deployment.yaml', 'service.yaml', 'ingress.yaml'],
        'vscode': ['.vscode'],
        'jetbrains': ['.idea'],
        'env_configs': ['.env', '.env.local', '.env.development']
    }
    
    ci_cd_indicators = {
        'github_actions': ['.github/workflows'],
        'travis_ci': ['.travis.yml'],
        'gitlab_ci': ['.gitlab-ci.yml'],
        'jenkins': ['Jenkinsfile'],
        'circleci': ['.circleci/config.yml']
    }
    
    # Walk through the repository
    for root, dirs, files in os.walk(repo_path):
        # Relative path from repository root
        relative_path = os.path.relpath(root, repo_path)
        
        # GitHub workflow detection
        if '.github' in root.split(os.path.sep):
            for file in files:
                if file.endswith(('.yml', '.yaml')):
                    workflow_path = os.path.join(relative_path, file)
                    repo_info['github_workflows'].append(workflow_path)
        
        # Index file detection
        index_candidates = [
            'index.md', 'README.md', 'readme.md',  # Markdown files
            'index.txt', 'readme.txt',  # Text files
            'index.html', 'readme.html',  # HTML files
            'index.rst'  # ReStructuredText files
        ]
        
        for index_file in index_candidates:
            if index_file in files:
                # Full path to the index file
                full_path = os.path.join(root, index_file)
                
                # Relative path from repository root
                file_relative_path = os.path.relpath(full_path, repo_path)
                
                # Read first 1000 characters of the file
                try:
                    with open(full_path, 'r', encoding='utf-8') as f:
                        content = f.read(1000)  # Read first 1000 characters
                        
                        repo_info['index_files'].append({
                            'path': file_relative_path,
                            'type': os.path.splitext(index_file)[1],
                            'preview': content.strip()
                        })
                except Exception as e:
                    print(f"Error reading {full_path}: {e}")
        
        # Check for framework indicators
        for framework, indicators in framework_indicators.items():
            for indicator in indicators:
                if indicator in files or indicator in relative_path:
                    special_configs['frameworks'].append({
                        'framework': framework,
                        'path': os.path.join(relative_path, indicator)
                    })
        
        # Check for package manager indicators
        for manager, indicators in package_manager_indicators.items():
            for indicator in indicators:
                if indicator in files:
                    special_configs['package_managers'].append({
                        'manager': manager,
                        'path': os.path.join(relative_path, indicator)
                    })
        
        # Check for development config indicators
        for config_type, indicators in development_config_indicators.items():
            for indicator in indicators:
                if indicator in files or indicator in relative_path:
                    special_configs['development_configs'].append({
                        'type': config_type,
                        'path': os.path.join(relative_path, indicator)
                    })
        
        # Check for CI/CD config indicators
        for ci_type, indicators in ci_cd_indicators.items():
            for indicator in indicators:
                if indicator in relative_path or any(ind in files for ind in indicator.split('/')):
                    special_configs['ci_cd_configs'].append({
                        'type': ci_type,
                        'path': os.path.join(relative_path, indicator)
                    })
        
        # Skip version control and hidden directories (except .github)
        dirs[:] = [d for d in dirs if not (d.startswith('.') and d != '.github') and d != 'node_modules']
        
        # Track directories
        if relative_path != '.':
            repo_info['summary']['total_directories'] += 1
            
            # Create nested dictionary for directory structure
            current_level = repo_info['directory_tree']
            for part in relative_path.split(os.path.sep):
                current_level = current_level.setdefault(part, {})
        
        # Process files
        for file in files:
            # Skip hidden files
            if file.startswith('.'):
                continue
            
            repo_info['summary']['total_files'] += 1
            
            # Get file extension
            file_ext = os.path.splitext(file)[1].lower()
            if file_ext:
                repo_info['file_types'][file] = file_ext
                repo_info['summary']['file_type_breakdown'][file_ext] = \
                    repo_info['summary']['file_type_breakdown'].get(file_ext, 0) + 1
            
            # Add file to directory structure
            current_level = repo_info['directory_tree']
            if relative_path != '.':
                for part in relative_path.split(os.path.sep):
                    current_level = current_level[part]
            current_level[file] = None
    
    # Add special configurations to repository info
    repo_info['special_configs'] = special_configs
    
    return repo_info

def generate_repository_report(repo_info, output_file='repository_summary.md'):
    """
    Generate a markdown report of the repository structure.
    
    :param repo_info: Dictionary containing repository information
    :param output_file: Path to output markdown file
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        # Repository Overview
        f.write(f"# Repository Structure Overview\n\n")
        f.write(f"**Repository Root:** {repo_info['repository_root']}\n\n")
        f.write(f"## Summary Statistics\n")
        f.write(f"- Total Directories: {repo_info['summary']['total_directories']}\n")
        f.write(f"- Total Files: {repo_info['summary']['total_files']}\n\n")
        
        # File Type Breakdown
        f.write(f"## File Type Breakdown\n")
        for ext, count in repo_info['summary']['file_type_breakdown'].items():
            f.write(f"- {ext}: {count} files\n")
        
        # Detailed Directory Tree
        f.write(f"\n## Directory Structure\n")
        
        def write_tree(tree, indent=''):
            for key, value in tree.items():
                f.write(f"{indent}- {key}\n")
                if isinstance(value, dict):
                    write_tree(value, indent + '  ')
        
        write_tree(repo_info['directory_tree'])
        
        # Detailed File Types
        f.write(f"\n## Detailed File Types\n")
        for file, ext in repo_info['file_types'].items():
            f.write(f"- {file}: {ext}\n")
        
        # GitHub Workflows
        if repo_info.get('github_workflows'):
            f.write(f"\n## GitHub Workflows\n")
            for workflow in repo_info['github_workflows']:
                f.write(f"- {workflow}\n")
        
        # Special Configurations
        special_configs = repo_info.get('special_configs', {})
        
        # Frameworks
        if special_configs.get('frameworks'):
            f.write(f"\n## Detected Frameworks\n")
            for framework in special_configs['frameworks']:
                f.write(f"- {framework['framework']}: {framework['path']}\n")
        
        # Package Managers
        if special_configs.get('package_managers'):
            f.write(f"\n## Package Managers\n")
            for manager in special_configs['package_managers']:
                f.write(f"- {manager['manager']}: {manager['path']}\n")
        
        # Development Configurations
        if special_configs.get('development_configs'):
            f.write(f"\n## Development Configurations\n")
            for config in special_configs['development_configs']:
                f.write(f"- {config['type']}: {config['path']}\n")
        
        # CI/CD Configurations
        if special_configs.get('ci_cd_configs'):
            f.write(f"\n## CI/CD Configurations\n")
            for config in special_configs['ci_cd_configs']:
                f.write(f"- {config['type']}: {config['path']}\n")
        
        # Index Files
        if repo_info.get('index_files'):
            f.write(f"\n## Index Files\n")
            for index_file in repo_info['index_files']:
                f.write(f"### {index_file['path']}\n")
                f.write(f"**File Type:** {index_file['type']}\n\n")
                f.write(f"**Preview:**\n```\n{index_file['preview']}\n```\n\n")
    
    print(f"Repository summary written to {output_file}")

def main():
    # Specify the path to the cloned repository
    repo_path = input("Enter the full path to the cloned repository: ")
    
    # Validate repository path
    if not os.path.exists(repo_path):
        print("Error: Invalid repository path")
        return
    
    # Explore repository
    repo_info = explore_repository(repo_path)
    
    # Generate report
    generate_repository_report(repo_info)

if __name__ == "__main__":
    main()