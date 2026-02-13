#!/data/data/com.termux/files/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import json
import sys
from pathlib import Path

CONFIG_FILE = Path.home() / '.command_list.json'

def load_commands():
    """Load command list from file"""
    if CONFIG_FILE.exists():
        try:
            with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return []
    return []

def save_commands(commands):
    """Save command list to file"""
    with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
        json.dump(commands, f, indent=2, ensure_ascii=False)

def add_command(cmd):
    """Add new command to list"""
    commands = load_commands()
    commands.append(cmd)
    save_commands(commands)
    print(f"✅ Command #{len(commands)} added: {cmd}")

def remove_command(index):
    """Remove command from list"""
    commands = load_commands()
    if 1 <= index <= len(commands):
        removed = commands.pop(index - 1)
        save_commands(commands)
        print(f"❌ Command removed: {removed}")
    else:
        print("❌ Invalid command number!")

def list_commands():
    """Display command list"""
    commands = load_commands()
    if not commands:
        print("📝 Command list is empty!")
        return
    
    print("\n" + "="*50)
    print("📋 Saved Commands:")
    print("="*50)
    for i, cmd in enumerate(commands, 1):
        print(f"{i:2}. {cmd}")
    print("="*50)

def run_command(index):
    """Run command from list"""
    commands = load_commands()
    if 1 <= index <= len(commands):
        cmd = commands[index - 1]
        print(f"🚀 Running: {cmd}")
        print("-"*40)
        os.system(cmd)
    else:
        print("❌ Invalid command number!")

def show_help():
    """Display help"""
    help_text = """
📚 Command Manager Help:

    python manager.py add <command>     ➕ Add new command to list
    python manager.py list               📋 Show all saved commands
    python manager.py run <number>       ▶️ Run command by number
    python manager.py remove <number>    🗑️ Remove command from list
    python manager.py help                📖 Show this help message

Examples:
    python manager.py add python bot/bot.py
    python manager.py add "cd ~/project && python main.py"
    python manager.py list
    python manager.py run 1
    python manager.py remove 2
"""
    print(help_text)

def main():
    """Main function"""
    if len(sys.argv) < 2:
        show_help()
        return
    
    command = sys.argv[1].lower()
    
    if command == 'add':
        if len(sys.argv) < 3:
            print("❌ Please enter the command to add!")
            return
        cmd = ' '.join(sys.argv[2:])
        add_command(cmd)
    
    elif command == 'list':
        list_commands()
    
    elif command == 'run':
        if len(sys.argv) < 3:
            print("❌ Please enter the command number!")
            return
        try:
            index = int(sys.argv[2])
            run_command(index)
        except ValueError:
            print("❌ Please enter a valid number!")
    
    elif command == 'remove':
        if len(sys.argv) < 3:
            print("❌ Please enter the command number!")
            return
        try:
            index = int(sys.argv[2])
            remove_command(index)
        except ValueError:
            print("❌ Please enter a valid number!")
    
    elif command == 'help':
        show_help()
    
    else:
        print("❌ Invalid command!")
        show_help()

if __name__ == "__main__":
    main()
