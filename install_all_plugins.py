#!/usr/bin/env python3
"""
Install all plugins from wshobson/agents marketplace to Claude Code globally
"""
import json
import os
import shutil
from pathlib import Path

# Paths
CLAUDE_DIR = Path.home() / ".claude"
PLUGINS_DIR = CLAUDE_DIR / "plugins"
MARKETPLACE_DIR = PLUGINS_DIR / "marketplaces" / "wshobson-agents"
MARKETPLACE_PLUGINS_DIR = MARKETPLACE_DIR / "plugins"
MANIFEST_FILE = MARKETPLACE_DIR / ".claude-plugin" / "marketplace.json"

def read_manifest():
    """Read the marketplace manifest file"""
    with open(MANIFEST_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_installed_plugins():
    """Get list of already installed plugins"""
    installed = set()
    if PLUGINS_DIR.exists():
        for item in PLUGINS_DIR.iterdir():
            if item.is_dir() and item.name != "marketplaces":
                installed.add(item.name)
    return installed

def install_plugin(plugin_name, plugin_source):
    """Install a single plugin by creating symlink or copying"""
    source_path = MARKETPLACE_DIR / plugin_source
    target_path = PLUGINS_DIR / plugin_name

    # Skip if already installed
    if target_path.exists():
        print(f"[SKIP] Skipping {plugin_name} (already installed)")
        return False

    # Check if source exists
    if not source_path.exists():
        print(f"[WARN] Warning: Source not found for {plugin_name}: {source_path}")
        return False

    try:
        # Try to create symlink first (Windows requires admin privileges or Developer Mode)
        try:
            os.symlink(source_path, target_path, target_is_directory=True)
            print(f"[OK] Installed {plugin_name} (symlink)")
            return True
        except OSError:
            # If symlink fails, copy the directory
            shutil.copytree(source_path, target_path, symlinks=True)
            print(f"[OK] Installed {plugin_name} (copied)")
            return True
    except Exception as e:
        print(f"[FAIL] Failed to install {plugin_name}: {e}")
        return False

def main():
    print("=" * 60)
    print("Installing all plugins from wshobson/agents marketplace")
    print("=" * 60)
    print()

    # Verify marketplace is installed
    if not MARKETPLACE_DIR.exists():
        print("[ERROR] Error: wshobson/agents marketplace not found")
        print(f"   Expected location: {MARKETPLACE_DIR}")
        print("   Please run: /plugin marketplace add wshobson/agents")
        return

    # Read manifest
    print(f"[INFO] Reading manifest from {MANIFEST_FILE}")
    manifest = read_manifest()

    plugins = manifest.get("plugins", [])
    print(f"[INFO] Found {len(plugins)} plugins in marketplace")
    print()

    # Get already installed plugins
    installed_before = get_installed_plugins()
    print(f"[INFO] Currently installed: {len(installed_before)} plugins")
    print()

    # Install each plugin
    installed_count = 0
    skipped_count = 0
    failed_count = 0

    for plugin in plugins:
        plugin_name = plugin.get("name")
        plugin_source = plugin.get("source")

        if not plugin_name or not plugin_source:
            print(f"[WARN] Warning: Invalid plugin entry: {plugin}")
            continue

        result = install_plugin(plugin_name, plugin_source)
        if result:
            installed_count += 1
        elif (PLUGINS_DIR / plugin_name).exists():
            skipped_count += 1
        else:
            failed_count += 1

    print()
    print("=" * 60)
    print("Installation Summary")
    print("=" * 60)
    print(f"[OK] Installed: {installed_count} plugins")
    print(f"[SKIP] Skipped (already installed): {skipped_count} plugins")
    print(f"[FAIL] Failed: {failed_count} plugins")
    print(f"[INFO] Total plugins: {len(plugins)}")
    print()

    # Get final installed plugins
    installed_after = get_installed_plugins()
    print(f"[SUCCESS] Total globally installed plugins: {len(installed_after)}")
    print()
    print("All plugins are now globally available in Claude Code!")

if __name__ == "__main__":
    main()
